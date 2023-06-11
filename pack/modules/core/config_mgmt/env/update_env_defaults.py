import os
import re

from definitions import STOR_DEFAULTS_PATH, nl
from pack.modules.core.config_mgmt.yaml_helpers import get_monkey_config_defaults


def update_env_defaults():
    config = get_monkey_config_defaults()

    # Format the properties
    formatted_properties = nl.join("#  " + key + ": " + str(value) for key, value in config.items())

    # Load the .env.default file
    ENV_DEFAULTS_PATH = os.path.join(STOR_DEFAULTS_PATH, '.env.default')
    with open(ENV_DEFAULTS_PATH, 'r') as env_file:
        env_content = env_file.read()

    # Replace the section between the markers
    updated_content = re.sub(
        r"(#  \[MONKEY_CONFIG_DEFAULT_OVERRIDES_START\]\n)(.*)(\n#  \[MONKEY_CONFIG_DEFAULT_OVERRIDES_END\])",
        r"\1" + formatted_properties + r"\3",
        env_content,
        flags=re.DOTALL  # Allows . to match newline
    )

    # Write the updated .env.default file
    with open(ENV_DEFAULTS_PATH, 'w') as env_file:
        env_file.write(updated_content)