from termcolor import colored

from codemonkeys.utils.misc.handle_exception import handle_exception

"""
This module acts as a bridge for importing the user-extended Monkey class that may contain project-specific
configurations and logic. In core framework code where user extension is expected, this module will import
the extended class directly if available. On import failure, the default Monkey class from the codemonkeys
package is used instead.
"""

try:
    from monkeys.monkey import Monkey
except ImportError as e:
    print(colored('Could not import user Monkey class from monkeys.monkey. Using default Monkey class.', 'red'))
    handle_exception(e, always_continue=True)
    from codemonkeys.entities.monkey import Monkey

OMonkey = Monkey | None
