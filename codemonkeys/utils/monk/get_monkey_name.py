import glob
import os
from typing import List

from pandas.io.common import file_exists

from codemonkeys.defs import MONKEYS_PATH
from codemonkeys.types import OStr
from codemonkeys.utils.monk.theme_functions import print_t, input_t


def list_monkeys() -> List[str]:
    """
    Lists all Monkey configs.

    :return List[str]: A list of Monkey config names.
    """
    file_paths = glob.glob(os.path.join(MONKEYS_PATH, '*.py'))
    return [os.path.splitext(os.path.basename(file))[0] for file in file_paths]


def _select_monkey_from_list() -> str:
    """
    Lists all monkeys and prompts user to select one.

    :return str: Selected Monkey name
    """
    print_t("Please select from the available monkeys:", 'warning')
    monkeys = list_monkeys()
    for idx, monkey in enumerate(monkeys, start=1):
        print_t(f"{idx}. {monkey}", 'option')
    monkey_index = int(input_t("Enter the number of the monkey")) - 1
    return monkeys[monkey_index]


def get_monkey_name(given_monkey_name: OStr = None) -> str:
    """
    Retrieves the Monkey name and corresponding config path.

    :param str given_monkey_name: A given Monkey name.
    :return Tuple[str, str]: A tuple consisting of the Monkey name and config file path.
    """

    if given_monkey_name is None:
        monkey_name = _select_monkey_from_list()
    elif not file_exists(os.path.join(MONKEYS_PATH, f'{given_monkey_name}.py')):
        print_t("Monkey does not exist. Please select an existing monkey:", 'important')
        monkey_name = _select_monkey_from_list()
    else:
        monkey_name = given_monkey_name

    return monkey_name
