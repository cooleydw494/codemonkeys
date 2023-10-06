import os
from importlib.util import spec_from_file_location, module_from_spec
from typing import Any

from termcolor import colored

"""
This module is imported to defs and/or cmdefs.
It houses code that can be run without importing other project modules (which would result in circular imports).

NO PROJECT MODULES, CONFIGS, ETC SHOULD BE IMPORTED HERE.
"""


def find_project_root() -> str:
    """
    Find the root directory of the project (i.e., the closest parent directory containing a `.env` file).

    :return: The project root directory path.
    """
    cwd = os.getcwd()
    while cwd != os.path.dirname(cwd):  # Stop when we reach the root directory
        if '.env' in os.listdir(cwd):
            if os.path.exists(os.path.join(cwd, 'config', 'monkeys')):
                return cwd
            else:
                print(colored("You must run `monk` within a CodeMonkeys project", 'red'))
                exit(1)
        cwd = os.path.dirname(cwd)
    print(colored("Could not find project root", 'red'))
    exit(1)


def load_class(entity_path: str, entity_name: str) -> Any:
    """
    Locates Entity class using path/name, loads the module, and returns the class reference for instantiation.
    This logic assumes an entity's class name is the same as the filename/CLI-name, but in CamelCase.

    :param str entity_path: The file path to the Entity class.
    :param str entity_name: The name of the Entity class.
    """
    # Convert entity_name from kebab-case/snake_case to CamelCase
    seperator = '-' if entity_name.find('-') != -1 else '_'
    entity_name_camel_case = ''.join(word.capitalize() for word in entity_name.split(seperator))

    # Normalize path
    entity_path = os.path.normpath(entity_path)

    # Create module spec, load module, and get class
    module_spec = spec_from_file_location(entity_name_camel_case, entity_path)
    module = module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    entity_class = getattr(module, entity_name_camel_case)

    return entity_class
