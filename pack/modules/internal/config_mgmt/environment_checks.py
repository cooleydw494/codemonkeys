import sys

import openai

from pack.modules.internal.config_mgmt.env_class import ENV
from pack.modules.internal.theme.theme_functions import print_t

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
    except ValueError as error:
        print_t(f"{error}", "error")
        sys.exit(1)
