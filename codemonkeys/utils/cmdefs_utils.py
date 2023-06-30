import importlib.util
import os
import subprocess

import Levenshtein
from termcolor import colored

"""
This module is imported to defs and/or cmdefs.
It houses code that can be run without importing other project modules (which would result in circular imports).

NO PROJECT MODULES, CONFIGS, ETC SHOULD BE IMPORTED HERE.
"""

# Lists of python and pip commands to be checked
python_commands = ["python3", "python3.11", "python3.10", "python3.9", "python3.8", "python3.7", "python3.6", "python"]


def get_python_command():
    # Loop over the python_commands list and return the first valid command
    for cmd in python_commands:
        if _test_command(cmd):
            return cmd
    print("No valid python command is available. Please add one of these to your path, "
          "or set the PYTHON_COMMAND manually in defs.py")


def _test_command(command):
    # noinspection PyBroadException
    try:
        # Use --version flag to check if a command is present
        # It should throw an Exception if it isn't
        output = subprocess.check_output([command, "--version"])
        return True
    except Exception:
        return False


def find_project_root():
    """Find the root directory of the project (i.e., the closest parent directory containing a `.env` file)."""
    cwd = os.getcwd()

    while cwd != os.path.dirname(cwd):  # Stop when we reach the root directory
        if '.env' in os.listdir(cwd):
            # check for existence of root/config/monkey-manifest.yaml to verify its a codemonkeys project
            if os.path.exists(os.path.join(cwd, 'config', 'monkey-manifest.yaml')):
                return cwd
            else:
                print(colored("You must run `monk` within a CodeMonkeys project", 'red'))
                exit(1)
        cwd = os.path.dirname(cwd)

    print(colored("Could not find project root", 'red'))
    exit(1)


def import_class_from_path_with_fallback(path, class_name, fallback_class):
    """
    Try to import a class from a Python file at a given path. If the import fails, return a fallback class.

    Args:
    - path (str): The path to the Python file.
    - class_name (str): The name of the class to import.
    - fallback_class (type): The class to use if the import fails.

    Returns:
    - The imported class, or the fallback class if the import fails.
    """
    try:
        spec = importlib.util.spec_from_file_location(class_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, class_name)
    except (ImportError, FileNotFoundError, AttributeError) as e:
        print(colored(f"Could not import {class_name} from {path}", 'red'))
        print(colored(f"Using fallback class {fallback_class.__name__}", 'yellow'))
        print(colored(f"Error: {e}", 'red'))
        return fallback_class


def levenshtein_distance(str1, str2):
    # determine if string1 or string2 fully contains the other and if so print(0) to emulate a match
    if str1 in str2 or str2 in str1:
        return 0
    return Levenshtein.distance(str1, str2)
