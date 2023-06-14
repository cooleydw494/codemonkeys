import subprocess

"""
This module is imported to defs.py to set a reliable, globally-available PYTHON_COMMAND and PIP_COMMAND.
"""

# Lists of python and pip commands to be checked
python_commands = ["python3", "python3.11", "python3.10", "python3.9", "python3.8", "python3.7", "python3.6", "python"]
pip_commands = ["pip3", "pip"]


def get_python_command():
    # Loop over the python_commands list and return the first valid command
    for cmd in python_commands:
        if test_command(cmd):
            return cmd
    print("No valid python command is available. Please add one of these to your path, "
          "or set the PYTHON_COMMAND manually in defs.py")


def get_pip_command():
    # Loop over the pip_commands list and return the first valid command
    for cmd in pip_commands:
        if test_command(cmd):
            return cmd
    print("No valid pip command is available. Please add one of these to your path, "
          "or set the PIP_COMMAND manually in defs.py")


# noinspection PyBroadException
def test_command(command):
    try:
        # Use --version flag to check if a command is present
        # It should throw an Exception if it isn't
        output = subprocess.check_output([command, "--version"])
        return True
    except Exception:
        return False
