import subprocess

from termcolor import colored


# This is used to set PYTHON_COMMAND in definitions.py. It covers the most common cases, as a convenience.
# If you're thinking about editing this, hard-coding in definitions.py is probably a better idea

def get_python_command():
    # Test the 'python3' command
    if test_command("python3"):
        return "python3"
    elif test_command("python"):
        return "python"
    else:
        print(colored("Neither python3 nor python command is available. Please add one of these to your path, "
                      "or set the PYTHON_COMMAND manually in definitions.py", 'red'))


def get_pip_command():
    # Test the 'pip3' command
    if test_command("pip3"):
        return "pip3"
    elif test_command("pip"):
        return "pip"
    else:
        print(colored("Neither pip3 nor pip command is available. Please add one of these to your path, "
                      "or set the PIP_COMMAND manually in definitions.py", 'red'))


# noinspection PyBroadException
def test_command(command):
    try:
        # Try to get the python version
        output = subprocess.check_output([command, "--version"])
        return True
    except Exception:
        return False
