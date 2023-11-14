class Theme:
    """
    Theme configuration for the CLI.

    This class defines color themes and additional UI settings for the CLI.

    Attributes:
        light_mode_enabled (bool): Flag to enable light mode for better readability.
        max_terminal_width (int): Maximum width allowed for the terminal output.
        verbose_logs_enabled (bool): Enables verbose logging.
        keywords (list): List of keywords to be bolded in CLI prints.
        fallback_colors (dict): Theme-compliant color fallbacks for terminal output.
        text_themes (dict): Dictionary defining the themes for CLI text.

    """

    # Improved readability for psychopaths
    light_mode_enabled: bool = False
    # Looks 👌 with very lil space, but you do you, boo-boo
    max_terminal_width: int = 120
    # Log Verbose Details
    verbose_logs_enabled: bool = False

    # KEYWORDS (bold in CLI prints)
    keywords: list = [
        'CodeMonkeys', 'entity types', 'entity type', 'automations', 'automation', 'action flags', 'action flag',
        'barrels', 'barrel', 'funcs', 'func', 'commands', 'command', 'monkeys', 'monkey', 'monk cli', 'monk'
    ]

    fallback_colors: dict = {

        # Theme-compliant termcolor fallbacks
        'black': {'color': 'black', 'light_mode': 'black', 'pre': ''},
        'red': {'color': 'red', 'light_mode': 'blue', 'pre': ''},
        'green': {'color': 'green', 'light_mode': 'green', 'pre': ''},
        'yellow': {'color': 'yellow', 'light_mode': 'blue', 'pre': ''},
        'blue': {'color': 'blue', 'light_mode': 'blue', 'pre': ''},
        'magenta': {'color': 'magenta', 'light_mode': 'blue', 'pre': ''},
        'cyan': {'color': 'cyan', 'light_mode': 'blue', 'pre': ''},
        'white': {'color': 'white', 'light_mode': 'black', 'pre': ''},
        'light_grey': {'color': 'light_grey', 'light_mode': 'black', 'pre': ''},
        'dark_grey': {'color': 'dark_grey', 'light_mode': 'black', 'pre': ''},
        'light_red': {'color': 'light_red', 'light_mode': 'blue', 'pre': ''},
        'light_green': {'color': 'light_green', 'light_mode': 'green', 'pre': ''},
        'light_yellow': {'color': 'light_yellow', 'light_mode': 'blue', 'pre': ''},
        'light_blue': {'color': 'light_blue', 'light_mode': 'blue', 'pre': ''},
        'light_magenta': {'color': 'light_magenta', 'light_mode': 'blue', 'pre': ''},
        'light_cyan': {'color': 'light_cyan', 'light_mode': 'blue', 'pre': ''},
    }

    text_themes: dict = {

        'start': {'color': 'light_green', 'light_mode': 'green', 'pre': '🚀 '},
        'done': {'color': 'light_green', 'light_mode': 'green', 'pre': '✅ '},

        'warning': {'color': 'red', 'light_mode': 'light_red', 'pre': '⚠️  '},
        'error': {'color': 'light_red', 'light_mode': 'light_red', 'pre': '❌ '},

        'super_important': {'color': 'light_yellow', 'light_mode': 'magenta', 'pre': '👀 '},
        'important': {'color': 'light_yellow', 'light_mode': 'magenta', 'pre': '👉 '},
        'special': {'color': 'light_magenta', 'light_mode': 'magenta', 'pre': ''},
        'loading': {'color': 'yellow', 'light_mode': 'magenta', 'pre': '⏳ '},

        'info': {'color': 'cyan', 'light_mode': 'blue', 'pre': '🔹 '},

        'input': {'color': 'light_cyan', 'light_mode': 'blue', 'pre': '⌨️  '},
        'quiet': {'color': 'dark_grey', 'light_mode': 'black', 'pre': ''},

        # All termcolor colors are also defined, inserted in the base class constructor
    }

    def __init__(self):
        self.text_themes.update(self.fallback_colors)
