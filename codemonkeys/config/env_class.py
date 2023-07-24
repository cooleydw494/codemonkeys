import os
from dataclasses import dataclass

from dotenv import load_dotenv

from codemonkeys.config.theme import light_mode_enabled, max_terminal_width, verbose_logs_enabled, keywords, text_themes
from codemonkeys.defs import ROOT_PATH

load_dotenv(os.path.join(ROOT_PATH, '.env'))

""" FRAMEWORK_ENV_PROPS_LIST - DO NOT MODIFY
A List tracking the source's env props. This is currently unused, but could be useful. """
# [DEFINE_FRAMEWORK_ENV_PROPS_LIST_START]
required_env_props = []


# [DEFINE_FRAMEWORK_ENV_PROPS_LIST_END]

@dataclass
class Env:
    _instance = None

    """ FRAMEWORK_ENV_PROPS - DO NOT MODIFY
    Definitions of the source's env props. These are used to generate the Env class. """
    # [DEFINE_FRAMEWORK_ENV_PROPS_START]

    # [DEFINE_FRAMEWORK_ENV_PROPS_END]

    """ GENERATED ENV PROPERTIES - DO NOT MODIFY
    Any other properties defined in your .env will be generated and written here on each run of `monk`,
    enabling full, easy IDE support for any custom .env values. """
    # [DEFINE_CUSTOM_ENV_PROPS_START]
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')

    # [DEFINE_CUSTOM_ENV_PROPS_END]

    """ THEME - DO NOT MODIFY
     This should eventually work another way, but for now it's convenient to have it here. """
    light_mode_enabled = light_mode_enabled
    max_terminal_width = max_terminal_width
    verbose_logs_enabled = verbose_logs_enabled
    keywords = (lambda words: sorted(words, key=len, reverse=True))(keywords)
    text_themes = text_themes

    @classmethod
    def get(cls):
        if Env._instance is None:
            Env._instance = Env()

        return Env._instance
