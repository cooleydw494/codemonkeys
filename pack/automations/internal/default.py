import argparse
import os

from pack.modules.internal.config_mgmt.environment_checks import automation_env_checks
from pack.modules.internal.config_mgmt.monkey_config.load_monkey_config import load_monkey_config
from pack.modules.internal.gpt.gpt_clients import gpt_client
from pack.modules.internal.tasks.process_file import process_file
from pack.modules.internal.tasks.summarize_special_file import summarize_special_file
from pack.modules.internal.helpers.file_processor import FileProcessor
from pack.modules.internal.theme.theme_functions import print_t


def main(monk_args: argparse.Namespace = None):
    print_t("Monkey Time!", "start")

    # Check environment settings for the automation
    automation_env_checks()

    # Load the configuration of the specified monkey or the default one if not specified
    M = load_monkey_config(monk_args.monkey or None)

    # Summarize the special file
    special_file_summary = summarize_special_file(M)
    print_t("Special file summarized successfully!", 'success')
    print_t(f"Summary:{os.linesep}```{special_file_summary}```", 'file')

    # Create an instance of the FileProcessor class
    fp = FileProcessor()

    # Write list of valid files to files-to-process.txt
    # file list defaults to fp.get_filtered_files()
    fp.write_files_to_process()

    # Process the files one by one, removing them from the list as they are processed
    while True:
        # Select a file from the list and remove it from the saved list
        selected_file = fp.select_and_remove_file()

        # Check if the selected_file is None, indicating the list is empty
        if selected_file is None:
            print_t("All files have been processed.", 'done')
            break

        # Check if the file is readable before processing
        if os.access(selected_file, os.R_OK):
            process_file(selected_file, special_file_summary, M.MAIN_PROMPT, M.MAIN_MODEL, gpt_client)
        else:
            print_t(f"Unable to read the file {selected_file}. Skipped.", 'warning')
