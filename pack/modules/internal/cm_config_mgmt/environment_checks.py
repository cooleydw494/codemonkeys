import sys

import openai

from pack.modules.custom.theme.theme_functions import print_t
from pack.modules.internal.cm_config_mgmt.env_class import ENV

ENV = ENV()


def monk_env_checks():
    version = sys.version_info[0]

    if version < 3:
        print_t("It appears you're running Python 2. Please use Python 3.", 'error')
        sys.exit(1)


def automation_env_checks():
    try:
        openai.api_key = ENV.OPENAI_API_KEY
        if openai.api_key is None:
            raise ValueError("OPENAI_API_KEY is not set.")
        work_path = ENV.WORK_PATH
        if work_path is None:
            raise ValueError("WORK_PATH is not set.")
    except ValueError as error:
        print_t(f"{error}", "error")
        sys.exit(1)
