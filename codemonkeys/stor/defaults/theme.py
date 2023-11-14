from codemonkeys.config.theme import Theme as Base


class Theme(Base):
    """
    Theme configuration for the CLI.

    This class provides settings for the visual theme of the CLI including color schemes,
    keyword highlighting, and layout parameters. It allows for customization of the
    CLI appearance to improve readability and differentiate types of output.

    Attributes:
        light_mode_enabled (bool): If set to true, enables the light color mode for
            improved readability. Defaults to False.
        max_terminal_width (int): The maximum width of the terminal output to prevent
            overly wide text. Defaults to 120.
        verbose_logs_enabled (bool): If set to True, enables verbose logging details.
            Defaults to False.
        keywords (list[str]): A list of keywords that will be highlighted in CLI output.
        text_themes (dict): A dictionary mapping theme names to their styling
            configurations such as color, light mode color, and prefixes.
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
