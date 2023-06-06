import os
import re

import yaml

from definitions import STORAGE_DEFAULTS_PATH


def update_env_defaults():
    MONKEY_CONFIG_DEFAULTS_PATH = os.path.join(STORAGE_DEFAULTS_PATH, 'monkey-config-defaults.yaml')
    # Load and parse the YAML config
    with open(MONKEY_CONFIG_DEFAULTS_PATH, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)

    # Format the properties
    formatted_properties = "\n".join("#  " + key + ": " + str(value) for key, value in config.items())

    # Load the .env.default file
    ENV_DEFAULTS_PATH = os.path.join(STORAGE_DEFAULTS_PATH, '.env.default')
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
