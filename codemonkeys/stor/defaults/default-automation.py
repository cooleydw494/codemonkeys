import argparse
import os
from typing import Dict, Any, List

from codemonkeys.composables.committer import Committer
from codemonkeys.composables.file_iterator import FileIterator
from codemonkeys.base_entities.automation_class import Automation
from codemonkeys.composables.output_checker import OutputChecker
from codemonkeys.composables.output_path_resolver import OutputPathResolver
from codemonkeys.utils.file_ops import get_file_contents, file_exists, write_file_contents
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.composables.file_prompter import FilePrompter
from codemonkeys.composables.summarizer import Summarizer


class Default(Automation):
    required_config_keys = ['MAIN_PROMPT']

    # TODO: implement this in base class
    required_config_keys_if = {
        'OUTPUT_CHECK_PROMPT': ['OUTPUT_TRIES'],
    }

    def __init__(self, monk_args: argparse.Namespace, named_args: Dict[str, Any], unnamed_args: List[str]):
        super().__init__(monk_args, named_args, unnamed_args)

    def run(self):
        mc = self.monkey_config
        # replace cop-syntax file contents references
        mc.cop_paths()

        # Prepare summarized or unsummarized context
        if mc.CONTEXT_FILE_PATH is None:
            context = ''
        elif mc.CONTEXT_SUMMARY_PROMPT is not None:
            context = (Summarizer()
                       .set_context_via_file(mc.CONTEXT_FILE_PATH)
                       .set_model(mc.SUMMARY_MODEL, mc.SUMMARY_TEMP, mc.SUMMARY_MAX_TOKENS)
                       .set_prompt(mc.CONTEXT_SUMMARY_PROMPT)
                       .summarize())
        else:
            context = get_file_contents(mc.CONTEXT_FILE_PATH)

        # Prepare Output Checker
        output_checker = None
        if mc.OUTPUT_CHECK_PROMPT is not None:
            output_checker = (OutputChecker()
                              .set_model(mc.OUTPUT_CHECK_MODEL, mc.OUTPUT_CHECK_TEMP, mc.OUTPUT_CHECK_MAX_TOKENS)
                              .set_tries(mc.OUTPUT_TRIES)
                              .set_prompt(mc.OUTPUT_CHECK_PROMPT))

        # Prepare FileIterator and filter files
        file_iterator = (FileIterator()
                         .set_token_count_model(mc.MAIN_MODEL, mc.MAIN_TEMP, mc.FILE_SELECT_MAX_TOKENS)
                         .set_file_types_included(mc.FILE_TYPES_INCLUDED)
                         .set_filepath_match_exclude(mc.FILEPATH_MATCH_EXCLUDE)
                         .set_work_path(mc.WORK_PATH)
                         .filter_files())

        # Prepare OutputPathResolver, configuring how to create output paths using each file's path
        output_path_resolver = (OutputPathResolver()
                                .set_output_path(mc.OUTPUT_PATH)
                                .set_output_filename_append(mc.OUTPUT_FILENAME_APPEND)
                                .set_output_ext(mc.OUTPUT_EXT)
                                .set_work_path(mc.WORK_PATH)
                                .set_use_work_path_relative_location(True))

        # Prepare Committer to handle git commits
        committer = None
        if mc.COMMIT_STYLE == 'gpt':
            committer = Committer(mc.OUTPUT_PATH).set_model('3', 0.75, mc.SUMMARY_MAX_TOKENS)
        elif mc.COMMIT_STYLE == 'static':
            committer = Committer(mc.OUTPUT_PATH).set_message(mc.STATIC_COMMIT_MESSAGE)

        # Iterate through filtered files
        while True:

            file_path = file_iterator.pop_file()
            if file_path is None:
                print_t("All Files Handled.", 'done')
                break

            output_file_path = output_path_resolver.get_output_path(file_path)
            if mc.SKIP_EXISTING_OUTPUT_FILES and file_exists(output_file_path):
                print_t(f"Skipping file, output exists at: {output_file_path}", 'quiet')
                continue

            print(f"Processing file: {file_path}")
            old_content = get_file_contents(file_path)

            # Create a copy for file-specific prompt replacements
            file_name = os.path.basename(file_path)
            _mc = mc.replace_prompt_str('{the-file}', file_name)

            # Set up a FilePrompter for the current file
            file_prompter = (FilePrompter()
                             .set_model(mc.MAIN_MODEL, mc.MAIN_TEMP, mc.MAIN_MAX_TOKENS)
                             .set_path(file_path)
                             .set_main_prompt(_mc.MAIN_PROMPT)
                             .set_context(context)
                             .set_output_example_prompt(_mc.OUTPUT_EXAMPLE_PROMPT)
                             .set_ultimatum_prompt(_mc.MAIN_PROMPT_ULTIMATUM)
                             .set_output_remove_strings(_mc.OUTPUT_REMOVE_STRINGS))

            # Generate output, checking it if an OutputChecker is configured
            new_content = None
            if output_checker is not None:
                output_checker.set_current_try(1)
                while output_checker.has_tries():
                    output = file_prompter.get_output()
                    output_valid = output_checker.check_output(output)
                    if output_valid:
                        new_content = output
                        break
            else:
                new_content = file_prompter.get_output()

            if new_content is None:
                print_t(f"Valid output could not be generated for: {file_path}", 'error')
                continue

            # Write output to file
            write_file_contents(output_file_path, new_content)
            print(f"Output saved to: {output_file_path}", 'info')

            # Commit changes if a Committer is configured
            if committer is not None:
                if mc.COMMIT_STYLE == 'gpt':
                    committer.set_message_via_content(old_content, new_content)
                committer.commit()
                message = committer.get_message()
                print_t(f"Changes committed to git with message: {message}.", 'info')
