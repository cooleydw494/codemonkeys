import glob
import os
from typing import List

from pandas.io.common import file_exists

from codemonkeys.defs import MONKEYS_PATH
from codemonkeys.utils.monk.theme_functions import print_t, input_t


def list_monkeys() -> List[str]:
    """
    Lists all monkey configs.

    :return List[str]: A list of monkey config names.
    """
    file_paths = glob.glob(os.path.join(MONKEYS_PATH, '*.yaml'))
    return [os.path.splitext(os.path.basename(file))[0] for file in file_paths]


def _select_monkey_from_list() -> str:
    """
    Lists all monkeys and prompts user to select one.

    :return str: Selected monkey name
    """
    print_t("Please select from the available monkeys:", 'warning')
    monkeys = list_monkeys()
    for idx, monkey in enumerate(monkeys, start=1):
        print_t(f"{idx}. {monkey}", 'option')
    monkey_index = int(input_t("Enter the number of the monkey")) - 1
    return monkeys[monkey_index]


def get_monkey_name(given_monkey_name: str = None) -> str:
    """
    Retrieves the monkey name and corresponding config path.

    :param str given_monkey_name: A given monkey name.
    :return Tuple[str, str]: A tuple consisting of the monkey name and config file path.
    """

    if given_monkey_name is None:
        monkey_name = _select_monkey_from_list()
    elif not file_exists(os.path.join(MONKEYS_PATH, f'{given_monkey_name}.yaml')):
        print_t("Provided monkey name does not correspond to an existing configuration. Please select an existing "
                "monkey:", 'important')
        monkey_name = _select_monkey_from_list()
    else:
        monkey_name = given_monkey_name

    return monkey_name
