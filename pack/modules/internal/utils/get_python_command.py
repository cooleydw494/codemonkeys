import subprocess

# IMPORTANT! PLEASE READ
#
# This module is used in the root definitions.py to set PYTHON_COMMAND and PIP_COMMAND. It covers the most common cases
# as a convenience. If you were going to edit this, hard-coding in definitions.py or .env is probably a better idea.
#
# Additionally, we can't import any framework modules here. The ...definitions.py, used throughout the pseudo-package,
# is a symlink of the root definitions.py, so importing framework modules could cause circular imports.
#
# For instance, we can't import modules.personality.custom.visuals.printc. We must use termcolor directly.

from termcolor import colored  # *DO NOT* import printc or any other framework modules in this file


def get_python_command():
    # Test the 'python3' command
    if test_command("python3"):
        return "python3"
    elif test_command("python"):
        return "python"
    else:
        print(colored("Neither python3 nor python command is available. Please add one of these to your path, "
                      "or set the PYTHON_COMMAND manually in definitions.py", 'error'))


def get_pip_command():
    # Test the 'pip3' command
    if test_command("pip3"):
        return "pip3"
    elif test_command("pip"):
        return "pip"
    else:
        print(colored("Neither pip3 nor pip command is available. Please add one of these to your path, "
                      "or set the PIP_COMMAND manually in definitions.py", 'error'))


# noinspection PyBroadException
def test_command(command):
    try:
        # Try to get the python version
        output = subprocess.check_output([command, "--version"])
        return True
    except Exception:
        return False
