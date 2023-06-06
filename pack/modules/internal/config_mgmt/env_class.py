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
from dataclasses import dataclass
from typing import List

from dotenv import load_dotenv

load_dotenv()

# [DEFINE_FRAMEWORK_ENV_PROPS_LIST_START]
required_env_props = ["WORK_PATH", "FILE_TYPES_INCLUDED", "FILEPATH_MATCH_EXCLUDED", "FILE_SELECT_MAX_TOKENS", "OPENAI_API_KEY", "TEMPERATURE", "DEFAULT_MONKEY"]
# [DEFINE_FRAMEWORK_ENV_PROPS_LIST_END]

@dataclass
class ENV:
    # [DEFINE_FRAMEWORK_ENV_PROPS_START]
    WORK_PATH: str = os.getenv('WORK_PATH', '~/projects/project-name')
    FILE_TYPES_INCLUDED: List[str] = os.getenv('FILE_TYPES_INCLUDED', '.js,.vue,.php')
    FILEPATH_MATCH_EXCLUDED: List[str] = os.getenv('FILEPATH_MATCH_EXCLUDED', '.config,.md,.git,migrations,vite,webpack,.txt')
    FILE_SELECT_MAX_TOKENS: int = os.getenv('FILE_SELECT_MAX_TOKENS', '4000')
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', 'THIS-ONES-ON-YOU')
    TEMPERATURE: int = os.getenv('TEMPERATURE', '1')
    DEFAULT_MONKEY: str = os.getenv('DEFAULT_MONKEY', '')

    # [DEFINE_FRAMEWORK_ENV_PROPS_END]

    """
    GENERATED ENV PROPERTIES - DO NOT MODIFY
    
    Any other properties defined in your .env will be generated and written here on each run of `monk`,
    enabling full, easy IDE support for any custom .env values.
    """
    # [DEFINE_CUSTOM_AND_MONKEY_CONFIG_OVERRIDE_PROPS_START]
    SOMETHING_NEW: float = os.getenv('SOMETHING_NEW')

    # [DEFINE_CUSTOM_AND_MONKEY_CONFIG_OVERRIDE_PROPS_END]
