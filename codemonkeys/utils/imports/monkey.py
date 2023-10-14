from termcolor import colored

from codemonkeys.utils.misc.handle_exception import handle_exception

"""
This "module" simplifies importing a user-extendable class within core framework code.
For a CodeMonkeys project codebase, it is best to import the extended class directly.

"""

try:
    from monkeys.monkey import Monkey
except ImportError as e:
    print(colored('Could not import user Monkey class from monkeys.monkey. Using default Monkey class.', 'red'))
    handle_exception(e, always_continue=True)
    from codemonkeys.entities.monkey import Monkey

OMonkey = Monkey | None
