from termcolor import colored

"""
This "module" simplifies importing a user-extendable class within core framework code.
For a CodeMonkeys project codebase, it is best to import the extended class directly.

"""

try:
    from config.theme import Theme
except ImportError:
    print(colored('Could not import user Theme class from config.theme. Using default Theme class.', 'red'))
    from codemonkeys.config.theme import Theme
