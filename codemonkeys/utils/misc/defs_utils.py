"""
Utility functions for the CodeMonkeys project framework.

This module contains helper functions that are used throughout the CodeMonkeys project to perform
operations such as finding the project root and dynamically loading classes from files.
The functions in this module are designed to be used without the need for importing other project-specific
modules, configurations, etc., to prevent circular imports.
"""

import os
from importlib.util import spec_from_file_location, module_from_spec
from typing import Any

from termcolor import colored


# NO PROJECT MODULES, CONFIGS, ETC SHOULD BE IMPORTED HERE.


def find_project_root() -> str:
    """
    Find the root directory of the project (i.e., the closest parent directory containing a `.env` file).

    This function searches upwards from the current working directory for the .env file that
    signifies the root of a CodeMonkeys project. Once found, it confirms the 'monkeys/monkey.py'
    file exists to ensure it's a valid project root. If neither are found, it terminates execution.

    :return: The project root directory path.
    :rtype: str

    :raises SystemExit: If the CodeMonkeys project root cannot be located or validated.
    """
    cwd = os.getcwd()
    while cwd != os.path.dirname(cwd):  # Stop when we reach the root directory
        if '.env' in os.listdir(cwd):
            if os.path.exists(os.path.join(cwd, 'monkeys', 'monkey.py')):
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

    The function dynamically imports a module based on its file location and extracts the class of the same
    name in CamelCase. It is used for dynamic CLI operation where entities are loaded based on user input.

    :param entity_path: The file path to the Entity class.
    :type entity_path: str
    :param entity_name: The name of the Entity class.
    :type entity_name: str
    :return: A reference to the Entity class.
    :rtype: Any
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
