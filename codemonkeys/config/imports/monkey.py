from termcolor import colored

"""
This "module" simplifies importing a user-extendable class within core framework code.
For a CodeMonkeys project codebase, it is best to import the extended class directly.

"""

try:
    from config.monkeys.monkey import Monkey
except ImportError:
    print(colored('Could not import user Monkey class from config.monkeys.monkey. Using default '
                  'Monkey class. automation', 'red'))
    from codemonkeys.config.monkey import Monkey
