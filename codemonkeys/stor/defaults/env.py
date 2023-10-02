import os
from dataclasses import dataclass

from codemonkeys.config.env import Env as CMEnv


@dataclass
class Env(CMEnv):
    """
    The Env class provides easy dot notation access to .env vars.

    DO NOT MODIFY the section between [DEFINE_ENV_PROPS_START] and [DEFINE_ENV_PROPS_END].
    This section is automatically re-generated each time you run a `monk` command.
    """

    # [DEFINE_ENV_PROPS_START]
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')
    CUSTOM_PROP: str = os.getenv('CUSTOM_PROP')
    # [DEFINE_ENV_PROPS_END]