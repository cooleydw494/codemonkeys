import os
import subprocess
import sys
import json
from dotenv import load_dotenv
from scripts.get_gpt_client import create_gpt_client
from scripts.get_monkey_name import get_monkey_name
from termcolor import colored
import openai

# Check if the monkey name argument is provided
if len(sys.argv) < 2:
    print(colored("⚠️ Please provide the name of the monkey as a command-line argument.", "yellow"))
    exit(1)

print(colored("🚀 Welcome to the Monkeyspace! Let's wreak the opposite of havoc on your [whatever] with Monkey Power! 🌟", "green"))

# Define variables from environment
openai.api_key = os.getenv("OPENAI_API_KEY")
codebase = os.getenv("CODEBASE_PATH")

monkey_name, monkey_config_file = get_monkey_name(sys.argv)
script_path = "scripts/load-monkey-config.py"
process = subprocess.run(["python", script_path, monkey_config_file], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if process.returncode != 0:
    print(colored(process.stderr.decode(), 'red'))
    sys.exit(1)

loaded_config = json.loads(process.stdout.decode())
main_prompt = loaded_config["MAIN_PROMPT"]
usage_prompt = loaded_config["USAGE_PROMPT"]
summarization_prompt = loaded_config["SUMMARIZATION_PROMPT"]
special_file = loaded_config["SPECIAL_FILE"]
default_monkey = loaded_config["DEFAULT_MONKEY"]
summarization_model = loaded_config["SUMMARIZATION_MODEL"]
main_prompt_model = loaded_config["MAIN_PROMPT_MODEL"]
usage_prompt_model = loaded_config["USAGE_PROMPT_MODEL"]

# Create instances of necessary GPT models
gpt_models = {}
for model in {main_prompt_model, summarization_model, usage_prompt_model}:
    if model == '3' and '3' not in gpt_models:
        gpt_models['3'] = create_gpt_client(3.5)
    elif model == '4' and '4' not in gpt_models:
        gpt_models['4'] = create_gpt_client(4)

def gpt_client(model_name):
    return gpt_models.get(model_name)

# Check if the special file exists
if not os.path.isfile(special_file):
    print(colored(f"⚠️ Special file '{special_file}' not found.", "yellow"))
    exit(1)

# Summarize the special file
with open(special_file, "r") as f:
    special_file_contents = f.read()
special_file_summary = gpt_client(summarization_model).prompt(summarization_prompt + special_file_contents).choices[0].text.strip()

print(colored("📋 Special file summarized successfully! 📝", 'green'))
print(colored(f"📝 Summary: {special_file_summary}\n", 'cyan'))

# Iterate over each file in the codebase
for root, dirs, files in os.walk(codebase):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, "r") as f:
            file_contents = f.read()

        # Generate suggestions for implementing the special file
        usage_input = usage_prompt + special_file_summary + file_contents
        suggestions = gpt_client(usage_prompt_model).prompt(usage_input).choices[0].text.strip()

        print(colored(f"🔍 Generating suggestions for {file}... 🤔", 'green'))
        print(colored(f"💡 Suggestions: {suggestions}\n", 'cyan'))

        # Apply the main prompt to generate updates
        main_input = main_prompt + special_file_summary + suggestions + file_contents
        updates = gpt_client(main_prompt_model).prompt(main_input).choices[0].text.strip()

        print(colored(f"⚙️ Applying AI suggestions to {file}... 🤖", 'green'))
        print(colored(f"✅ Updates applied successfully!\n", 'cyan'))

        # Write the updates back to the file
        with open(file_path, "w") as f:
            f.write(updates)

        # Git-related operations are removed for now, as they would require additional setup, like a git.Repo object.
        # It's also a good idea to make sure you're checking which files are being modified before performing commits.

        print(colored(f"✨ {file} updated with AI suggestions!", 'green'))

