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


#  TODO (monk)
#   - Add a way to run a script with a flag that will run it in a new terminal tab
#   - Add a monk sub-command that allows the user to create or open a new version of an existing X after backing up old
#   - Add a monk sub-command that allows the user to create a new X from a template

#  TODO (organization)
#   - configs become subdirs of monkeys dir, and the monkey-manifest should be a file in the root directory
#     These directories will store existing configs, enabling the new/backup functionality above for monkey configs.
#     I had an idea related to internal/customizable but idk. Keep thinking, this is fertile ground.
