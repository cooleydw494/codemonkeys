from termcolor import colored

"""
This "module" simplifies importing user-extendable config classes within core framework code.
For a CodeMonkeys project codebase, it is best to import the extended classes directly.

"""

try:
    from config.framework.env import Env
except ImportError:
    print(colored('Could not import user Env class from config.framework.env. Using default Env class.', 'red'))
    from codemonkeys.config.env import Env
