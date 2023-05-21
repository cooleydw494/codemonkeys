import os
import sys

from termcolor import colored
from definitions import ROOT_DIR_NAME


def monk_environment_checks():
    if sys.version_info[0] < 3:
        print(colored("⚠️ It appears you're running Python 2. Please use Python 3 with CodeMonkeys.", 'red'))
        exit(1)
    if not os.path.exists(os.path.join(sys.prefix, 'lib', 'python3.8', 'site-packages', f"{ROOT_DIR_NAME}.pth")):
        if not os.path.exists(os.path.join(sys.prefix, 'lib', 'python3.7', 'site-packages', f"{ROOT_DIR_NAME}.pth")):
            if not os.path.exists(os.path.join(sys.prefix, 'lib', 'python3.6', 'site-packages', f"{ROOT_DIR_NAME}.pth")):
                if not os.path.exists(
                        os.path.join(sys.prefix, 'lib', 'python3.5', 'site-packages', f"{ROOT_DIR_NAME}.pth")):
                    if not os.path.exists(
                            os.path.join(sys.prefix, 'lib', 'python3', 'site-packages', f"{ROOT_DIR_NAME}.pth")):
                        print(colored("⚠️ CodeMonkeys must be installed as a source package. Run `setup.py`.", 'red'))
                        exit(1)
