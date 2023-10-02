from codemonkeys.utils.monk.theme_functions import print_t

try:
    from config.framework.env import Env
except ImportError:
    print_t('Could not import user Env class from config.framework.env. Using default Env class.', 'warning')
    from codemonkeys.config.env import Env

try:
    from config.framework.monkey_config import MonkeyConfig
except ImportError:
    print_t('Could not import user MonkeyConfig class from config.framework.monkey_config. Using default '
            'MonkeyConfig class. automation', 'warning')
    from codemonkeys.config.monkey_config import MonkeyConfig
