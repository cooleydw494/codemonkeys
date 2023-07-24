import os

from codemonkeys.defs import TEMP_PATH
from codemonkeys.utils.monk.get_monkey_name import get_monkey_name
from codemonkeys.utils.monk.theme_functions import print_t, input_t, apply_t

try:
    from config.framework.monkey_config_class import MonkeyConfig
except ImportError:
    print_t('Could not import user MonkeyConfig class from config.framework.monkey_config_class. Using default '
            'MonkeyConfig class. load_monkey_config', 'warning')
    from codemonkeys.config.monkey_config_class import MonkeyConfig


def load_monkey_config(given_monkey_name=None) -> MonkeyConfig:
    loaded_monkey_name = _get_loaded_monkey()
    if loaded_monkey_name is not None and given_monkey_name is None:
        use_current = input_t(f"Continue with loaded monkey: {apply_t(loaded_monkey_name, 'important')}?", '(y/n)')
        if use_current == 'y':
            monkey_name = loaded_monkey_name
        else:
            monkey_name, _ = get_monkey_name(prompt_user=True)
    elif given_monkey_name is not None:
        monkey_name = given_monkey_name
    else:
        print_t("No monkey name or currently loaded monkey.", "quiet")
        monkey_name, _ = get_monkey_name(prompt_user=True)

    _set_loaded_monkey(monkey_name)
    return MonkeyConfig.load(monkey_name=monkey_name)


def _get_loaded_monkey() -> str or None:
    loaded_monkey_name_path = os.path.join(TEMP_PATH, "loaded-monkey-name.txt")
    if not os.path.exists(loaded_monkey_name_path):
        return None
    with open(loaded_monkey_name_path, 'r') as file:
        monkey_name = file.read()
    if monkey_name == '':
        return None
    return monkey_name


def _set_loaded_monkey(given_monkey_name: str) -> None:
    monkey_path = os.path.join(TEMP_PATH, "loaded-monkey-name.txt")
    with open(monkey_path, 'w') as file:
        file.write(given_monkey_name)
