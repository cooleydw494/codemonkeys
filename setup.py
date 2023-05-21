import os
import platform
import subprocess
from termcolor import colored

print(colored("🚀 Initiating the setup process... 🌟", "green"))

# Get the OS type
os_type = platform.system().lower()
print(colored(f"🔍 Detected {os_type.capitalize()} as your operating system... Let's continue.", "cyan"))

# Check if python3 is installed
if subprocess.call('command -v python3', shell=True) == 0:
    print(colored("✅ Detected Python 3. Great! Let's proceed. 🐍", "green"))
elif subprocess.call('command -v python', shell=True) == 0:
    print(colored("⚠️ Python 3 was not detected, but Python was found. Our code uses 'python3'.", "yellow"))
    user_input = input(colored("Would you like to alias 'python3' to 'python'? (y/n).", "yellow"))
    if user_input.lower() == 'y':
        if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
            subprocess.call('echo "alias python3=python" >> ~/.bashrc', shell=True)
            print(colored("✅ Aliased 'python3' to 'python'. Open a new terminal to start using 'python3'. 🐍", "green"))
        elif os_type == "windows":  # If OS is Windows
            print(colored("⚠️ Please alias 'python3' to 'python' manually in your environment. 🖥️", "yellow"))
    else:
        print(colored("Makes sense, come back when you have installed python3!", "yellow"))
        exit(1)
else:
    print(colored("⚠️ Python 3 doesn't seem to be installed. Please install it and try again. 🤔", "red"))
    exit(1)

# Check if pip3 is installed
if subprocess.call('command -v pip3', shell=True) == 0:
    print(colored("✅ Detected pip3. Awesome! 🐍", "green"))
elif subprocess.call('command -v pip', shell=True) == 0:
    print(colored("⚠️ pip3 was not detected, but pip was found. Our code uses 'pip3'.", "yellow"))
    user_input = input(colored("Would you like to alias 'pip3' to 'pip'? (y/n).", "yellow"))
    if user_input.lower() == 'y':
        if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
            subprocess.call('echo "alias pip3=pip" >> ~/.bashrc', shell=True)
            print(colored("✅ Aliased 'pip3' to 'pip'. Open a new terminal to start using 'pip3'. 🐍", "green"))
        elif os_type == "windows":  # If OS is Windows
            print(colored("⚠️ Please alias 'pip3' to 'pip' manually in your environment. 🖥️", "yellow"))
    else:
        print(colored("Makes sense, come back when you have installed pip3!", "yellow"))
        exit(1)
else:
    print(colored("⚠️ pip3 doesn't seem to be installed. Please install it and try again. 🤔", "red"))
    exit(1)

# Install required python modules from requirements.txt
print(colored("⏳ Installing the required Python modules from the requirements.txt file... 🛠️", "cyan"))
subprocess.call('pip3 install -r requirements.txt', shell=True)

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
    subprocess.call('chmod +x monk.py', shell=True)
elif os_type == "windows":  # If OS is Windows
    print(colored("⚠️ On Windows, Python scripts are typically run directly with the Python interpreter, so when you "
                  "see something like `monk [script-name]` in the docs, so should instead do something like:"
                  "`python monk.py [script-name]` or `py monk.py [script-name]`. 🖥️", "yellow"))

# Add monk to PATH if monk is not in path
monk_in_path = subprocess.call('command -v monk', shell=True)
if monk_in_path == 0:
    if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
        print(colored("🔗 Adding 'monk' to your PATH... ", "cyan"))
        subprocess.call('echo "export PATH=$PATH:`pwd`" >> ~/.bashrc', shell=True)
        print(colored("✅ The 'monk' command was added to your PATH. "
                      "💻", "green"))
        # source the terminal to make the changes take effect
        print(colored("🔄 Sourcing the terminal to make the changes take effect... ", "cyan"))
        subprocess.call('source ~/.bashrc', shell=True)
        print(colored("✅ The terminal was sourced. You can now use the 'monk' command in this directory to run scripts "
                      "located in the 'scripts' directory. 🐵🎛️", "green"))
        print(colored("⚠️ You may still need to restart or source existing terminals for changes to take effect. 🖥️",
                      "yellow"))
    elif os_type == "windows":  # If OS is Windows
        print(colored("⚠️ Please add 'monk' to your PATH manually in your environment. 🖥️", "yellow"))
        print(colored("⚠️ Please restart your terminal for the changes to take effect. 🖥️", "yellow"))
else:
    print(colored("✅ The 'monk' command is already in your PATH. 💻", "green"))


# Use monk to generate the default configurations
print("🔧 Generating default monkey configurations... 🐵🎛️")
if os_type == "linux" or os_type == "darwin":  # If OS is Linux or macOS
    subprocess.call('python3 monk.py generate-monkeys', shell=True)
    print(colored("Monkey configurations are based on the 'monkey-manifest.yaml' file. Individual configs will be "
                  "generated in the 'monkeys' directory.", "green"))
elif os_type == "windows":  # If OS is Windows
    print(colored("⚠️ Please run `python3 ./monk generate-monkeys` to generate the default monkey configurations. 🐵🎛️",
                  "yellow"))

# Feedback to the user
print(colored("🎉 Setup complete! You're all set. 🎊", "green"))
print(colored("✨ You can now use the 'monk' command in this directory to run scripts located in the 'scripts' "
              "directory. ✨", "green"))
print(colored("📝 Feel free to modify the monkey configurations in the 'monkeys/monkey-manifest.yaml' file as per "
              "your needs. You can also edit individual configs directly in the 'monkeys' directory. 🐵📄", "green"))
print(colored("💡 After making any changes, use the command 'monk generate-monkeys' to apply them. Keep going! 🚀",
              "green"))
