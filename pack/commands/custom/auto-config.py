import yaml
import os
import sys

from ...modules.internal.get_monkey_name import get_monkey_name
from pack.modules.custom.style.visuals import printc
from definitions import STORAGE_INTERNAL_PATH

# Load the default monkey configuration
DEFAULT_MONKEY_CONFIG_PATH = os.path.join(STORAGE_INTERNAL_PATH, "default-monkey-config")
try:
    with open(DEFAULT_MONKEY_CONFIG_PATH, 'r') as f:
        DEFAULT_MONKEY_CONFIG = yaml.safe_load(f)
except FileNotFoundError:
    printc(f"Error: Default monkey configuration file not found at '{DEFAULT_MONKEY_CONFIG_PATH}'.", 'error')
    sys.exit(1)
except yaml.YAMLError:
    printc(f"Error: Default monkey configuration file at '{DEFAULT_MONKEY_CONFIG_PATH}' is invalid.", 'error')
    sys.exit(1)

# Define input prompts
INPUT_PROMPTS = {
    'MAIN_PROMPT': "Please enter the main prompt: ",
    'SUMMARY_PROMPT': "Please enter the prompt for summarizing the special file: ",
    'USAGE_PROMPT': "Please enter the prompt for generating guidance: ",
    'MAIN_PROMPT_ULTIMATUM': "Please enter a final ultimatum for the main prompt: ",
    'OVERRIDE_WORK_PATH': "Please enter the path to the work_path to use (absolute path or start with ~ for home dir "
                          "on Mac/Linux): ",
    'OVERRIDE_PROCESS_FILE_FN': "Please enter the override program's process_file function (relative path from "
                                "overrides/process_file/): ",
    'OVERRIDE_MAIN_PROGRAM': "Please enter the override program's main.py from (relative path from programs/): ",
    'OUTPUT_EXAMPLE': "Please enter an example of the output you want to see: ",
    'OUTPUT_CHECK_PROMPT': "Please enter a prompt for checking the output: ",
    'OUTPUT_FILENAME_APPEND': "Please enter text to append to output filenames: ",
    'OUTPUT_EXT': "Please enter text to override output file extensions: ",
    'SPECIAL_FILE': "Please enter a file which will be summarized using SUMMARY_PROMPT to give context for the main "
                    "prompt (absolute path): ",
    'MAIN_MODEL': "Enter the model to use for the main prompts. Choose 3 (gpt-3.5-turbo) or 4 (gpt-4): ",
    'SUMMARY_MODEL': "Enter the model to use for the summary prompts. Choose 3 (gpt-3.5-turbo) or 4 (gpt-4): ",
    'USAGE_MODEL': "Enter the model to use for the usage prompts. Choose 3 (gpt-3.5-turbo) or 4 (gpt-4): "
}


def is_valid_path(path):
    if not os.path.exists(os.path.expanduser(path)):
        printc("Invalid path. Please try again.", 'error')
        return False
    return True


def handle_input(prop_name, old_value):
    input_handlers = {
        'path': lambda p: input(p) if is_valid_path(input(p)) else old_value,
        'model': lambda p: input(p) if input(p) in ['3', '4'] else old_value,
        'default': lambda p: input(p) or old_value
    }
    prompt = INPUT_PROMPTS[prop_name]
    input_type = 'path' if 'path' in prompt.lower() else 'model' if 'model' in prompt.lower() else 'default'
    return input_handlers[input_type](prompt)


def handle_yaml(data):
    return {key: handle_input(key, value) for key, value in data.items()}


def main():
    printc("Welcome to the Monkey Manifest Configuration tool.", 'monkey')

    # Fetch the monkey name to configure
    monkey_name, _ = get_monkey_name(sys.argv, allow_new=True)

    # Open the YAML file and load the data
    try:
        with open('monkey-manifest.yaml', 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        printc("Error: 'monkey-manifest.yaml' file not found.", 'error')
        sys.exit(1)

    # If the monkey is new, initialize with the default config, otherwise load existing data
    monkey_data = data.get(monkey_name, DEFAULT_MONKEY_CONFIG)

    printc(f"Now configuring {monkey_name}...", 'config')
    new_monkey_data = handle_yaml(monkey_data)
    data[monkey_name] = new_monkey_data

    # Save the modified data back to the file
    with open('monkey-manifest.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

    printc("Configuration complete. The 'monkey-manifest.yaml' file has been updated.", 'done')


if __name__ == '__main__':
    main()
