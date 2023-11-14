import os
from dataclasses import dataclass

from codemonkeys.config.env import Env as CMEnv


@dataclass
class Env(CMEnv):
    """
    The Env class provides easy dot notation access to .env vars.

    This class serves as an interface for accessing environment variables defined
    in the .env file. The Env class inherits from the codemonkeys.config.env.Env
    class and includes all of its properties and methods.

    Each environment variable is defined as a class attribute with type hints,
    providing better IDE support and error-checking. The environment variables
    are loaded using os.getenv and are type-annotated for clarity.

    Attributes:
        OPENAI_API_KEY: A string representing the OpenAI API key.
        CUSTOM_PROP: A string representing a custom property.

    DO NOT MODIFY the section between [DEFINE_ENV_PROPS_START] and [DEFINE_ENV_PROPS_END].
    This section is automatically re-generated each time you run a `monk` command.
    """

    # [DEFINE_ENV_PROPS_START]
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')
    CUSTOM_PROP: str = os.getenv('CUSTOM_PROP')
    # [DEFINE_ENV_PROPS_END]
