from termcolor import colored

from codemonkeys.utils.misc.handle_exception import handle_exception

"""
This "module" simplifies importing user-extendable config classes within core framework code.
For a CodeMonkeys project codebase, it is best to import the extended classes directly.

"""

try:
    from config.env import Env
except ImportError as e:
    print(colored('Warning: Could not import user Env class from config.env. Using default Env class.', 'red'))
    handle_exception(e, always_continue=True)
    from codemonkeys.config.env import Env
