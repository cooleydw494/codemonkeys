import os
import pathlib
import yaml
from dotenv import load_dotenv
from typing import List, Tuple
from termcolor import colored

# Load environment variables from .env file
load_dotenv()


def list_monkeys(directory: str = "../monkeys/") -> List[str]:
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files


def get_monkey_name(argv: List[str], allow_new: bool = False) -> Tuple[str, str]:
    default_monkey = os.getenv("DEFAULT_MONKEY")
    monkey_dir = "../monkeys/"

    # No monkey name provided
    if len(argv) < 2:
        if default_monkey and pathlib.Path(monkey_dir + default_monkey).exists():
            print(f"🐒 No monkey name provided. Loading default monkey configuration from {default_monkey}...")
            monkey_name = default_monkey
        else:
            print("⚠️ No monkey name provided. Please select from the available monkeys:")
            monkeys = list_monkeys(monkey_dir)
            for idx, monkey in enumerate(monkeys, start=1):
                print(f"{idx}. {monkey}")
            monkey_index = int(input("Enter the number of the monkey: ")) - 1
            monkey_name = monkeys[monkey_index]
    # Monkey name provided but does not exist
    elif not pathlib.Path(monkey_dir + argv[1]).exists():
        if allow_new:
            print(f"⚠️ Monkey {argv[1]} does not exist. You can create a new monkey with this name, or select "
                  f"from the available monkeys:")
            monkeys = list_monkeys(monkey_dir)
            print(colored(f"0. New Monkey with name {argv[1]}", 'green'))
            for idx, monkey in enumerate(monkeys, start=1):
                print(f"{idx}. {monkey}")
            monkey_index = int(input("Enter the number of the monkey: "))
            monkey_name = argv[1] if monkey_index == 0 else monkeys[monkey_index - 1]
            # Add a new monkey to the yaml if the user decides to add a new one
            if monkey_index == 0:
                with open('monkey-manifest.yaml', 'r') as f:
                    data = yaml.safe_load(f)
                data[monkey_name] = {}  # Initialize the new monkey with empty data
                with open('monkey-manifest.yaml', 'w') as f:
                    yaml.dump(data, f, default_flow_style=False)
        else:
            print("⚠️ No valid monkey name provided. Please select from the available monkeys:")
            monkeys = list_monkeys(monkey_dir)
            for idx, monkey in enumerate(monkeys, start=1):
                print(f"{idx}. {monkey}")
            monkey_index = int(input("Enter the number of the monkey: ")) - 1
            monkey_name = monkeys[monkey_index]
    # Monkey name provided and exists
    else:
        monkey_name = argv[1]
        print(f"🐒 Loading {monkey_name} monkey configuration...")

    monkey_config_file = monkey_dir + monkey_name
    return monkey_name, monkey_config_file