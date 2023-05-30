import os
import sys

import Levenshtein
import yaml

from definitions import STORAGE_INTERNAL_PATH, MONKEYS_PATH
from pack.modules.custom.theme.theme_functions import print_t


def load_monkey_config(monkey_name):
    monkey_file = os.path.join(MONKEYS_PATH, monkey_name, f'{monkey_name}.yaml')

    # Check if the monkey configuration file exists
    if not os.path.isfile(monkey_file):
        print_t(f"Monkey config file '{monkey_name}.yaml' not found.", "error")
        return None

    # Load the monkey configuration variables
    try:
        with open(monkey_file, 'r') as f:
            monkey_config = yaml.safe_load(f)
    except Exception as e:
        print_t(f"Failed to load monkey config from file: '{monkey_name}'. Error: {str(e)}", "error")
        return None

    return monkey_config


def get_monkey_config_defaults(short=False):
    if short:
        filename = 'monkey-config-defaults-short.yaml'
    else:
        filename = 'monkey-config-defaults.yaml'
    monkey_config_defaults_files = os.path.join(STORAGE_INTERNAL_PATH, 'defaults', filename)
    try:
        with open(monkey_config_defaults_files, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print_t(f"Error: Monkey configuration defaults file not found at '{monkey_config_defaults_files}'.", 'error')
        sys.exit(1)
    except yaml.YAMLError:
        print_t(f"Error: Monkey configuration defaults file at '{monkey_config_defaults_files}' is invalid.", 'error')
        sys.exit(1)


def select_next_file():
    input_file = os.path.join(STORAGE_INTERNAL_PATH, "files-to-process.txt")

    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Get the next file and remove the line number
    next_file = lines[0].split('. ', 1)[1].strip()

    # Write the remaining lines back to the file
    with open(input_file, 'w') as file:
        file.writelines(lines[1:])

    # Output the saved file path
    return next_file


def levenshtein_distance(str1, str2):
    # determine if string1 or string2 fully contains the other and if so print(0) to emulate a match
    if str1 in str2 or str2 in str1:
        return 0
    return Levenshtein.distance(str1, str2)
