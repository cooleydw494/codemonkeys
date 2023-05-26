import sys

from pack.modules.custom.theme.theme_functions import print_t


def environment_checks():
    version = sys.version_info[0]

    # VERBOSE
    # python_version = f"python{version}"
    # print_t(f"Running environment checks for {python_version}.")

    if version < 3:
        print_t("It appears you're running Python 2. Please use Python 3.", 'error')
        sys.exit(1)
