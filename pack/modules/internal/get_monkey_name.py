import os
import pathlib
from typing import List, Tuple

import yaml
from dotenv import load_dotenv

from definitions import MONKEYS_PATH
from pack.modules.custom.theme.theme_functions import print_t, input_t

# Load environment variables from .env file
load_dotenv()


def list_monkeys() -> List[str]:
    # Change to list directories instead of files
    dirs = [d for d in os.listdir(MONKEYS_PATH) if os.path.isdir(os.path.join(MONKEYS_PATH, d))]
    return dirs


def get_monkey_name(supplied_name, allow_new: bool = False) -> Tuple[str, str]:
    default_monkey = os.getenv("DEFAULT_MONKEY")

    # No monkey name provided
    if not supplied_name:
        if default_monkey and pathlib.Path(MONKEYS_PATH + default_monkey).exists():
            print_t(f"No monkey name provided. Loading default monkey config from {default_monkey}...", 'monkey')
            monkey_name = default_monkey
        else:
            print_t("No monkey name provided. Please select from the available monkeys:", 'warning')
            monkeys = list_monkeys()
            for idx, monkey in enumerate(monkeys, start=1):
                print_t(f"{idx}. {monkey}", 'option')
            monkey_index = int(input_t("Enter the number of the monkey: ", 'input')) - 1
            monkey_name = monkeys[monkey_index]
    # Monkey name provided but does not exist
    elif not pathlib.Path(MONKEYS_PATH + supplied_name).exists():
        if allow_new:
            print_t(f"Monkey {supplied_name} not found. You can create {supplied_name}, or select "
                    f"an existing monkey:", 'warning')
            monkeys = list_monkeys()
            print_t(f"🐒 0. New Monkey with name {supplied_name}", 'green')
            for idx, monkey in enumerate(monkeys, start=1):
                print_t(f"{idx}. {monkey}", 'option')
            monkey_index = int(input_t("Enter the number of the monkey: ", 'input'))
            monkey_name = supplied_name if monkey_index == 0 else monkeys[monkey_index - 1]
            # Add a new monkey to the yaml if the user decides to add a new one
            if monkey_index == 0:
                os.makedirs(MONKEYS_PATH + monkey_name)  # Create a directory for the new monkey
                with open(MONKEYS_PATH + monkey_name + '/monkey-manifest.yaml', 'w') as f:
                    data = {}  # Initialize the new monkey with empty data
                    yaml.dump(data, f, default_flow_style=False)
        else:
            print_t("No valid monkey name provided. Please select an existing monkey:", 'warning')
            monkeys = list_monkeys()
            for idx, monkey in enumerate(monkeys, start=1):
                print_t(f"{idx}. {monkey}", 'cyan')
            monkey_index = int(input("Enter the number of the monkey: ")) - 1
            monkey_name = monkeys[monkey_index]
    # Monkey name provided and exists
    else:
        monkey_name = supplied_name
        print_t(f"Loaded {monkey_name} config...", 'done')

    monkey_config_file = MONKEYS_PATH + monkey_name + '/monkey-manifest.yaml'
    return monkey_name, monkey_config_file
