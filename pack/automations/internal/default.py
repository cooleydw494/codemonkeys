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

    # Initialize Automation Environment
    automation_env_checks()
    print_t("Monkey Time!", "start")
    m = load_monkey_config(monk_args.monkey or None)

    # Summarize the special file
    special_file_summary = summarize_special_file(m)
    print_t("Special file summarized successfully!", 'success')
    print_t(f"Summary:{os.linesep}```{special_file_summary}```", 'file')

    # Write list of valid files to files-to-process.txt
    # file list defaults to fp.get_filtered_files()
    fp = FileProcessor()
    fp.write_files_to_process()

    # Process files 1-by-1; remove from list as processed
    while True:
        selected_file = fp.select_and_remove_file()

        if selected_file is None:
            print_t("All files have been processed.", 'done')
            break

        if os.access(selected_file, os.R_OK):  # is readable
            process_file(selected_file, m)
        else:
            print_t(f"Unable to read the file {selected_file}. Skipped.", 'warning')
