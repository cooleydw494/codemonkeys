from pandas.io.common import file_exists

from codemonkeys.builders.committer import Committer
from codemonkeys.builders.file_iterator import FileIterator
from codemonkeys.builders.file_prompter import FilePrompter
from codemonkeys.builders.output_path_resolver import OutputPathResolver
from codemonkeys.builders.summarizer import Summarizer
from codemonkeys.entities.automation import Automation
from codemonkeys.utils.misc.file_ops import get_file_contents, write_file_contents
from codemonkeys.utils.monk.theme_functions import print_t


class Default(Automation):

    def run(self) -> None:
        m = self._monkey

        # Prepare summarized or unsummarized context
        context = None
        if m.CONTEXT_FILE_PATH is not None and m.CONTEXT_SUMMARY_PROMPT is not None:
            context = (Summarizer()
                       .context_from_file(m.CONTEXT_FILE_PATH)
                       .model(m.SUMMARY_MODEL, m.SUMMARY_TEMP, m.SUMMARY_MAX_TOKENS)
                       .prompt(m.CONTEXT_SUMMARY_PROMPT)
                       .summarize())
        elif m.CONTEXT_FILE_PATH is not None:
            context = get_file_contents(m.CONTEXT_FILE_PATH)

        # Build a FileIterator and filter files
        file_iterator = (FileIterator()
                         .work_path(m.WORK_PATH)
                         .include_exts(m.INCLUDE_EXTS)
                         .filepath_match_include(m.FILEPATH_MATCH_INCLUDE)
                         .filepath_match_exclude(m.FILEPATH_MATCH_EXCLUDE)
                         .token_count_model(m.MAIN_MODEL, m.MAIN_TEMP, m.FILTER_MAX_TOKENS)
                         .filter_files())

        # Build a FilePrompter for prompting output on each file
        file_prompter = (FilePrompter()
                         .model(m.MAIN_MODEL, m.MAIN_TEMP, m.MAIN_MAX_TOKENS)
                         .finalize_output(True)  # hard-coded to use FinalizeOutput Func
                         .main_prompt(m.MAIN_PROMPT)
                         .context(context)
                         .output_prompt(m.OUTPUT_PROMPT)
                         .ultimatum_prompt(m.MAIN_PROMPT_ULTIMATUM))

        # Build an OutputPathResolve to resolve filepaths for writing
        output_path_resolver = (OutputPathResolver()
                                .output_path(m.OUTPUT_PATH)
                                .output_filename_append(m.OUTPUT_FILENAME_APPEND)
                                .output_ext(m.OUTPUT_EXT)
                                .relative_from_root(m.WORK_PATH if m.RELATIVE_OUTPUT_PATHS else None))

        # If enabled, build a Committer for GPT Git Commits
        committer = None
        if m.GPT_GIT_COMMITS:
            committer = (Committer(repo_path=m.OUTPUT_PATH)
                         .model('gpt-3.5-turbo', 0.7, 2000))

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
                continue

            # Write output to file
            write_file_contents(output_file_path, new_content)
            print(f"Output saved to: {output_file_path}", 'info')

            # Commit changes if a Committer was configured
            if committer is not None:
                committer.message_from_context(old_content, new_content).commit()