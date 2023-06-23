import os
import sys

import yaml
from ruamel.yaml import YAML

from defs import MONKEY_CONFIG_DEFAULTS_PATH
from codemonkeys.utils.monk.theme_functions import print_t


def read_yaml_file(file_path, ruamel=False):
    try:
        with open(file_path, 'r') as file:
            if ruamel:
                ruamel_yaml = get_ruamel_yaml()
                return ruamel_yaml.load(file)
            else:
                return yaml.safe_load(file)
    except FileNotFoundError:
        print_t(f"Error: File not found at '{file_path}'.", 'error')
        sys.exit(1)
    except yaml.YAMLError:
        print_t(f"Error: File at '{file_path}' is not a valid YAML file.", 'error')
        sys.exit(1)


def write_yaml_file(file_path, data, ruamel=False):
    try:
        with open(file_path, 'w') as file:
            if ruamel:
                ruamel_yaml = get_ruamel_yaml()
                ruamel_yaml.dump(data, file)
            else:
                yaml.safe_dump(data, file)
    except Exception as e:
        print_t(f"An error occurred while writing to the file: {str(e)}", 'error')
        sys.exit(1)


def get_ruamel_yaml() -> YAML:
    ruamel_yaml = YAML()
    ruamel_yaml.default_style = "'"
    ruamel_yaml.indent(sequence=4, offset=2)
    return ruamel_yaml


def get_monkey_config_defaults():
    monkey_config_defaults_file = os.path.join(MONKEY_CONFIG_DEFAULTS_PATH)
    return read_yaml_file(monkey_config_defaults_file, ruamel=True)

