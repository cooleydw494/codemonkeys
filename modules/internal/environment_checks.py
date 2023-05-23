import sys

from termcolor import colored


def environment_checks():
    version = sys.version_info[0]

    # VERBOSE
    # python_version = f"python{version}"
    # print(f"🐵 Running environment checks for {python_version}.")

    if version < 3:
        print(colored("⚠️ It appears you're running Python 2. Please use Python 3.", 'red'))
        exit(1)

    # TODO - find a way to check that setup has been run in the new paradigm

    # PSEUDO_PACKAGE
    # if str(sys.path).find(os.path.join(PSEUDO_PACKAGE_PATH)) == -1:
    #     print(colored("⚠️  CodeMonkeys must be installed into `sys.path`. Run `setup.py`.", 'red'))
    #     exit(1)
