import os
from typing import Dict, Any, List

from pandas.io.common import file_exists

from codemonkeys.builders.committer import Committer
from codemonkeys.builders.file_iterator import FileIterator
from codemonkeys.builders.file_prompter import FilePrompter
from codemonkeys.builders.output_checker import OutputChecker
from codemonkeys.builders.output_path_resolver import OutputPathResolver
from codemonkeys.builders.summarizer import Summarizer
from codemonkeys.entities.automation import Automation
from codemonkeys.utils.file_ops import get_file_contents, write_file_contents
from codemonkeys.utils.monk.theme_functions import print_t


class Default(Automation):
    required_config_keys = ['MAIN_PROMPT']

    # TODO: implement this in base class
    required_config_keys_if = {
        'OUTPUT_CHECK_PROMPT': ['OUTPUT_TRIES'],
    }

    def __init__(self, named_args: Dict[str, Any], unnamed_args: List[str]):
        super().__init__(named_args, unnamed_args)

    def run(self) -> None:
        mc = self.monkey_config
        # replace cop-syntax file contents references
        mc.cop_paths()

        # Prepare summarized or unsummarized _context
        if mc.CONTEXT_FILE_PATH is None:
            context = ''
        elif mc.CONTEXT_SUMMARY_PROMPT is not None:
            context = (Summarizer()
                       .context_from_file(mc.CONTEXT_FILE_PATH)
                       .model(mc.SUMMARY_MODEL, mc.SUMMARY_TEMP, mc.SUMMARY_MAX_TOKENS)
                       .prompt(mc.CONTEXT_SUMMARY_PROMPT)
                       .summarize())
        else:
            context = get_file_contents(mc.CONTEXT_FILE_PATH)

        # Prepare Output Checker
        output_checker = None
        if mc.OUTPUT_CHECK_PROMPT is not None:
            output_checker = (OutputChecker()
                              .model(mc.OUTPUT_CHECK_MODEL, mc.OUTPUT_CHECK_TEMP, mc.OUTPUT_CHECK_MAX_TOKENS)
                              .tries(mc.OUTPUT_TRIES)
                              .prompt(mc.OUTPUT_CHECK_PROMPT))

        # Prepare FileIterator and filter files
        file_iterator = (FileIterator()
                         .token_count_model(mc.MAIN_MODEL, mc.MAIN_TEMP, mc.FILE_SELECT_MAX_TOKENS)
                         .file_types_included(mc.FILE_TYPES_INCLUDED)
                         .filepath_match_include(mc.FILEPATH_MATCH_INCLUDE)
                         .filepath_match_exclude(mc.FILEPATH_MATCH_EXCLUDE)
                         .work_path(mc.WORK_PATH)
                         .filter_files())

        # Prepare OutputPathResolver, configuring how to create output paths using each file's path
        output_path_resolver = (OutputPathResolver()
                                .output_path(mc.OUTPUT_PATH)
                                .output_filename_append(mc.OUTPUT_FILENAME_APPEND)
                                .output_ext(mc.OUTPUT_EXT)
                                .work_path(mc.WORK_PATH)
                                .use_work_path_relative_location(True))

        # Prepare Committer to handle git commits
        committer = None
        if mc.COMMIT_STYLE == 'gpt':
            committer = Committer(mc.OUTPUT_PATH).model('3', 0.75, mc.SUMMARY_MAX_TOKENS)
        elif mc.COMMIT_STYLE == 'static':
            committer = Committer(mc.OUTPUT_PATH).message(mc.STATIC_COMMIT_MESSAGE)

        # Iterate through filtered files
        while True:

            files_remaining = len(file_iterator.get_filtered_files())
            print_t(f"Files remaining: {files_remaining}", 'info')

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

            # Create a copy for file-specific _prompt replacements
            file_name = os.path.basename(file_path)
            _mc = mc.replace_prompt_str('{the-file}', file_name)

            # Set up a FilePrompter for the current file
            file_prompter = (FilePrompter()
                             .model(mc.MAIN_MODEL, mc.MAIN_TEMP, mc.MAIN_MAX_TOKENS)
                             .file_path(file_path)
                             .main_prompt(_mc.MAIN_PROMPT)
                             .context(context)
                             .output_example_prompt(_mc.OUTPUT_EXAMPLE_PROMPT)
                             .ultimatum_prompt(_mc.MAIN_PROMPT_ULTIMATUM)
                             .output_remove_strings(_mc.OUTPUT_REMOVE_STRINGS))

            # Generate output, checking it if an OutputChecker is configured
            new_content = None
            if output_checker is not None:
                output_checker.set_current_try(1)
                while output_checker.has_tries():
                    output = file_prompter.get_output()
                    if output is None:
                        print_t(f"Valid output could not be generated for: {file_path}", 'error')
                        print_t("Output Check not run because no output was generated.", 'info')
                        break
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
                    committer.message_from_context(old_content, new_content)
                committer.commit()
                message = committer.get_message()
                print_t(f"Changes committed to git with message: {message}.", 'info')
