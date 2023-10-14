from termcolor import colored

"""
This "module" simplifies importing a user-extendable class within core framework code.
For a CodeMonkeys project codebase, it is best to import the extended class directly.

"""

try:
    from config.theme import Theme
except ImportError as e:
    print(colored('Warning: Could not import user Theme class from config.theme. Using default Theme class.', 'red'))
    # Cannot use handle_exception here, or check for verbose_logs_enabled
    # We'll just not print anything here and allow the default Theme class to be used with simple warnings
    from codemonkeys.config.theme import Theme
