text_themes = {

    # Themes for printing text to the terminal
    # Colors are required and must be termcolor compatible
    # Prefixes can be unset with None
    #

    # Theme       # Color                  # Prefix

    'success':    {'color': 'green',       'pre': None},
    'start':      {'color': 'green',       'pre': '🚀 '},
    'done':       {'color': 'green',       'pre': '✅ '},

    'error':      {'color': 'red',         'pre': '❌ Error: '},
    'warning':    {'color': 'light_red',   'pre': '⚠️ Warning: '},

    'important':  {'color': 'yellow',      'pre': '👉 '},
    'loading':    {'color': 'yellow',      'pre': '⏳ '},
    'monkey':     {'color': 'yellow',      'pre': '🐵 '},
    'file':       {'color': 'yellow',      'pre': '📁 '},

    'tip':        {'color': 'cyan',        'pre': '💡 '},
    'link':       {'color': 'cyan',        'pre': '🔗 '},
    'info':       {'color': 'cyan',        'pre': '🔹 '},
    'option':     {'color': 'cyan',        'pre': '🔘 '},
    'input':      {'color': 'cyan',        'pre': '⌨️ '},

    'special':    {'color': 'magenta',     'pre': '✨ '},
    'config':     {'color': 'magenta',     'pre': '🔧 '},

    'quiet':      {'color': 'dark_grey',  'pre': None},
}
