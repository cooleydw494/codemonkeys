import os
import sys

import yaml

from codemonkeys.defs import MONKEY_CONFIG_DEFAULTS_PATH
from codemonkeys.utils.monk.theme_functions import print_t


def read_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print_t(f"Error: File not found at '{file_path}'.", 'error')
        sys.exit(1)
    except yaml.YAMLError:
        print_t(f"Error: File at '{file_path}' is not a valid YAML file.", 'error')
        sys.exit(1)


def get_monkey_config_defaults():
    monkey_config_defaults_file = os.path.join(MONKEY_CONFIG_DEFAULTS_PATH)
    return read_yaml_file(monkey_config_defaults_file)
