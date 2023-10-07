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
from codemonkeys.special_types import OMonkey
from codemonkeys.utils.file_ops import get_file_contents, write_file_contents
from codemonkeys.utils.monk.theme_functions import print_t


class Default(Automation):

    def __init__(self, named_args: Dict[str, Any], unnamed_args: List[str], monkey: OMonkey = None):
        super().__init__(named_args, unnamed_args, monkey)

    def run(self) -> None:
        m = self.get_monkey()

        # Prepare summarized or unsummarized context
        if m.CONTEXT_FILE_PATH is None:
            context = ''
        elif m.CONTEXT_SUMMARY_PROMPT is not None:
            context = (Summarizer()
                       .context_from_file(m.CONTEXT_FILE_PATH)
                       .model(m.SUMMARY_MODEL, m.SUMMARY_TEMP, m.SUMMARY_MAX_TOKENS)
                       .prompt(m.CONTEXT_SUMMARY_PROMPT)
                       .summarize())
        else:
            context = get_file_contents(m.CONTEXT_FILE_PATH)

        # Prepare Output Checker
        output_checker = None
        if m.OUTPUT_CHECK_PROMPT is not None:
            output_checker = (OutputChecker()
                              .model(m.OUTPUT_CHECK_MODEL, m.OUTPUT_CHECK_TEMP, m.OUTPUT_CHECK_MAX_TOKENS)
                              .tries(m.OUTPUT_TRIES)
                              .prompt(m.OUTPUT_CHECK_PROMPT))

        # Prepare FileIterator and filter files
        file_iterator = (FileIterator()
                         .token_count_model(m.MAIN_MODEL, m.MAIN_TEMP, m.FILE_SELECT_MAX_TOKENS)
                         .file_types_included(m.FILE_TYPES_INCLUDED)
                         .filepath_match_include(m.FILEPATH_MATCH_INCLUDE)
                         .filepath_match_exclude(m.FILEPATH_MATCH_EXCLUDE)
                         .work_path(m.WORK_PATH)
                         .filter_files())

        # Prepare OutputPathResolver, configuring how to create output paths using each file's path
        output_path_resolver = (OutputPathResolver()
                                .output_path(m.OUTPUT_PATH)
                                .output_filename_append(m.OUTPUT_FILENAME_APPEND)
                                .output_ext(m.OUTPUT_EXT)
                                .work_path(m.WORK_PATH)
                                .use_work_path_relative_location(True))

        # Prepare Committer to handle git commits
        committer = None
        if m.COMMIT_STYLE == 'gpt':
            committer = Committer(m.OUTPUT_PATH).model('3', 0.75, m.SUMMARY_MAX_TOKENS)
        elif m.COMMIT_STYLE == 'static':
            committer = Committer(m.OUTPUT_PATH).message(m.STATIC_COMMIT_MESSAGE)

        # Iterate through filtered files
        while True:

            files_remaining = len(file_iterator.get_filtered_files())
            print_t(f"Files remaining: {files_remaining}", 'info')

            file_path = file_iterator.pop_file()
            if file_path is None:
                print_t("All Files Handled.", 'done')
                break

            output_file_path = output_path_resolver.get_output_path(file_path)
            if m.SKIP_EXISTING_OUTPUT_FILES and file_exists(output_file_path):
                print_t(f"Skipping file, output exists at: {output_file_path}", 'quiet')
                continue

            print(f"Processing file: {file_path}")
            old_content = get_file_contents(file_path)

            # Create a copy for file-specific _prompt replacements
            file_name = os.path.basename(file_path)
            _m = m.prompt_replace('{the-file}', file_name)

            # Set up a FilePrompter for the current file
            file_prompter = (FilePrompter()
                             .model(m.MAIN_MODEL, m.MAIN_TEMP, m.MAIN_MAX_TOKENS)
                             .file_path(file_path)
                             .main_prompt(_m.MAIN_PROMPT)
                             .context(context)
                             .output_example_prompt(_m.OUTPUT_EXAMPLE_PROMPT)
                             .ultimatum_prompt(_m.MAIN_PROMPT_ULTIMATUM)
                             .output_remove_strings(_m.OUTPUT_REMOVE_STRINGS))

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
                if m.COMMIT_STYLE == 'gpt':
                    committer.message_from_context(old_content, new_content)
                committer.commit()
                message = committer.get_message()
                print_t(f"Changes committed to git with message: {message}.", 'info')
