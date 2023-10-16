import os

from codemonkeys.defs import content_sep, nl, nl2
from codemonkeys.funcs.write_file import WriteFile
from codemonkeys.utils.gpt.gpt_client import GPTClient
from pandas.io.common import file_exists

from codemonkeys.builders.committer import Committer
from codemonkeys.entities.automation import Automation
from codemonkeys.utils.misc.file_ops import get_file_contents
from codemonkeys.utils.monk.theme_functions import print_t

from codemonkeys.funcs.extract_list import ExtractList
from monkeys.scaffold import Scaffold as ScaffoldMonkey


class Scaffold(Automation):

    def run(self) -> None:
        m: ScaffoldMonkey = self._monkey

        # Fetch the context (should be a file detailing a codebase)
        context = get_file_contents(m.CONTEXT_FILE_PATH)

        extract_prompt = f"{m.FILE_EXTRACTION_PROMPT}:{nl}{content_sep}{nl}{context}{nl}{content_sep}"
        print_t(f"Filepath extraction prompt:{nl}{extract_prompt}{nl}", "quiet")

        # Use ExtractList Func to get a list of absolute filepaths that the context file references
        file_paths: list = (GPTClient(m.FILE_EXTRACTION_MODEL, m.FILE_EXTRACTION_TEMP, m.FILE_EXTRACTION_MAX_TOKENS)
                            .generate(extract_prompt, [ExtractList()], 'extract_list'))

        if len(file_paths) == 0:
            print_t("No filepaths were extracted. Exiting.", 'error')
            return

        print_t(f"Extracted {len(file_paths)} filepaths: {file_paths}", 'info')

        # If enabled, build a Committer for GPT Git Commits
        committer = None
        if m.GPT_GIT_COMMITS:
            committer = (Committer(repo_path=m.GIT_REPO_PATH)
                         .model('gpt-3.5-turbo', 0.7, 2000))

        # Build a WriteFile Func for prompting file writes
        # Note: PROJECT_ROOT is particularly important as it verifies no file is written outside of that dir
        # This is the primary safeguard against accidental file writes that could be destructive
        write_file_func = WriteFile(skip_existing=m.SKIP_EXISTING_OUTPUT_FILES, base_path=m.PROJECT_ROOT)

        # Iterate through filepaths and generate scaffolded files
        while True:

            files_remaining = len(file_paths)
            print_t(f"Filepaths remaining: {files_remaining}", 'info')

            if files_remaining == 0:
                print_t("All Filepaths Handled.", 'done')
                break
            file_path = os.path.expanduser(file_paths.pop())

            if m.SKIP_EXISTING_OUTPUT_FILES and file_exists(file_path):
                print_t(f"Skipping file, output exists at: {file_path}", 'quiet')
                continue

            print(f"Processing filepath: {file_path}")
            old_content = get_file_contents(file_path) if file_exists(file_path) else ''

            scaffold_prompt = (f"{m.MAIN_PROMPT}:{content_sep}{nl}{context}{content_sep}{nl2}The current file to "
                               f"implement/write is {file_path} (this is the absolute path for writing).")
            print_t(f"Scaffolding prompt:{nl}{scaffold_prompt}{nl}", "quiet")

            written_file_path = (GPTClient(m.MAIN_MODEL, m.MAIN_TEMP, m.MAIN_MAX_TOKENS)
                                 .generate(scaffold_prompt, [write_file_func], 'write_file'))

            if written_file_path is None:
                print_t(
                    f" No written filepath was returned, seeming to indicate a file was not written. Skipping "
                    f"file: {file_path}", 'warning')
                continue

            if written_file_path != file_path:
                print_t(f" The current file to implement/write was not written: {file_path}.", 'warning')
                continue

            new_content = get_file_contents(file_path) if file_exists(file_path) else ''

            # Commit changes if a Committer was configured
            if committer is not None:
                if file_path != written_file_path:
                    committer.message('Updated via CodeMonkeys with unexpected written file.')
                elif new_content != '':
                    committer.message_from_context(old_content, new_content).commit()
