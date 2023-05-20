import yaml
import os
import sys

def is_valid_path(path):
    if not os.path.exists(os.path.expanduser(path)):
        print("Invalid path. Please try again.")
        return False
    return True

def prompt_model():
    while True:
        model = input("Enter the model to use for the prompts. Choose 3 (gpt-3.5-turbo) or 4 (gpt-4): ")
        if model not in ['3', '4']:
            print("Invalid choice. Please try again.")
            continue
        return model

def prompt_path(message):
    while True:
        path = input(message)
        if is_valid_path(path):
            return path

def handle_prompt(prop_name):
    prompt_text = {
        'MAIN_PROMPT': "Please enter the main prompt: ",
        'SUMMARY_PROMPT': "Please enter the prompt for summarizing the special file: ",
        'USAGE_PROMPT': "Please enter the prompt for generating guidance: ",
        'MAIN_PROMPT_ULTIMATUM': "Please enter a final ultimatum for the main prompt: "
    }
    if prop_name in prompt_text:
        return input(prompt_text[prop_name])
    return None

def handle_override(prop_name):
    override_text = {
        'OVERRIDE_WORK_PATH': "Please enter the path to the work_path to use (absolute path or start with ~ for home dir on Mac/Linux): ",
        'OVERRIDE_PROCESS_FILE_FN': "Please enter the override program's process_file function (relative path from overrides/process_file/): ",
        'OVERRIDE_MAIN_PROGRAM': "Please enter the override program's main.py from (relative path from programs/): "
    }
    if prop_name in override_text:
        return prompt_path(override_text[prop_name])
    return None

def handle_output(prop_name):
    output_text = {
        'OUTPUT_EXAMPLE': "Please enter an example of the output you want to see: ",
        'OUTPUT_CHECK_PROMPT': "Please enter a prompt for checking the output: ",
        'OUTPUT_FILENAME_APPEND': "Please enter text to append to output filenames: ",
        'OUTPUT_EXT': "Please enter text to override output file extensions: "
    }
    if prop_name in output_text:
        return input(output_text[prop_name])
    return None

def handle_other(prop_name):
    other_text = {
        'SPECIAL_FILE': "Please enter a file which will be summarized using SUMMARY_PROMPT to give context for the main prompt (absolute path): "
    }
    if prop_name in other_text:
        return prompt_path(other_text[prop_name])
    return None

def handle_yaml(data):
    new_data = {}
    for key, value in data.items():
        if key.endswith('_PROMPT'):
            new_value = handle_prompt(key)
        elif key.startswith('OVERRIDE_'):
            new_value = handle_override(key)
        elif key.startswith('OUTPUT_'):
            new_value = handle_output(key)
        elif key in ['MAIN_MODEL', 'SUMMARY_MODEL', 'USAGE_MODEL']:
            new_value = prompt_model()
        else:
            new_value = handle_other(key)
        if new_value is None:
            new_value = value
        new_data[key] = new_value
    return new_data

def main():
    print("\nWelcome to the Monkey Manifest Configuration tool.\n")

    # Open the YAML file and load the data
    try:
        with open('monkey-manifest.yaml', 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print("Error: 'monkey-manifest.yaml' file not found.")
        sys.exit(1)

    # Iterate over the monkeys
    for monkey, monkey_data in data.items():
        print(f"\nNow configuring the {monkey}...")
        new_monkey_data = handle_yaml(monkey_data)
        data[monkey] = new_monkey_data

    # Save the modified data back to the file
    with open('monkey-manifest.yaml', 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

    print("\nConfiguration complete. The 'monkey-manifest.yaml' file has been updated.\n")

if __name__ == '__main__':
    main()

