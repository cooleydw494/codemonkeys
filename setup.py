import os
import platform
import subprocess
import sys

from definitions import PIP_COMMAND, PYTHON_COMMAND
from pack.modules.custom.theme.theme_functions import print_t
from pack.modules.internal.cm_config_mgmt.environment_checks import monk_env_checks

print_t("Thanks for using CodeMonkeys!", 'monkey')
print_t("Initiating the setup process...", "start")

current_shell_rc = None
monk_env_checks()

# Get the OS type
os_type = platform.system().lower()
print_t(f"Detected {os_type.capitalize()} as your operating system...", "info")

current_shell = os.environ['SHELL']
curren_shell_rc = None
if current_shell.endswith("bash"):
    current_shell_rc = "~/.bashrc"
elif current_shell.endswith("zsh"):
    current_shell_rc = "~/.zshrc"
elif current_shell.endswith("fish"):
    current_shell_rc = "~/.config/fish/config.fish"
if current_shell:
    print_t(f"Detected {current_shell} as your current shell...", "info")
else:
    print_t("Could not detect your current shell. You may need to take some manual steps throughout setup.", "error")

# Install required python modules from requirements.txt
print_t("Installing the required Python modules from the requirements.txt file...", "loading")
subprocess.call(f'{PIP_COMMAND} install -r requirements.txt', shell=True)

# if the .env doesn't already exist, copy it from storage/.env.template and print some helpful feedback.
if not os.path.exists('.env'):
    print_t("No .env file found. Creating it from the template...", "file")
    subprocess.call('cp storage/.env.template .env', shell=True)
else:
    print_t("The .env file already exists. No changes were made to it.", "file")

# Make the monk script executable
print_t("Making the monk script executable...", "monkey")
if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
    subprocess.call('chmod +x monk', shell=True)

if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
    alias_exists = subprocess.call('alias | grep -q "^alias monk="', shell=True)
    if alias_exists == 1:
        print_t("The 'monk' alias is already present.", "link")
    else:
        print_t("Adding 'monk' alias... ", "link")

        if not current_shell_rc:
            print_t("Could not determine current shell. Please add the 'monk=./monk' alias manually to be "
                    "able to use the monk command more easily.", "important")
            sys.exit(1)
        subprocess.call(f'echo "alias monk=\'{PYTHON_COMMAND} ./monk\'" >> {current_shell_rc}', shell=True)
        print_t("The 'monk' alias was added.", "success")
        print_t("You can now use the 'monk' command in this directory to run scripts located in the 'scripts' "
                "directory.", "success")
elif os_type.startswith("win"):  # If OS is Windows
    if os.path.exists("monk.bat"):
        print_t("The 'monk.bat' batch file is already present.", "success")
    else:
        print_t("Creating 'monk.bat' batch file for Windows compatibility... ", "link")
        with open("monk.bat", "w") as batch_file:
            batch_file.write(f"@echo off\n{PYTHON_COMMAND} ./monk %*")
        print_t("The 'monk.bat' batch file was created. Run it using 'monk'.", "success")
else:
    print_t("OS not detected. Please add 'monk' to your PATH manually to use the `monk` command.", "warning")

# Use monk to generate the default configs
if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
    subprocess.call(f'{PYTHON_COMMAND} ./monk generate-monkeys', shell=True)
elif os_type == "windows":  # If OS is Windows
    subprocess.call('python monk.py generate-monkeys', shell=True)
print_t("Monkey configs are based on the 'monkey-manifest.yaml' file. Individual configs will be "
        "generated in the 'monkeys' directory.", "info")
print_t("After making changes, use 'monk generate-monkeys' to apply them.",
        "tip")
if current_shell_rc is not None:
    print_t(f'You still need to source your {current_shell_rc} to use the `monk` command (if initial setup).',
            'super_important')
    print_t(f"Run `source {current_shell_rc}`", 'tip')
elif os_type == "darwin" or os_type == "linux":
    print_t("Shell undetermined. Please source your shell profile to enable the 'monk' command", 'warning')

print_t('CodeMonkeys setup complete', 'done')
