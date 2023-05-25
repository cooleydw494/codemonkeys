import subprocess

from termcolor import colored  # *DO NOT* import printc or any other framework modules in this file

"""
IMPORTANT! PLEASE READ

This module is imported to definitions.py to set a reliable, globally-available PYTHON_COMMAND and PIP_COMMAND.

We cannot import definitions.py or any project modules that use it here, or we will get a circular import error.
Although we could import project modules that don't use definitions.py, it is better to avoid this for maintenance.
"""

# Lists of python and pip commands to be checked
python_commands = ["python3", "python3.11", "python3.10", "python3.9", "python3.8", "python3.7", "python3.6", "python"]
pip_commands = ["pip3", "pip"]


def get_python_command():
    # Loop over the python_commands list and return the first valid command
    for cmd in python_commands:
        if test_command(cmd):
            return cmd
    print(colored("No valid python command is available. Please add one of these to your path, "
                  "or set the PYTHON_COMMAND manually in definitions.py", 'error'))


def get_pip_command():
    # Loop over the pip_commands list and return the first valid command
    for cmd in pip_commands:
        if test_command(cmd):
            return cmd
    print(colored("No valid pip command is available. Please add one of these to your path, "
                  "or set the PIP_COMMAND manually in definitions.py", 'error'))


# noinspection PyBroadException
def test_command(command):
    try:
        # Use --version flag to check if a command is present
        # It should throw an Exception if it isn't
        output = subprocess.check_output([command, "--version"])
        return True
    except Exception:
        return False
