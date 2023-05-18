import os
import subprocess
from dotenv import load_dotenv, set_key

# Load the .env file
load_dotenv()

# Get the absolute path of CODE_MONKEY_DIR from .env
base_dir_abs_path = os.getenv("BASE_DIR_ABS_PATH")

print("🚀 Starting the setup... Hang tight! 🌟")

# Check if python3 and pip are installed
if subprocess.call('command -v python3', shell=True) == 0 and subprocess.call('command -v pip3', shell=True) == 0:
    print("✅ Python 3 and pip are installed. Amazing! 🐍")
else:
    print("⚠️ Uh-oh! It seems Python 3 or pip is not installed. Please install them and try again. 🤔")
    exit(1)

# Install required python modules from requirements.txt
print("⏳ Installing the required python modules... This may take a moment. 🛠️")
subprocess.call('pip3 install -r requirements.txt', shell=True)

# Set default values for .env if not already set
print("📝 Setting default .env values if not already set... ✨")
env_file = os.path.join(base_dir_abs_path, '.env')

# if the .env doesn't already exist, copy it from storage/.env.template and print some helpful feedback. If it does exist, let the user know it already exists
if not os.path.exists(env_file):
    print("📝 Creating the .env file from the template... 📄")
    subprocess.call('cp storage/.env.template .env', shell=True)
else:
    print("⚠️ The .env file already exists. Skipping... 📄")

# Make the monk script executable
print("🔐 Making the monk script executable... Just a sec! 🔒")
subprocess.call('chmod +x monk', shell=True)

# Use monk to generate the default configurations
print("🔧 Generating the default monkey configurations... 🐵🎛️")
subprocess.call('./monk generate-monkeys', shell=True)

# Feedback to the user
print("🎉 Installation finished! Woohoo! 🎊")
print("✨ You're now ready to rock 'n' roll with the 'monk' command inside this directory to run scripts in the 'scripts' directory. ✨")
print("📝 Feel free to edit the monkey configurations in the 'monkeys/monkey-manifest.yaml' file. 🐵📄")
print("💡 To apply changes, regenerate the configurations using the command: './monk generate-monkeys'. Keep going! 🚀")

