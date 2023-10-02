from termcolor import colored

"""
This "module" simplifies importing a user-extendable class within core framework code.
For a CodeMonkeys project codebase, it is best to import the extended class directly.

"""

try:
    from config.framework.monkey_config import MonkeyConfig
except ImportError:
    print(colored('Could not import user MonkeyConfig class from config.framework.monkey_config. Using default '
                  'MonkeyConfig class. automation', 'red'))
    from codemonkeys.config.monkey_config import MonkeyConfig
