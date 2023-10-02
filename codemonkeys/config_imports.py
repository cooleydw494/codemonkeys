from codemonkeys.utils.monk.theme_functions import print_t

"""
This "module" simplifies importing user-extendable config classes within core framework code.
For a CodeMonkeys project codebase, it is best to import the extended classes directly.
"""

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

try:
    from config.framework.theme import Theme
except ImportError:
    print('Could not import user Theme class from config.framework.theme. Using default Theme class.')
    from codemonkeys.config.theme import Theme
