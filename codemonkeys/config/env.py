import os
from dataclasses import dataclass
from typing import List

from dotenv import load_dotenv

from codemonkeys.defs import ROOT_PATH

load_dotenv(os.path.join(ROOT_PATH or '.', '.env'))

""" FRAMEWORK_ENV_PROPS_LIST - DO NOT MODIFY
A List tracking the source's env props. This is currently unused, but could be useful. """
# [DEFINE_FRAMEWORK_ENV_PROPS_LIST_START]
required_env_props: List = []


# [DEFINE_FRAMEWORK_ENV_PROPS_LIST_END]

@dataclass
class Env:
    """
    The Env class provides easy dot notation access to .env vars.
    """

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

    @classmethod
    def get(cls) -> 'Env':
        """
        Get the instance of the Env class, or create one if it doesn't exist.

        :return: Singleton instance of the Env class
        """
        if Env._instance is None:
            Env._instance = Env()

        return Env._instance
