import os
import sys
import textwrap
import re
from math import floor

# from art import text2art
from termcolor import colored, COLORS, ATTRIBUTES

from __init__ import __version__
from definitions import STORAGE_INTERNAL_PATH
from pack.modules.custom.theme.theme_config import text_themes

MAX_TERMINAL_WIDTH = 120
KEYWORDS = ['pseudo-package', 'entity types', 'definitions.py', 'CodeMonkeys', 'automations', 'action flags',
            'entity type', 'barrels', 'modules', 'commands', 'monkeys', 'actions', 'barrel', 'module', 'action flag',
            'automation', 'command', 'monkey', 'types', 'pack', 'cli', 'monk']

# Sort the keywords by their lengths in descending order to avoid partial boldness
KEYWORDS.sort(key=len, reverse=True)


def get_theme(theme):
    has_theme = theme in text_themes.keys()
    if has_theme:
        prefix = text_themes[theme]['pre']
        color = text_themes[theme]['color']
        return has_theme, color, prefix
    else:
        return False, None, None


def apply_theme(text, theme):
    # Apply theme (if any)
    has_theme, color, prefix = get_theme(theme)
    if has_theme:
        text = f"{prefix}{text}"
        text = colored(text, color)
    # Fallback for color strings
    elif theme in COLORS.keys():
        text = colored(text, theme)
    return text


def print_t(text, theme=None, attrs=None):
    sub_indent = ''
    if theme:
        text = apply_theme(text, theme)
        _, __, prefix = get_theme(theme)
        sub_indent = ' ' * len(f'{prefix} ' or '')
    print_nice(text, sub_indent=sub_indent, attrs=attrs)


def input_t(text, input_options=None, theme='input'):
    text = apply_theme(text, theme)
    # if input_options is longer than 10 characters, print it on a new line
    if input_options:
        if len(input_options) > 16:
            new_line_maybe = os.linesep
        else:
            new_line_maybe = ''
        text = text + new_line_maybe + colored(' - ', 'cyan') + colored(input_options, "yellow")
    try:

        result = input(f'{text}{colored(":", "cyan")}{os.linesep + os.linesep}{colored(">> ", "cyan", attrs=["blink"])}')
    except KeyboardInterrupt:
        print()
        print_t("Exiting due to KeyboardInterrupt from user.", 'yellow')
        sys.exit(1)
    return result


def print_nice(*args, sub_indent='', no_keywords=False, **kwargs):
    """
    Improved print function that automatically wraps long lines to fit the terminal width.
    """
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", os.linesep)
    file = kwargs.get("file", None)
    flush = kwargs.get("flush", False)

    terminal_width = min(os.get_terminal_size().columns, MAX_TERMINAL_WIDTH)

    text = sep.join(str(arg) for arg in args)

    if len(strip_color_and_bold_codes(text)) > terminal_width:
        text = os.linesep.join(
            textwrap.fill(line, terminal_width, subsequent_indent=sub_indent)
            for i, line in enumerate(text.split(os.linesep))
        )

    # This pattern matches colored text.
    color_pattern = re.compile(r'(\x1b\[[0-9;]*m)(.*?)(\x1b\[0m)', re.DOTALL)

    def bold_colored_text(match):
        """Returns the colored text with bold attribute."""
        color_start = match.group(1)
        colored_text = match.group(2)
        color_end = match.group(3)

        for keyword in KEYWORDS:
            keyword_pattern = fr"(?i)\b{keyword}\b"  # case-insensitive match whole word
            colored_text = re.sub(keyword_pattern, '\033[1m' + r'\g<0>' + '\033[22m', colored_text)

        return color_start + colored_text + color_end

    text = color_pattern.sub(bold_colored_text, text)

    print(text, end=end, file=file, flush=flush)


def strip_color_and_bold_codes(s):
    return re.sub(r'\x1b\[[0-9;]*m', '', s)


def print_banner():
    with open(os.path.join(STORAGE_INTERNAL_PATH, 'monk', 'art.txt'), 'r') as f:
        art = f.read()

    art = art.replace('vX.X.X', f'v{__version__}')
    print_t(art, 'yellow')
    print()


def print_table(table, title=None, sub_indent='   ', min_col_width=None):
    import os

    terminal_width = min(os.get_terminal_size().columns, MAX_TERMINAL_WIDTH)
    terminal_width -= len(sub_indent)  # Adjust for indentation

    if title:
        print_t(title)

    if not isinstance(min_col_width, list):
        min_col_width = [min_col_width] * len(table["headers"])

    raw_col_widths = [max(len(str(x)) for x in col) for col in zip(*table["rows"])]
    raw_col_widths = [max(width, min_width) for width, min_width in zip(raw_col_widths, min_col_width)]

    col_widths = [min(width + 2, floor((terminal_width - len(table["headers"]) + 1) / len(table["headers"]))) for width in raw_col_widths]
    col_widths = [min(width, raw_width + 2) for width, raw_width in zip(col_widths, raw_col_widths)]

    if table["show_headers"]:
        header = ''.join([colored(name.ljust(width), 'magenta', attrs=['bold']) for name, width in zip(table["headers"], col_widths)])
        print_t(sub_indent + header, 'yellow')
        print_t(sub_indent + '-' * len(header), 'magenta')

    for row in table["rows"]:
        colored_row = [colored(str(val).ljust(width), 'cyan' if i == 0 else 'green' if i == 1 else 'dark_grey') for i, (val, width) in enumerate(zip(row, col_widths))]
        print_t(sub_indent + ''.join(colored_row))
    print()


def print_tree(start_dir, exclude_dirs, title=None):
    if title:
        print_t(title, 'white', attrs=['bold'])

    # print_t(os.path.basename(start_dir), 'magenta')

    for root, dirs, files in os.walk(start_dir):
        dirs[:] = [d for d in dirs if not d[0] in ['.', '_']]  # ignore hidden directories

        relative_root = os.path.relpath(root, start_dir)
        if relative_root in exclude_dirs:
            continue  # skip excluded dir

        # if we're in the start directory, don't indent or print
        if relative_root == ".":
            level = 0
        else:
            level = relative_root.count(os.sep) + 1  # Adding 1 to properly indent subdirectories
            indent = ' ' * 4 * level
            print('{}{}'.format(indent, colored(os.path.basename(root), 'magenta')))

        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            if f.startswith('.') or f.startswith('_'):  # ignore hidden files
                continue

            name = os.path.splitext(f)[0]
            print('{}{}'.format(sub_indent, colored(name, 'green')))
