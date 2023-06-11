import argparse
import os

from definitions import nl
from pack.modules.core.config_mgmt.environment_checks import automation_env_checks
from pack.modules.core.config_mgmt.monkey_config.load_monkey_config import load_monkey_config
from pack.modules.core.tasks.process_file import process_file
from pack.modules.core.tasks.summarize_special_file import summarize_special_file
from pack.modules.core.helpers.file_list_manager import FileListManager
from pack.modules.core.theme.theme_functions import print_t


def main(monk_args: argparse.Namespace = None):

    automation_env_checks()
    print_t("Monkey Time!", "start")
    m = load_monkey_config(monk_args.monkey or None)

    fp = FileListManager(m)
    fp.write_files_to_process()

    special_file_summary = summarize_special_file(m)

    while True:
        selected_file = fp.select_and_remove_file()

        if selected_file is None:
            print_t("All files have been processed.", 'done')
            break

        if os.access(selected_file, os.R_OK):  # is readable
            process_file(selected_file, special_file_summary, m)
        else:
            print_t(f"Unable to read the file:{nl}{selected_file}{nl}Skipped.", 'warning')
