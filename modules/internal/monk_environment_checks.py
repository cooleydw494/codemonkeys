import os
import sys

from termcolor import colored
from definitions import ROOT_DIR_NAME


def monk_environment_checks():
    version = sys.version_info[0]
    python_command = f"python{version}"
    print(f"🐵 Running environment checks for {python_command}. If you expected another version, look into the way "
          f"you're managing python versions. The `monk` script is added to your PATH in setup.py")

    if version < 3:
        print(colored("⚠️ It appears you're running Python 2. Please use Python 3 with CodeMonkeys.", 'red'))
        exit(1)
    if not os.path.exists(os.path.join(sys.prefix, 'lib', 'python3.8', 'site-packages', f"{ROOT_DIR_NAME}.pth")):
        print(colored("⚠️  CodeMonkeys must be installed as a source package. Run `setup.py`.", 'red'))
        exit(1)