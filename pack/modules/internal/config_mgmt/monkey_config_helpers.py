import os
import sys

import yaml

from definitions import STORAGE_DEFAULTS_PATH
from pack.modules.internal.theme.theme_functions import print_t


def get_monkey_config_defaults(yaml_override=None):
    # yaml_override is to support ruamel (TODO: remove one of the yaml libraries and use the other always)
    if yaml_override is not None:
        yaml_instance = yaml_override
    else:
        yaml_instance = yaml
    filename = 'monkey-config-defaults.yaml'
    monkey_config_defaults_file = os.path.join(STORAGE_DEFAULTS_PATH, filename)
    try:
        with open(monkey_config_defaults_file, 'r') as f:
            return yaml_instance.safe_load(f)
    except FileNotFoundError:
        print_t(f"Error: Monkey config defaults file not found at '{monkey_config_defaults_file}'.", 'error')
        sys.exit(1)
    except yaml_instance.YAMLError:
        print_t(f"Error: Monkey config defaults file at '{monkey_config_defaults_file}' is invalid.", 'error')
        sys.exit(1)
