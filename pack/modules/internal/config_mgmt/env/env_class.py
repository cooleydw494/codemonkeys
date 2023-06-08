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

from dotenv import load_dotenv

load_dotenv()

""" FRAMEWORK_ENV_PROPS_LIST - DO NOT MODIFY
A List tracking the framework's env props. This is currently unused, but could be useful. """
# [DEFINE_FRAMEWORK_ENV_PROPS_LIST_START]
required_env_props = ["OPENAI_API_KEY", "DEFAULT_MONKEY", "CUSTOM_PROP"]
# [DEFINE_FRAMEWORK_ENV_PROPS_LIST_END]

@dataclass
class ENV:

    """ FRAMEWORK_ENV_PROPS - DO NOT MODIFY
    Definitions of the framework's env props. These are used to generate the ENV class. """
    # [DEFINE_FRAMEWORK_ENV_PROPS_START]
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', 'THIS-ONES-ON-YOU')
    DEFAULT_MONKEY: str = os.getenv('DEFAULT_MONKEY', 'default')
    CUSTOM_PROP: str = os.getenv('CUSTOM_PROP', 'custom_value')

    # [DEFINE_FRAMEWORK_ENV_PROPS_END]

    """ GENERATED ENV PROPERTIES - DO NOT MODIFY
    Any other properties defined in your .env will be generated and written here on each run of `monk`,
    enabling full, easy IDE support for any custom .env values. """
    # [DEFINE_CUSTOM_AND_MONKEY_CONFIG_OVERRIDE_PROPS_START]

    # [DEFINE_CUSTOM_AND_MONKEY_CONFIG_OVERRIDE_PROPS_END]
