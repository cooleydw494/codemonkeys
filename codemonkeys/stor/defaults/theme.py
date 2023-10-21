from codemonkeys.config.theme import Theme as Base


class Theme(Base):
    """Theme configuration for the CLI."""

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
