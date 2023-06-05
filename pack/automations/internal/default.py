import os
import sys

from pack.modules.custom.process_file import process_file
from pack.modules.custom.summarize_special_file import summarize_special_file
from pack.modules.custom.theme.theme_functions import print_t
from pack.modules.internal.cm_config_mgmt.environment_checks import automation_env_checks
from pack.modules.internal.cm_config_mgmt.load_monkey_config import load_monkey_config
from pack.modules.internal.gpt.get_gpt_client import instantiate_gpt_models


def main(args):
    print_t("Monkey Time!", "start")

    automation_env_checks()
    M = load_monkey_config(args.monkey or None)

    # Instantiate necessary GPT models
    gpt_models = instantiate_gpt_models()

    def gpt_client(model_name):
        return gpt_models.get(model_name)

    # Check if the special file exists
    if not os.path.isfile(M.SPECIAL_FILE):
        print_t(f"Special file '{M.SPECIAL_FILE}' not found.", "error")
        sys.exit(1)

    # Summarize the special file
    special_file_summary = summarize_special_file(M.SPECIAL_FILE, M.SUMMARY_MODEL,
                                                  M.SUMMARY_PROMPT, gpt_client)
    print_t("Special file summarized successfully!", 'success')
    print_t(f"Summary:{os.linesep}{special_file_summary}", 'file')

    # Iterate over each file in the work_path
    for root, dirs, files in os.walk(M.ENV.WORK_PATH):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(file_path, special_file_summary,
                         M.MAIN_PROMPT, M.MAIN_MODEL, gpt_client)


if __name__ == '__main__':
    main()
