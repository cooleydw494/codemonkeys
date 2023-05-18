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

if not os.getenv("OPENAI_API_KEY"):
    set_key(env_file, "OPENAI_API_KEY", "your_openai_api_key")
if not os.getenv("CODEBASE_PATH"):
    set_key(env_file, "CODEBASE_PATH", "~/project-directory")
if not os.getenv("FILE_TYPES_INCLUDED"):
    set_key(env_file, "FILE_TYPES_INCLUDED", ".js,.php")
if not os.getenv("FILEPATH_MATCH_EXCLUDED"):
    set_key(env_file, "FILEPATH_MATCH_EXCLUDED", ".config,.md,.git,.txt")
if not os.getenv("DEFAULT_MONKEY"):
    set_key(env_file, "DEFAULT_MONKEY", "generic-monkey")
if not os.getenv("MAX_TOKENS"):
    set_key(env_file, "MAX_TOKENS", "8000")
if not os.getenv("TEMPERATURE"):
    set_key(env_file, "TEMPERATURE", "1")

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

