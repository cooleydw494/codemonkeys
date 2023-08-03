from codemonkeys.utils.monk.get_monkey_name import get_monkey_name
from codemonkeys.utils.monk.theme_functions import print_t

try:
    from config.framework.monkey_config import MonkeyConfig
except ImportError:
    print_t('Could not import user MonkeyConfig class from config.framework.monkey_config. Using default '
            'MonkeyConfig class. load_monkey_config', 'warning')
    from codemonkeys.config.monkey_config import MonkeyConfig


def load_monkey_config(monkey_name: str | None = None) -> MonkeyConfig:
    """
    Get `MonkeyConfig` for a given monkey config name, or prompt user to select if None is provided.

    :param str | None monkey_name: Optional; to load specified monkey config without user input.
    :return: Instance of the `MonkeyConfig` class.
    """
    if monkey_name is None:
        monkey_name, _ = get_monkey_name()

    return MonkeyConfig.load(monkey_name)
