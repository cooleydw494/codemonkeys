import glob
import os
import pathlib
from typing import List, Tuple

from definitions import MONKEYS_PATH
from pack.modules.internal.config_mgmt.env_class import ENV
from pack.modules.internal.theme.theme_functions import print_t, input_t


def list_monkeys() -> List[str]:
    """
    List all monkey YAML files in the directory.

    :return: A list of monkey names (without the .yaml extension)
    """
    file_paths = glob.glob(os.path.join(MONKEYS_PATH, '*.yaml'))
    return [os.path.splitext(os.path.basename(file))[0] for file in file_paths]


def get_monkey_name(given_monkey_name: str = None) -> Tuple[str, str]:
    """
    Retrieve the monkey name and corresponding configuration file path.

    :param given_monkey_name: A given monkey name
    :return: A tuple consisting of monkey name and its configuration file path
    """
    default_monkey = ENV.DEFAULT_MONKEY or None

    def select_monkey_from_list() -> str:
        """
        Lists all monkeys and lets user select one.

        :return: Selected monkey name
        """
        print_t("Please select from the available monkeys:", 'warning')
        monkeys = list_monkeys()
        for idx, monkey in enumerate(monkeys, start=1):
            print_t(f"{idx}. {monkey}", 'option')
        monkey_index = int(input_t("Enter the number of the monkey")) - 1
        return monkeys[monkey_index]

    def monkey_exists(name: str) -> bool:
        """
        Check if monkey configuration file exists.

        :param name: Monkey name
        :return: True if file exists, False otherwise
        """
        return pathlib.Path(os.path.join(MONKEYS_PATH, f'{name}.yaml')).exists()

    if given_monkey_name is None:
        if default_monkey and monkey_exists(default_monkey):
            print_t(f"No monkey name provided. Loading default monkey config from {default_monkey}...", 'monkey')
            monkey_name = default_monkey
        else:
            monkey_name = select_monkey_from_list()
    elif not monkey_exists(given_monkey_name):
        print_t("Provided monkey name does not correspond to an existing configuration. Please select an existing "
                "monkey:", 'important')
        monkey_name = select_monkey_from_list()
    else:
        monkey_name = given_monkey_name

    monkey_config_file = os.path.join(MONKEYS_PATH, f'{monkey_name}.yaml')
    return monkey_name, monkey_config_file
