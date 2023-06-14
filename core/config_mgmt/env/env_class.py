"""==========================================================================================***
***==  MONKEY MANIFEST  =====================================================================***
***
***    The Monkey Manifest houses centralized configuration of automation profiles (monkeys).
***
***    Undefined props will default based on `stor/core/defaults/monkey-config_mgmt-defaults.yaml`.
***
***=========================================================================================="""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

""" FRAMEWORK_ENV_PROPS_LIST - DO NOT MODIFY
A List tracking the core's env props. This is currently unused, but could be useful. """
# [DEFINE_FRAMEWORK_ENV_PROPS_LIST_START]
required_env_props = ["OPENAI_API_KEY", "CUSTOM_PROP"]
# [DEFINE_FRAMEWORK_ENV_PROPS_LIST_END]

@dataclass
class ENV:
    """ FRAMEWORK_ENV_PROPS - DO NOT MODIFY
    Definitions of the core's env props. These are used to generate the ENV class. """
    # [DEFINE_FRAMEWORK_ENV_PROPS_START]
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', 'THIS-ONES-ON-YOU')
    CUSTOM_PROP: str = os.getenv('CUSTOM_PROP', 'custom_value')

    # [DEFINE_FRAMEWORK_ENV_PROPS_END]

    """ GENERATED ENV PROPERTIES - DO NOT MODIFY
    Any other properties defined in your .env will be generated and written here on each run of `monk`,
    enabling full, easy IDE support for any custom .env values. """
    # [DEFINE_CUSTOM_ENV_PROPS_START]

    # [DEFINE_CUSTOM_ENV_PROPS_END]
