import os
from dataclasses import dataclass

from dotenv import load_dotenv

from codemonkeys.defs import ROOT_PATH

load_dotenv(os.path.join(ROOT_PATH or '.', '.env'))


@dataclass
class Env:
    """
    The Env class provides easy dot notation access to .env vars.
    """

    _instance = None

    # GENERATED ENV PROPERTIES - DO NOT MODIFY
    # [DEFINE_ENV_PROPS_START]
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')
    # [DEFINE_ENV_PROPS_END]

    @classmethod
    def get(cls) -> 'Env':
        """
        Get the instance of the Env class, or create one if it doesn't exist.

        :return: Singleton instance of the Env class
        """
        if Env._instance is None:
            Env._instance = Env()

        return Env._instance
