#!/bin/bash

cd ../../..

if [[ -f ./.env ]]; then
    echo "You already have a .env file, so it's likely you already ran this script."
    echo "Please address your needs without re-installing or remove/back-up your current .env file and re-run the install script."
    exit 1
fi

# Give feedback about the process.
echo "🚀 Starting the setup... Hang tight! 🌟"

# Check if python3 and pip are installed
if command -v python3 &>/dev/null && command -v pip3 &>/dev/null; then
    echo "✅ Python 3 and pip are installed. Amazing! 🐍"
else
    echo "⚠️ Uh-oh! It seems Python 3 or pip is not installed. Please install them and try again. 🤔"
    exit 1
fi

# Install required python modules from requirements.txt
echo "⏳ Installing the required python modules... This may take a moment. 🛠️"
pip3 install -r requirements.txt

# Create .env template
echo "📝 Creating the .env template file... ✨"
touch .env
echo 'OPENAI_API_KEY="your_openai_api_key"' > .env
scripts_root_dir=$(pwd -P)/scripts
echo "SCRIPTS_ROOT_DIR=${scripts_root_dir}" > .env

# Make the monk script executable
echo "🔐 Making the monk script executable... Just a sec! 🔒"
chmod +x monk

# Use monk to generate the default configurations
echo "🔧 Generating the default monkey configurations... 🐵🎛️"
./monk generate-monkeys

# Feedback to the user
echo "🎉 Installation finished! Woohoo! 🎊"
echo "✨ You're now ready to rock 'n' roll with the 'monk' command inside this directory to run scripts in the 'scripts' directory. ✨"
echo "📝 Feel free to edit the monkey configurations in the 'monkeys/monkey-manifest.yaml' file. 🐵📄"
echo "💡 To apply changes, regenerate the configurations using the command: './monk generate-monkeys'. Keep going! 🚀"

