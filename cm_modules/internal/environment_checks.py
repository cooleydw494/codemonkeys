import sys

from cm_modules.personality.custom.visuals import printc


def environment_checks():
    version = sys.version_info[0]

    # VERBOSE
    # python_version = f"python{version}"
    # printc(f"Running environment checks for {python_version}.")

    if version < 3:
        printc("It appears you're running Python 2. Please use Python 3.", 'error')
        exit(1)


