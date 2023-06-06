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

from pack.modules.internal.cm_config_mgmt.env_helpers import get_env_prop_type

load_dotenv()

# required env props (must match the class definitions at the bottom of this file)
required_env_props = ["DEFAULT_MONKEY", "WORK_PATH", "FILE_TYPES_INCLUDED", "FILEPATH_MATCH_EXCLUDED",
                      "FILE_SELECT_MAX_TOKENS", "OPENAI_API_KEY", "TEMPERATURE"]

ENV_PATTERN = re.compile(r"# \[DEFINE_GENERATED_START\]\n(.*)\n# \[DEFINE_GENERATED_END\]", re.DOTALL)
ENV_DEFINITION_TEMPLATE = "    {var_name}: {var_type} = os.getenv('{var_name}')"


def update_env_class():
    """
    Updates the env_class.py file to include all environment variables as attributes of the ENV class.
    """
    # Read the current contents of the file
    with open("env_class.py", "r") as f:
        content = f.read()

    # Get all environment variables and generate the corresponding class attribute definitions
    env_definitions = []
    for key, value in os.environ.items():
        if key not in required_env_props:
            env_definitions.append(ENV_DEFINITION_TEMPLATE.format(var_name=key, var_type=get_env_prop_type(value)))

    # Replace placeholder in class definition with generated definitions
    new_content = ENV_PATTERN.sub(
        "# [DEFINE_GENERATED_START]\n" + "\n".join(env_definitions) + "\n# [DEFINE_GENERATED_END]",
        content)

    # Write updated contents
    with open("env_class.py", "w") as f:
        f.write(new_content)


@dataclass
class ENV:
    # REQUIRED ENV PROPERTIES (must match the above list)
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
