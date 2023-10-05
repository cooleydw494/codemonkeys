import importlib
import re

from codemonkeys.config.yaml_helpers import get_monkey_config_defaults
from codemonkeys.defs import MONKEY_CONFIG_CLASS_PATH, nl
from codemonkeys.utils.monk.theme_functions import print_t

try:
    # import this in a non-standard way to allow force-reloading the module
    import config.framework.monkey_config
    MonkeyConfig = config.framework.monkey_config.MonkeyConfig
except ImportError as e:
    print_t('Failed to import user MonkeyConfig from config.framework.monkey_config. Using default '
            'MonkeyConfig class.', 'warning')
    print_t(str(e))
    from codemonkeys.config.monkey_config import MonkeyConfig


def force_reload_monkey_config_class() -> None:
    """ Force re-import MonkeyConfig because it may have been rewritten after initial import. """
    try:
        importlib.reload(config.framework.monkey_config)
    except ImportError:
        print_t('Failed to re-import user MonkeyConfig from config.framework.monkey_config. Using default '
                'MonkeyConfig class.', 'warning')


def update_monkey_config_class() -> None:
    config_defaults = get_monkey_config_defaults()

    formatted_properties = [
        "    " + key + ": Optional[" + type(config_defaults[key]).__name__ + "] = field(default=None)" for key in
        config_defaults.keys()]

    # Load the MonkeyConfig class
    with open(MONKEY_CONFIG_CLASS_PATH, 'r') as class_file:
        existing_contents = class_file.readlines()

    props_start_index = props_end_index = None

    # Regular expressions for the markers
    props_start_re = re.compile(r'\[\s*MONKEY_CONFIG_PROPS_START\s*\]')
    props_end_re = re.compile(r'\[\s*MONKEY_CONFIG_PROPS_END\s*\]')

    for i, line in enumerate(existing_contents):
        if props_start_re.search(line):
            props_start_index = i + 1
        elif props_end_re.search(line):
            props_end_index = i

    if None in [props_start_index, props_end_index]:
        raise Exception("Couldn't find all markers in the class file.")

    # Add newlines to the formatted properties
    formatted_properties = [p + nl for p in formatted_properties]

    # Import types so that IDE optimization of imports removal gets fixed on each generation
    prop_type_imports = [
        f"    from types import NoneType{nl}",
        f"    from typing import Optional{nl}{nl}",
        f"    from dataclasses import field{nl}"
    ]

    # Put it back together with the generated properties
    new_class_lines = (existing_contents[:props_start_index]
                       + prop_type_imports
                       + formatted_properties
                       + existing_contents[props_end_index:])

    # Write the updated MonkeyConfig class
    with open(MONKEY_CONFIG_CLASS_PATH, 'w') as class_file:
        class_file.write(''.join(new_class_lines))  # join the lines without adding extra newlines

    force_reload_monkey_config_class()
