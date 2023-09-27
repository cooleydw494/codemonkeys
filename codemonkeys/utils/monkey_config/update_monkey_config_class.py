import importlib

from codemonkeys.config.yaml_helpers import get_monkey_config_defaults
from codemonkeys.defs import MONKEY_CONFIG_CLASS_PATH, nl
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.utils.monkey_config.monkey_config_validations import is_path_key

try:
    # import this in a non-standard way to allow force-reloading the module
    import config.framework.monkey_config
    MonkeyConfig = config.framework.monkey_config.MonkeyConfig
except ImportError as e:
    print_t('Could not import user MonkeyConfig class from config.framework.monkey_config. Using default '
            'MonkeyConfig class.', 'warning')
    print_t(str(e))
    from codemonkeys.config.monkey_config import MonkeyConfig


def force_reload_monkey_config_class() -> None:
    """ Force re-import MonkeyConfig because it may have been rewritten after initial import. """
    try:
        importlib.reload(config.framework.monkey_config)
    except ImportError:
        print_t('Could not import user MonkeyConfig class from config.framework.monkey_config. Using default '
                'MonkeyConfig class.', 'warning')


def update_monkey_config_class() -> None:
    """
    This function dynamically updates the published MonkeyConfig declarations/validations to be up-to-date with
    monkey-config-defaults.yaml.

    :raises Exception: If any required markers are not found in the class file.
    :raises ValueError: If the config contains a List with non-string items.
    """
    config_defaults = get_monkey_config_defaults()

    formatted_properties = [
        "    " + key + ": Optional[" + type(config_defaults[key]).__name__ + "] = field(default=None)" for key in config_defaults.keys()]

    # Format the validations
    formatted_validations = []
    for key, value in config_defaults.items():
        if isinstance(value, bool):
            formatted_validations.append(f"        self.{key} = validate_bool('{key}', self.{key})")
        elif isinstance(value, int):
            formatted_validations.append(f"        self.{key} = validate_int('{key}', self.{key})")
        elif isinstance(value, float):
            formatted_validations.append(f"        self.{key} = validate_float('{key}', self.{key})")
        elif is_path_key(key):
            formatted_validations.append(f"        self.{key} = validate_path('{key}', self.{key})")
        elif isinstance(value, str):
            formatted_validations.append(f"        self.{key} = validate_str('{key}', self.{key})")
        elif isinstance(value, list):
            if all(isinstance(item, str) for item in value):
                formatted_validations.append(f"        self.{key} = validate_list_str('{key}', self.{key})")
            else:
                raise ValueError(f"{key} contains non-string items")

    import re

    # Load the MonkeyConfig class
    with open(MONKEY_CONFIG_CLASS_PATH, 'r') as class_file:
        class_lines = class_file.readlines()

    props_start_index = props_end_index = validations_start_index = validations_end_index = None

    # Regular expressions for the markers
    props_start_re = re.compile(r'\[\s*MONKEY_CONFIG_PROPS_START\s*\]')
    props_end_re = re.compile(r'\[\s*MONKEY_CONFIG_PROPS_END\s*\]')
    validations_start_re = re.compile(r'\[\s*MONKEY_CONFIG_VALIDATIONS_START\s*\]')
    validations_end_re = re.compile(r'\[\s*MONKEY_CONFIG_VALIDATIONS_END\s*\]')

    for i, line in enumerate(class_lines):
        if props_start_re.search(line):
            props_start_index = i + 1
        elif props_end_re.search(line):
            props_end_index = i
        elif validations_start_re.search(line):
            validations_start_index = i + 1
        elif validations_end_re.search(line):
            validations_end_index = i

    if None in [props_start_index, props_end_index, validations_start_index, validations_end_index]:
        raise Exception("Couldn't find all markers in the class file.")

    # Add newlines to the formatted properties and validations
    formatted_properties = [p + nl for p in formatted_properties]
    formatted_validations = [v + nl for v in formatted_validations]

    # Import types so that IDE optimization of imports removal gets fixed on each generation
    prop_type_imports = [
        f"    from types import NoneType{nl}",
        f"    from typing import Optional{nl}{nl}",
        f"    from ruamel.yaml.scalarfloat import ScalarFloat{nl}",
        f"    from dataclasses import field{nl}"
    ]

    validations_imports = [
        f"        from codemonkeys.utils.monkey_config.monkey_config_validations import validate_str, "
        f"validate_bool, validate_int, validate_float, validate_path, validate_list_str{nl}"
    ]

    # Replace the sections
    new_class_lines = class_lines[:props_start_index] + \
                      prop_type_imports + \
                      formatted_properties + \
                      class_lines[props_end_index:validations_start_index] + \
                      validations_imports + \
                      formatted_validations + \
                      class_lines[validations_end_index:]

    # Write the updated MonkeyConfig class
    with open(MONKEY_CONFIG_CLASS_PATH, 'w') as class_file:
        class_file.write(''.join(new_class_lines))  # join the lines without adding extra newlines

    force_reload_monkey_config_class()
