import os
import openai
import json
import pathlib
import subprocess
import sys
from dotenv import load_dotenv
from datetime import datetime
from scripts.get_gpt_client import create_gpt_client

# Check if the monkey name argument is provided
if len(sys.argv) < 2:
    print("⚠️ Please provide the name of the monkey as a command-line argument.")
    exit(1)

print("🚀 Welcome to the Monkeyspace! Let's wreak the opposite of havoc on your [whatever] with Monkey Power! 🌟")

# Define variables from environment
openai.api_key = os.getenv("OPENAI_API_KEY")
codebase = os.getenv("CODEBASE_PATH")

# Get monkey name from command-line arg & load config
# imports variables: main_prompt, usage_prompt, summarization_prompt, special_file
if len(sys.argv) < 2:
    if default_monkey:
        default_monkey_config_file = f"../monkeys/{default_monkey}"
        # If no monkey name provided, use default if it exists
        if pathlib.Path(default_monkey_config_file).exists():
            print(f"🐒 No monkey name provided. Loading default monkey configuration from {default_monkey}...")
            monkey_config_file = default_monkey_config_file
        else:
            print(f"⚠️ No monkey name provided and default configuration {default_monkey} not found. Please specify a monkey name.")
            exit(1)
    else:
        print("⚠️ No monkey name provided and no default monkey configured. Please specify a monkey name.")
        exit(1)
else:
    monkey_name = sys.argv[1]
    monkey_config_file = f"../monkeys/{monkey_name}"
    print(f"🐒 Loading {monkey_name} monkey configuration...")

script_path = "scripts/load-monkey-config.py"
subprocess.run(["python", script_path, monkey_name], check=True)

# Create an instance of GPTCommunication for 3.5 and 4
gpt_3 = create_gpt_client(3.5)
gpt_4 = create_gpt_client(4)

# Summarize the special file
with open(special_file, "r") as f:
    special_file_contents = f.read()
special_file_summary = gpt_4.prompt(summarization_prompt + special_file_contents).choices[0].text.strip()

print("📋 Special file summarized successfully! 📝")
print(f"📝 Summary: {special_file_summary}\n")

# Iterate over each file in the codebase
for root, dirs, files in os.walk(codebase):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, "r") as f:
            file_contents = f.read()

        # Generate suggestions for implementing the special file
        usage_input = usage_prompt + special_file_summary + file_contents
        suggestions = gpt_4.prompt(usage_input).choices[0].text.strip()

        print(f"🔍 Generating suggestions for {file}... 🤔")
        print(f"💡 Suggestions: {suggestions}\n")

        # Apply the main prompt to generate updates
        main_input = main_prompt + special_file_summary + suggestions + file_contents
        updates = gpt_4.prompt(main_input).choices[0].text.strip()

        print(f"⚙️ Applying AI suggestions to {file}... 🤖")
        print(f"✅ Updates applied successfully!\n")

        # Write the updates back to the file
        with open(file_path, "w") as f:
            f.write(updates)

        # Stage the file
        repo.git.add(file_path)

        print(f"✨ {file} staged for commit! 📂")

        # Commit the changes
        commit_message = f"Applied AI suggestions to {file}"
        repo.git.commit('-m', commit_message)

        print(f"🎉 Changes in {file} committed

