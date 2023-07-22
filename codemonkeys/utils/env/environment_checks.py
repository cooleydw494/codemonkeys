import sys

import openai

from codemonkeys.utils.monk.theme_functions import print_t


try:
    from config.framework.env_class import Env
except ImportError:
    print_t('Could not import user Env class from config.framework.env_class. Using default Env class.', 'warning')
    from codemonkeys.config.env_class import Env


def monk_env_checks():

    version = sys.version_info[0]

    if version < 3:
        print_t("It appears you're running Python 2. Please use Python 3.", 'error')
        sys.exit(1)


def automation_env_checks():
    try:
        env = Env.get()
        openai.api_key = env.OPENAI_API_KEY
        if openai.api_key is None:
            raise ValueError("OPENAI_API_KEY is not set.")
    except ValueError as error:
        print_t(f"{error}", "error")
        sys.exit(1)
