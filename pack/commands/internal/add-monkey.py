import argparse
import os
import sys
import tempfile
from io import StringIO

from ruamel.yaml import YAML, CommentedMap

from definitions import ROOT_PATH, COMMANDS_INTERNAL_PATH
from pack.modules.internal.config_mgmt.add_monkey_input_prompts import INPUT_PROMPTS
from pack.modules.internal.config_mgmt.monkey_config_validations import get_user_config_value, validate_monkey_name
from pack.modules.internal.theme.theme_functions import print_t, input_t
from pack.modules.internal.utils.monk_helpers import run_command_as_module

yaml = YAML()
yaml.default_style = "'"
yaml.indent(sequence=4, offset=2)


def process_input_prompts(data):
    return {key: get_user_config_value(key, validate_function, hint) for key, validate_function, hint in data}


def main(monk_args: argparse.Namespace):
    monkey_name = getattr(monk_args, 'monkey', None)
    if monkey_name is None or not validate_monkey_name(monkey_name):
        monkey_name = get_user_config_value("Please enter a name for your new monkey: ",
                                            validate_monkey_name, "(letters/hyphens only)")

    print_t(f"Let's configure your new {monkey_name} monkey", 'monkey')

    monkey_manifest_path = os.path.join(ROOT_PATH, 'monkey-manifest.yaml')
    with open(monkey_manifest_path, 'r') as file:
        try:
            monkey_manifest = yaml.load(file)
        except Exception as e:
            print_t("An error occurred while reading the monkey-manifest file: " + str(e), 'error')
            return

    if monkey_name in monkey_manifest.keys():
        print_t(f"A monkey named {monkey_name} already exists.", 'important')
        result = input_t(f"Would you like to overwrite the existing config?", '(y/n)')
        if result.lower() != 'y':
            sys.exit(0)
        else:
            print_t("Continuing config...", 'done')

    new_monkey_data = process_input_prompts(INPUT_PROMPTS)

    comment = f"Config for {monkey_name} generated by `monk add-monkey`"
    new_monkey_commented_map = CommentedMap(new_monkey_data)
    new_monkey_commented_map.yaml_set_start_comment(comment)

    monkey_manifest[monkey_name] = new_monkey_commented_map

    yaml_string = StringIO()
    yaml.dump(monkey_manifest, yaml_string)

    yaml_string = yaml_string.getvalue().replace(monkey_name + ":", os.linesep + monkey_name + ":")

    with tempfile.NamedTemporaryFile('w', delete=False) as temp_file:
        temp_file_name = temp_file.name
        temp_file.write(yaml_string)

    try:
        os.replace(temp_file_name, monkey_manifest_path)
    except Exception as e:
        print_t("An error occurred while updating the monkey-manifest file: " + str(e), 'error')
        return

    print_t("Config complete. The 'monkey-manifest.yaml' file has been updated.", 'done')
    run_generate = input_t("Run `monk generate-monkeys` to complete the config process?", '(y/n)')
    if run_generate.lower() == 'y':
        run_command_as_module(os.path.join(COMMANDS_INTERNAL_PATH, 'generate-monkeys.py'), 'main', [])


if __name__ == '__main__':
    main()
