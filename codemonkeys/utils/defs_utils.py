import os

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
