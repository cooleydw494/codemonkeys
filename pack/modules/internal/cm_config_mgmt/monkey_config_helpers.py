import os
import sys

import yaml

from definitions import STORAGE_DEFAULTS_PATH
from pack.modules.custom.theme.theme_functions import print_t


def get_monkey_config_defaults(short=False):
    if short:
        filename = 'monkey-config-defaults-short.yaml'
    else:
        filename = 'monkey-config-defaults.yaml'
    monkey_config_defaults_files = os.path.join(STORAGE_DEFAULTS_PATH, filename)
    try:
        with open(monkey_config_defaults_files, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print_t(f"Error: Monkey config defaults file not found at '{monkey_config_defaults_files}'.", 'error')
        sys.exit(1)
    except yaml.YAMLError:
        print_t(f"Error: Monkey config defaults file at '{monkey_config_defaults_files}' is invalid.", 'error')
        sys.exit(1)