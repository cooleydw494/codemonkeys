import os
import sys

import yaml

from definitions import MONKEYS_PATH
from pack.modules.custom.theme.theme_functions import print_t
from pack.modules.internal.get_monkey_name import get_monkey_name
from pack.modules.internal.utils.general_helpers import get_monkey_config_defaults

MONKEY_CONFIG_DEFAULTS = get_monkey_config_defaults(short=True)

# Define input prompts
INPUT_PROMPTS = {
    'MAIN_PROMPT': "Please generate code for the following task... ",
    'SUMMARY_PROMPT': "Provide a summary of this file... ",
    'MAIN_PROMPT_ULTIMATUM': "Limit your response to the full contents of a python script, and nothing else. ",
    'WORK_PATH': "Please enter the path to the WORK_PATH to use (absolute path or start with ~ for home dir on "
                 "Mac/Linux): ",
    'OUTPUT_EXAMPLE': "Limit your output strictly to the contents of the file, like this: ```complete contents of "
                      "file```.",
    'OUTPUT_CHECK_PROMPT': "Examine the following output and determine if 1. The output is complete and 2. The output "
                           "is limited strictly to the contents of a file. Format your response exactly like this: "
                           "```is_limited_to_file_contents:[1/0],is_complete:[1/0]```.",
    'OUTPUT_FILENAME_APPEND': "Please enter text to append to output filenames: ",
    'OUTPUT_EXT': "Please enter text to override output file extensions: ",
    'SPECIAL_FILE': "Please enter a file which will be summarized using SUMMARY_PROMPT to give context for the main "
                    "prompt (absolute path): ",
    'MAIN_MODEL': "Enter the model to use for the main prompts. Choose 3 (gpt-3.5-turbo) or 4 (gpt-4): ",
    'SUMMARY_MODEL': "Enter the model to use for the summary prompts. Choose 3 (gpt-3.5-turbo) or 4 (gpt-4): ",
    'OUTPUT_CHECK_MODEL': "Enter the model to use for the usage prompts. Choose 3 (gpt-3.5-turbo) or 4 (gpt-4): ",
    'MAIN_TEMP': "Enter the temperature to use for the main prompts (a value between 0 and 1): ",
    'SUMMARY_TEMP': "Enter the temperature to use for the summary prompts (a value between 0 and 1): ",
    'OUTPUT_CHECK_TEMP': "Enter the temperature to use for the usage prompts (a value between 0 and 1): "
}


def is_valid_path(path):
    if not os.path.exists(os.path.expanduser(path)):
        print_t("Invalid path. Please try again.", 'error')
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


def main(supplied_monkey_name=''):
    print_t("Welcome to the Monkey Manifest Configuration tool.", 'monkey')

    # Fetch the monkey name to configure
    monkey_name, _ = get_monkey_name(supplied_monkey_name, allow_new=True)

    # Open the YAML file and load the data
    try:
        with open(os.path.join(MONKEYS_PATH, monkey_name, f'{monkey_name}.yaml'), 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print_t(f"{monkey_name}.yaml file not found.", 'error')
        sys.exit(1)

    # If the monkey is new, initialize with the default config, otherwise load existing data
    monkey_data = data.get(monkey_name, MONKEY_CONFIG_DEFAULTS)

    print_t(f"Now configuring {monkey_name}...", 'config')
    new_monkey_data = handle_yaml(monkey_data)
    data[monkey_name] = new_monkey_data

    # Save the modified data back to the file
    with open('monkey-manifest.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

    print_t("Configuration complete. The 'monkey-manifest.yaml' file has been updated.", 'done')


if __name__ == '__main__':
    main()
