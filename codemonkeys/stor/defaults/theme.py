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
        'entity types', 'defs.py', 'CodeMonkeys', 'automations', 'action flags', 'entity type',
        'barrels', 'modules', 'commands', 'monkeys', 'actions', 'barrel', 'module', 'action flag', 'automation',
        'command', 'monkey', 'types', 'cli', 'monk'
    ]

    text_themes: dict = {

        'start': {'color': 'light_green', 'light_mode': 'green', 'pre': '🚀 '},
        'done': {'color': 'light_green', 'light_mode': 'green', 'pre': '✅ '},

        'warning': {'color': 'red', 'light_mode': 'light_red', 'pre': '⚠️  '},
        'error': {'color': 'light_red', 'light_mode': 'light_red', 'pre': '❌ '},

        'super_important': {'color': 'light_magenta', 'light_mode': 'magenta', 'pre': ''},
        'important': {'color': 'light_yellow', 'light_mode': 'magenta', 'pre': '👉 '},
        'special': {'color': 'magenta', 'light_mode': 'magenta', 'pre': ''},
        'loading': {'color': 'yellow', 'light_mode': 'magenta', 'pre': '⏳ '},
        'monkey': {'color': 'light_yellow', 'light_mode': 'magenta', 'pre': '🐒 '},

        'file': {'color': 'dark_grey', 'light_mode': 'black', 'pre': ''},

        'tip': {'color': 'light_cyan', 'light_mode': 'blue', 'pre': '💡 '},
        'info': {'color': 'cyan', 'light_mode': 'blue', 'pre': '🔹 '},
        'option': {'color': 'white', 'light_mode': 'black', 'pre': ''},

        'input': {'color': 'light_cyan', 'light_mode': 'blue', 'pre': '⌨️  '},
        'quiet': {'color': 'dark_grey', 'light_mode': 'black', 'pre': ''},

        # All termcolor colors are also defined, inserted in the base class constructor

    }
