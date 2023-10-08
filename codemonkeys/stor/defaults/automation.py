from typing import Dict, Any, List

from pandas.io.common import file_exists

from codemonkeys.builders.committer import Committer
from codemonkeys.builders.file_iterator import FileIterator
from codemonkeys.builders.file_prompter import FilePrompter
from codemonkeys.builders.output_fixer import OutputFixer
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

        # Prepare Output Fixer
        output_fixer = None
        if m.FIX_OUTPUT_PROMPT is not None:
            output_fixer = (OutputFixer()
                            .model(m.FIX_OUTPUT_MODEL, m.FIX_OUTPUT_TEMP, m.FIX_OUTPUT_MAX_TOKENS)
                            .prompt(m.FIX_OUTPUT_PROMPT))

        # Prepare FileIterator and filter files
        file_iterator = (FileIterator()
                         .token_count_model(m.MAIN_MODEL, m.MAIN_TEMP, m.FILE_SELECT_MAX_TOKENS)
                         .file_types_included(m.FILE_TYPES_INCLUDED)
                         .filepath_match_include(m.FILEPATH_MATCH_INCLUDE)
                         .filepath_match_exclude(m.FILEPATH_MATCH_EXCLUDE)
                         .work_path(m.WORK_PATH)
                         .filter_files())

        # Set up a FilePrompter for prompting output on each file
        file_prompter = (FilePrompter()
                         .model(m.MAIN_MODEL, m.MAIN_TEMP, m.MAIN_MAX_TOKENS)
                         .main_prompt(m.MAIN_PROMPT)
                         .context(context)
                         .output_example_prompt(m.OUTPUT_EXAMPLE_PROMPT)
                         .ultimatum_prompt(m.MAIN_PROMPT_ULTIMATUM)
                         .output_remove_strings(m.OUTPUT_REMOVE_STRINGS))

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
            committer = Committer(m.OUTPUT_PATH).model('gpt-3.5-turbo', 0.7, 2000)
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
            new_content = file_prompter.file_path(file_path).get_output()

            if new_content is None:
                print_t(f"Valid output could not be generated for: {file_path}", 'error')
                continue

            # Fix output if an OutputFixer is configured
            if output_fixer is not None:
                new_content = output_fixer.fix(new_content)

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
