import sys

import openai

from defs import import_env_class
from codemonkeys.utils.monk.theme_functions import print_t

ENV = import_env_class()
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
