import glob
import os
import pathlib
from typing import List, Tuple

from defs import MONKEYS_PATH
from codemonkeys.utils.monk.theme_functions import print_t, input_t


def list_monkeys() -> List[str]:
    """ List all monkey configs.
    :return: A list of monkey names """
    file_paths = glob.glob(os.path.join(MONKEYS_PATH, '*.yaml'))
    return [os.path.splitext(os.path.basename(file))[0] for file in file_paths]


def get_monkey_name(given_monkey_name: str = None, prompt_user: bool = False) -> Tuple[str, str]:
    """ Retrieve the monkey name and corresponding config path.
    :param prompt_user: Whether or not to prompt the user
    :param given_monkey_name: A given monkey name
    :return: A tuple consisting of monkey name and its configuration file path """

    def select_monkey_from_list() -> str:
        """ Lists all monkeys and lets user select one.
        :return: Selected monkey name """

        print_t("Please select from the available monkeys:", 'warning')
        monkeys = list_monkeys()
        for idx, monkey in enumerate(monkeys, start=1):
            print_t(f"{idx}. {monkey}", 'option')
        monkey_index = int(input_t("Enter the number of the monkey")) - 1
        return monkeys[monkey_index]

    def monkey_exists(name: str) -> bool:
        """ Checks if a generated monkey config exists.
        :param name: Monkey name
        :return: True if a generated config exists, False otherwise
        """
        return pathlib.Path(os.path.join(MONKEYS_PATH, f'{name}.yaml')).exists()

    if given_monkey_name is None:
        if monkey_exists('default') and not prompt_user:
            print_t(f"No monkey name provided. Loading default monkey config...", 'monkey')
            monkey_name = 'default'
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
