import os
import platform
import shutil
import subprocess

from termcolor import colored
from modules.internal.environment_checks import environment_checks
from definitions import PIP_COMMAND

current_shell_rc = None
environment_checks()

print(colored("🚀 Initiating the setup process... 🌟", "green"))

# Get the OS type
os_type = platform.system().lower()
print(colored(f"🔍 Detected {os_type.capitalize()} as your operating system... Let's continue.", "cyan"))

# Install required python modules from requirements.txt
print(colored("⏳ Installing the required Python modules from the requirements.txt file... 🛠️", "cyan"))
subprocess.call(f'{PIP_COMMAND} install -r requirements.txt', shell=True)

# Set default values for .env if not already set
print(colored("📝 Checking the .env file... ✨", "cyan"))

# if the .env doesn't already exist, copy it from storage/.env.template and print some helpful feedback.
if not os.path.exists('.env'):
    print(colored("📝 .env file not found. Creating it from the template... 📄", "cyan"))
    subprocess.call('cp storage/.env.template .env', shell=True)
else:
    print(colored("⚠️ The .env file already exists. No changes were made to it. 📄", "yellow"))

# Make the monk script executable
print(colored("🔐 Making the monk script executable... 🔒", "cyan"))
if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
    subprocess.call('chmod +x monk', shell=True)
elif os_type == "windows":  # If OS is Windows
    print(colored("⚠️ On Windows, Python scripts are typically run directly with the Python interpreter, so when you "
                  "see something like `monk [script-name]` in the docs, so should instead do something like:"
                  "`python monk.py [script-name]` or `py monk.py [script-name]`. 🖥️", "yellow"))

# PSEUDO_PACKAGE
#
# subprocess.call(f'python3 {SCRIPTS_INTERNAL_PATH}/fix-namespace.py', shell=True)
# old_pseudo_package_dir_name = PSEUDO_PACKAGE_DIR_NAME
#
# # ! ! ! ! !  I M P O R T A N T  ! ! ! ! ! ! ! ! ! !  I M P O R T A N T  ! ! ! ! ! ! ! ! !  I M P O R T A N T  ! ! ! !
# # For the rest of this script, use lowercase local variables instead of imports from definitions.py
# # The ROOT_PATH (and all derived definitions.py paths) may have changed during execution of fix-namespace.py
#
#
# with open(os.path.join('.', 'storage', 'internal', 'root_path.txt'), 'r') as f:
#     root_path = f.read().strip()
# with open(os.path.join('.', 'storage', 'internal', 'pseudo_package_dir_name.txt'), 'r') as f:
#     pseudo_package_dir_name = f.read().strip()
# pseudo_package_path = os.path.join(root_path, pseudo_package_dir_name)
#
# # Get the site-packages directory and filepath for the pth file
# site_packages_dir = site.getsitepackages()[0]
# old_pth_file_path = os.path.join(site_packages_dir, f"{old_pseudo_package_dir_name}.pth")
# pth_file_path = os.path.join(site_packages_dir, f"{pseudo_package_dir_name}.pth")
#
# # Remove old .pth if changed and not default (likely to be old path on setup and may still be used in first install)
# if old_pseudo_package_dir_name != 'code_monkeys' \
#         and pseudo_package_dir_name != old_pseudo_package_dir_name \
#         and os.path.exists(old_pth_file_path):
#     os.remove(old_pth_file_path)
#
# if os.path.exists(pth_file_path):
#     print(colored(f"Overwriting existing .pth file (installs {pseudo_package_dir_name} pseudo-package)...", "yellow"))
# else:
#     print(colored(f"""Let's install the {pseudo_package_dir_name} pseudo-package!
#
# The pseudo-package isn't "installed" in the typical sense, but allows easy imports of modules globally.
# Let's create '{pseudo_package_dir_name}.pth' in the 'site-packages' directory, so Python can find CodeMonkeys' modules.
# "The {pseudo_package_dir_name} pseudo-package allows you and I to add/edit/import modules with ease!""", "cyan"))
#     # Write the project root directory to the .pth file
#     with open(pth_file_path, "w") as pth_file:
#         pth_file.write(pseudo_package_path)
#     # give user success feedback which includes the absolute filepath of the .pth file
#     print(colored(f"✅ Created the .pth file at {pth_file_path}. 📄", "green"))

if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
    alias_exists = subprocess.call('alias | grep -q "^alias monk="', shell=True)
    if alias_exists == 0:
        print(colored("✅ The 'monk' alias is already present. 💻", "green"))
    else:
        print(colored("🔗 Adding 'monk' alias... ", "cyan"))
        current_shell = os.environ['SHELL']
        if current_shell.endswith("bash"):
            current_shell_rc = "~/.bashrc"
        elif current_shell.endswith("zsh"):
            current_shell_rc = "~/.zshrc"
        elif current_shell.endswith("fish"):
            current_shell_rc = "~/.config/fish/config.fish"
        else:
            print(colored("⚠️ Could not determine current shell. Please add the 'monk=./monk' alias manually to be "
                          "able to use the monk command more easily. 🖥️", "yellow"))
            exit(1)
        subprocess.call(f'echo "alias monk=\'./monk\'" >> {current_shell_rc}', shell=True)
        print(colored("✅ The 'monk' alias was added. 💻", "green"))
elif os_type.startswith("win"):  # If OS is Windows
    if os.path.exists("monk.py"):
        print(colored("✅ The 'monk.py' command is already present. 💻", "green"))
    else:
        print(colored("🔗 Renaming 'monk' to 'monk.py' for Windows compatibility... ", "cyan"))
        shutil.move("monk", "monk.py")
        print(colored("✅ The 'monk' command was renamed to 'monk.py'. Run it using 'python monk.py'. 💻", "green"))
else:
    print(colored("⚠️ Unrecognized operating system. Please add 'monk' to your PATH manually. 🖥️", "yellow"))

# Use monk to generate the default configurations
print("🔧 Generating default monkey configurations... 🐵🎛️")
if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
    subprocess.call('./monk generate-monkeys', shell=True)
elif os_type == "windows":  # If OS is Windows
    subprocess.call('python monk.py generate-monkeys', shell=True)
print(colored("Monkey configurations are based on the 'monkey-manifest.yaml' file. Individual configs will be "
              "generated in the 'monkeys' directory.", "green"))

# Feedback to the user
print(colored("🎉 Setup complete! You're all set. 🎊", "green"))
print(colored("✨ You can now use the 'monk' command in this directory to run scripts located in the 'scripts' "
              "directory. ✨", "green"))
print(colored("📝 Feel free to modify the monkey configurations in the 'monkeys/monkey-manifest.yaml' file as per "
              "your needs. You can also edit individual configs directly in the 'monkeys' directory. 🐵📄", "green"))
print(colored("💡 After making any changes, use the command 'monk generate-monkeys' to apply them. Keep going! 🚀",
              "green"))

print("")
print("Thanks for using CodeMonkeys! 🐵🐒🐵🐒🐵🐒🐵🐒🐵🐒🐵🐒🐵🐒🐵🐒🐵🐒🐵🐒🐵🐒")
if current_shell_rc is not None:
    print(colored('⚠️ You still need to source your {current_shell_rc} to be able to use the `monk` command. Press '
                  'enter to acknowledge and exit setup.', 'yellow'))
    print(colored(f"source {current_shell_rc}", 'cyan'))
    input(colored('Press enter to acknowledge and finish setup.', 'yellow'))
elif os_type == "darwin" or os_type == "linux":
    print(colored("⚠️ Shell undetermined. Please source your shell profile to enable the 'monk' command"), 'yellow')
