"""==================================================================================================================***
***==  MONKEY MANIFEST  =============================================================================================***
***                                                                                                                  ***
***    The Monkey Manifest houses centralized configuration of automation profiles (monkeys).                        ***
***                                                                                                                  ***
***    Undefined props will default based on `storage/internal/defaults/monkey-config-defaults.yaml`.                ***
***    Monkey props defined in your .env will override the framework defaults.                                       ***
***                                                                                                                  ***
***=================================================================================================================="""

import os
import re
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

# required env props list (must match the class definitions below)
required_env_props = ["DEFAULT_MONKEY", "WORK_PATH", "FILE_TYPES_INCLUDED", "FILEPATH_MATCH_EXCLUDED",
                      "FILE_SELECT_MAX_TOKENS", "OPENAI_API_KEY", "TEMPERATURE"]

ENV_PATTERN = re.compile(r"# \[DEFINE_GENERATED_START\]\n(.*)\n# \[DEFINE_GENERATED_END\]", re.DOTALL)
ENV_DEFINITION_TEMPLATE = "    {var_name}: {var_type} = os.getenv('{var_name}')"


@dataclass
class ENV:
    # REQUIRED ENV PROP class definitions (must match the required env props list above)
    DEFAULT_MONKEY: str = os.getenv('DEFAULT_MONKEY', 'default')
    WORK_PATH: str = os.getenv('WORK_PATH')
    FILE_TYPES_INCLUDED: str = os.getenv('FILE_TYPES_INCLUDED')
    FILEPATH_MATCH_EXCLUDED: str = os.getenv('FILEPATH_MATCH_EXCLUDED')
    FILE_SELECT_MAX_TOKENS: int = int(os.getenv('FILE_SELECT_MAX_TOKENS', 4000))
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')
    TEMPERATURE: float = float(os.getenv('TEMPERATURE', 1))

    """
    GENERATED ENV PROPERTIES - DO NOT MODIFY
    
    Any other properties defined in your .env will be generated and written here on each run of `monk`,
    enabling full, easy IDE support for any custom .env values.
    """
    # [DEFINE_GENERATED_START]

    # [DEFINE_GENERATED_END]
