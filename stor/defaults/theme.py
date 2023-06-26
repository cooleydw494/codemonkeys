"""  PREFERENCES
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  """

# Improved readability for psychopaths
light_mode_enabled: bool = False
# Looks 👌 with very lil space, but you do you, boo-boo
max_terminal_width: int = 120

# KEYWORDS (bold in CLI prints)
keywords: list = [
    'entity types', 'defs.py', 'CodeMonkeys', 'automations', 'action flags', 'entity type',
    'barrels', 'modules', 'commands', 'monkeys', 'actions', 'barrel', 'module', 'action flag', 'automation', 'command',
    'monkey', 'types', 'cli', 'monk']


"""  CLI TEXT THEMES
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  """

text_themes: dict = {
    'start': {'color': 'light_green', 'light_mode': 'green', 'pre': '🚀 '},
    'done': {'color': 'light_green', 'light_mode': 'green', 'pre': '✅ '},

    'warning': {'color': 'red', 'light_mode': 'light_red', 'pre': '⚠️  Warning: '},
    'error': {'color': 'light_red', 'light_mode': 'light_red', 'pre': '❌ Error: '},

    'super_important': {'color': 'light_magenta', 'light_mode': 'magenta', 'pre': ''},
    'important': {'color': 'light_yellow', 'light_mode': 'magenta', 'pre': '👉 '},
    'special': {'color': 'magenta', 'light_mode': 'magenta', 'pre': ''},
    'loading': {'color': 'yellow', 'light_mode': 'magenta', 'pre': '⏳ '},
    'monkey': {'color': 'light_yellow', 'light_mode': 'magenta', 'pre': ''},
    # 'config': {'color': 'yellow', 'light_mode': 'magenta', 'pre': '🔧 '},

    'file': {'color': 'dark_grey', 'light_mode': 'black', 'pre': ''},

    'tip': {'color': 'light_cyan', 'light_mode': 'blue', 'pre': '💡 '},
    'info': {'color': 'cyan', 'light_mode': 'blue', 'pre': '🔹 '},
    'option': {'color': 'white', 'light_mode': 'black', 'pre': ''},

    'input': {'color': 'light_cyan', 'light_mode': 'blue', 'pre': '⌨️  '},
    'quiet': {'color': 'dark_grey', 'light_mode': 'black', 'pre': ''},

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
