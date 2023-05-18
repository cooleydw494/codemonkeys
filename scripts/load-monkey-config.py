import os
import sys
from termcolor import colored

# Check if the monkey name argument is provided
if len(sys.argv) < 2:
    print(colored("⚠️ Please provide the name of the monkey as a command-line argument.", "yellow"))
    exit(1)

# Get the monkey name from the command-line argument
monkey_name = sys.argv[1]
monkey_config_file = f"../monkeys/{monkey_name}.py"

# Check if the monkey configuration file exists
if not os.path.isfile(monkey_config_file):
    print(colored(f"⚠️ Monkey configuration file '{monkey_name}.py' not found.", "yellow"))
    exit(1)

# Load the monkey configuration variables
monkey_config = {}
try:
    exec(open(monkey_config_file).read(), monkey_config)
except Exception as e:
    print(colored(f"⚠️ Failed to load monkey configuration file '{monkey_name}.py'. Error: {str(e)}", "yellow"))
    exit(1)

# Extract the configuration variables
main_prompt = monkey_config.get("MAIN_PROMPT", "")
usage_prompt = monkey_config.get("USAGE_PROMPT", "")
summarization_prompt = monkey_config.get("SUMMARIZATION_PROMPT", "")
special_file = monkey_config.get("SPECIAL_FILE", "")
default_monkey = monkey_config.get("DEFAULT_MONKEY", "")
summarization_model = monkey_config.get("SUMMARIZATION_MODEL", "")
main_prompt_model = monkey_config.get("MAIN_PROMPT_MODEL", "")
usage_prompt_model = monkey_config.get("USAGE_PROMPT_MODEL", "")

# Print the loaded configuration variables
print(colored("🐒 Monkey Configuration Loaded 🐒", 'green'))
print(colored("Monkey Name: ", 'cyan') + f"{monkey_name}")
print(colored("Main Prompt: ", 'cyan') + f"{main_prompt}")
print(colored("Usage Prompt: ", 'cyan') + f"{usage_prompt}")
print(colored("Summarization Prompt: ", 'cyan') + f"{summarization_prompt}")
print(colored("Special File: ", 'cyan') + f"{special_file}")
print(colored("Default Monkey: ", 'cyan') + f"{default_monkey}")
print(colored("Summarization Model: ", 'cyan') + f"{summarization_model}")
print(colored("Main Prompt Model: ", 'cyan') + f"{main_prompt_model}")
print(colored("Usage Prompt Model: ", 'cyan') + f"{usage_prompt_model}")

