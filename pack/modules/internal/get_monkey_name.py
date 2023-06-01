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


def get_monkey_name(supplied_name) -> Tuple[str, str]:
    default_monkey = os.getenv("DEFAULT_MONKEY")

    # No monkey name provided
    if not supplied_name:
        if default_monkey and pathlib.Path(os.path.join(MONKEYS_PATH, default_monkey)).exists():
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
    elif not pathlib.Path(os.path.join(MONKEYS_PATH, supplied_name)).exists():
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

    monkey_config_file = os.path.join(MONKEYS_PATH, monkey_name, f'{monkey_name}.yaml')
    return monkey_name, monkey_config_file
