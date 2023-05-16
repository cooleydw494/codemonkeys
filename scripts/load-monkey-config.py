import os
import sys

# Check if the monkey name argument is provided
if len(sys.argv) < 2:
    print("⚠️ Please provide the name of the monkey as a command-line argument.")
    exit(1)

# Get the monkey name from the command-line argument
monkey_name = sys.argv[1]
monkey_config_file = f"../monkeys/{monkey_name}.py"

# Check if the monkey configuration file exists
if not os.path.isfile(monkey_config_file):
    print(f"⚠️ Monkey configuration file '{monkey_name}.py' not found.")
    exit(1)

# Load the monkey configuration variables
monkey_config = {}
try:
    exec(open(monkey_config_file).read(), monkey_config)
except Exception as e:
    print(f"⚠️ Failed to load monkey configuration file '{monkey_name}.py'. Error: {str(e)}")
    exit(1)

# Extract the configuration variables
main_prompt = monkey_config.get("MAIN_PROMPT", "")
usage_prompt = monkey_config.get("USAGE_PROMPT", "")
summarization_prompt = monkey_config.get("SUMMARIZATION_PROMPT", "")
special_file = monkey_config.get("SPECIAL_FILE", "")

# Print the loaded configuration variables
print(f"🐵 Monkey Configuration Loaded: {monkey_name} 🌟")
print(f"MAIN_PROMPT: {main_prompt}")
print(f"USAGE_PROMPT: {usage_prompt}")
print(f"SUMMARIZATION_PROMPT: {summarization_prompt}")
print(f"SPECIAL_FILE: {special_file}")

