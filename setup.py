import os
import platform
import shutil
import subprocess
import sys

from definitions import PIP_COMMAND, PYTHON_COMMAND
from pack.modules.custom.theme.theme_functions import printc
from pack.modules.internal.utils.environment_checks import environment_checks

printc("Initiating the setup process...", "start")

current_shell_rc = None
environment_checks()

# Get the OS type
os_type = platform.system().lower()
printc(f"Detected {os_type.capitalize()} as your operating system...", "info")

current_shell = os.environ['SHELL']
curren_shell_rc = None
if current_shell.endswith("bash"):
    current_shell_rc = "~/.bashrc"
elif current_shell.endswith("zsh"):
    current_shell_rc = "~/.zshrc"
elif current_shell.endswith("fish"):
    current_shell_rc = "~/.config/fish/config.fish"
if current_shell:
    printc(f"Detected {current_shell} as your current shell...", "info")
else:
    printc("Could not detect your current shell. You may need to take some manual steps throughout setup.", "error")

# Install required python modules from requirements.txt
printc("Installing the required Python modules from the requirements.txt file...", "loading")
subprocess.call(f'{PIP_COMMAND} install -r requirements.txt', shell=True)

# if the .env doesn't already exist, copy it from storage/.env.template and print some helpful feedback.
if not os.path.exists('.env'):
    printc("No .env file found. Creating it from the template...", "file")
    subprocess.call('cp storage/.env.template .env', shell=True)
else:
    printc("The .env file already exists. No changes were made to it.", "file")

# Make the monk script executable
printc("Making the monk script executable...", "monkey")
if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
    subprocess.call('chmod +x monk', shell=True)
elif os_type == "windows":  # If OS is Windows
    printc("On Windows, Python scripts are typically run directly with the Python interpreter, so when you "
           "see something like `monk [script-name]` in the docs, so should instead do something like:"
           "`python monk.py [script-name]` or `py monk.py [script-name]`.", "tip")

if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
    alias_exists = subprocess.call('alias | grep -q "^alias monk="', shell=True)
    if alias_exists == 1:
        printc("The 'monk' alias is already present.", "link")
    else:
        printc("Adding 'monk' alias... ", "link")

        if not current_shell_rc:
            printc("Could not determine current shell. Please add the 'monk=./monk' alias manually to be "
                   "able to use the monk command more easily.", "important")
            sys.exit(1)
        subprocess.call(f'echo "alias monk=\'{PYTHON_COMMAND} ./monk\'" >> {current_shell_rc}', shell=True)
        printc("The 'monk' alias was added.", "success")
        printc("You can now use the 'monk' command in this directory to run scripts located in the 'scripts' "
               "directory.", "success")
elif os_type.startswith("win"):  # If OS is Windows
    if os.path.exists("monk.py"):
        printc("The 'monk.py' command is already present.", "success")
    else:
        printc("Renaming 'monk' to 'monk.py' for Windows compatibility... ", "link")
        shutil.move("monk", "monk.py")
        printc("The 'monk' command was renamed to 'monk.py'. Run it using 'python monk.py'.", "success")
else:
    printc("OS not detected. Please add 'monk' to your PATH manually to use the `monk` command.", "warning")

# Use monk to generate the default configurations
printc("Generating default monkey configurations...", 'config')
if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
    subprocess.call(f'{PYTHON_COMMAND} ./monk generate-monkeys', shell=True)
elif os_type == "windows":  # If OS is Windows
    subprocess.call('python monk.py generate-monkeys', shell=True)
printc("Monkey configurations are based on the 'monkey-manifest.yaml' file. Individual configs will be "
       "generated in the 'monkeys' directory.", "info")
printc("After making changes, use 'monk generate-monkeys' to apply them.",
       "tip")
printc("Thanks for using CodeMonkeys!", 'monkey')
if current_shell_rc is not None:
    printc(f'You still need to source your {current_shell_rc} to use the `monk` command (if initial setup).', 'warning')
    printc(f"Run `source {current_shell_rc}`", 'tip')
elif os_type == "darwin" or os_type == "linux":
    printc("Shell undetermined. Please source your shell profile to enable the 'monk' command", 'warning')

printc('CodeMonkeys setup complete', 'done')
