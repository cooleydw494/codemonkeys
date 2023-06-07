import argparse
import os
import sys

from pack.modules.internal.config_mgmt.environment_checks import automation_env_checks
from pack.modules.internal.config_mgmt.load_monkey_config import load_monkey_config
from pack.modules.internal.gpt.gpt_clients import gpt_client
from pack.modules.internal.tasks.process_file import process_file
from pack.modules.internal.tasks.summarize_special_file import summarize_special_file
from pack.modules.internal.theme.theme_functions import print_t


def main(monk_args: argparse.Namespace = None):
    print_t("Monkey Time!", "start")

    # Check environment settings for the automation
    automation_env_checks()

    # Load the configuration of the specified monkey or the default one if not specified
    M = load_monkey_config(monk_args.monkey or None)

    # Summarize the special file
    special_file_summary = summarize_special_file(M.SPECIAL_FILE_PATH, M.SUMMARY_MODEL, M.SUMMARY_PROMPT, gpt_client)
    print_t("Special file summarized successfully!", 'success')
    print_t(f"Summary:{os.linesep}{special_file_summary}", 'file')

    # Iterate over each file in the work_path
    for root, dirs, files in os.walk(M.WORK_PATH):
        for file in files:
            file_path = os.path.join(root, file)
            # Check if the file is readable before processing
            if os.access(file_path, os.R_OK):
                process_file(file_path, special_file_summary, M.MAIN_PROMPT, M.MAIN_MODEL, gpt_client)
            else:
                print_t(f"Unable to read the file {file_path}. Skipped.", 'warning')
