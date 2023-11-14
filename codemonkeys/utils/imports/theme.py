from termcolor import colored

"""
This module acts as a bridge for importing a user-extendable theme class within the CodeMonkeys framework.
It attempts to import the extended Theme class from the user's config.theme module. If it fails to import due to
an ImportError, it falls back to using the default Theme class provided by the framework itself.

The Theme class is responsible for theming and coloring the printed output in the terminal, and users can
customize this by extending the Theme class with their own theme configurations.
"""

try:
    from config.theme import Theme
except ImportError as e:
    print(colored('Warning: Could not import user Theme class from config.theme. Using default Theme class.', 'red'))
    # Cannot use handle_exception here, or check for verbose_logs_enabled
    # We'll just not print anything here and allow the default Theme class to be used with simple warnings
    from codemonkeys.config.theme import Theme
