import os
import sys
import textwrap

# from art import text2art
from termcolor import colored, COLORS

from __init__ import __version__
from definitions import STORAGE_INTERNAL_PATH
from pack.modules.custom.theme.theme_config import text_themes


def apply_theme(text, theme):
    # Apply theme (if any)
    has_theme = theme in text_themes.keys()
    if has_theme:
        prefix = text_themes[theme]['pre']
        if prefix is not None:
            text = f"{prefix}{text}"
        color = text_themes[theme]['color']
        text = colored(text, color)
    # Fallback for color strings
    elif theme in COLORS.keys():
        text = colored(text, theme)
    return text


def printc(text, theme=None, attrs=None):
    if theme:
        text = apply_theme(text, theme)
    print_nice(text, attrs=attrs)


def inputc(text, theme='input'):
    text = apply_theme(text, theme)
    try:
        result = input(text)
    except KeyboardInterrupt:
        print()
        printc("Exiting due to KeyboardInterrupt from user.", 'yellow')
        sys.exit(1)
    return result


def print_nice(*args, color=None, max_width=120, **kwargs):
    """
    Improved print function that automatically wraps long lines to fit the terminal width.
    """

    # Default values for print() parameters
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", "\n")
    file = kwargs.get("file", None)
    flush = kwargs.get("flush", False)

    terminal_width = min(os.get_terminal_size().columns, max_width)

    # Combine arguments into a single string
    text = sep.join(str(arg) for arg in args)

    # If the text is short enough, print it as-is
    if len(text) > terminal_width:
        # Wrap long lines
        text = "\n".join(textwrap.fill(line, terminal_width) for line in text.split("\n"))

    if color:  # doesn't apply a default color (text may be pre-colored)
        text = colored(text, color)

    print(text, end=end, file=file, flush=flush)


def print_banner():
    with open(os.path.join(STORAGE_INTERNAL_PATH, 'monk', 'art.txt'), 'r') as f:
        art = f.read()
    printc(art, 'yellow')
    printc(f'Version {__version__}', 'monkey')


def print_table(table, title=None):
    print()
    if title:
        print_nice(title, color="white", attrs=['bold'])

    # Calculate column widths
    col_widths = [max(len(str(x)) for x in col) for col in zip(*table["rows"])]

    # Print headers in bold magenta
    if table["show_headers"]:
        header = '   '.join([colored(name.ljust(width), 'magenta', attrs=['bold']) for name, width in
                             zip(table["headers"], col_widths)])
        print_nice(header)
        print_nice('-' * len(header), color="magenta")

    # Print rows
    for row in table["rows"]:
        # Color the command in green, description in cyan, and note in yellow
        colored_row = [colored(str(val).ljust(width), 'cyan' if i == 0 else 'green' if i == 1 else 'light_grey') for
                       i, (val, width) in enumerate(zip(row, col_widths))]
        print_nice('   '.join(colored_row))

    print()


def print_tree(start_dir, exclude_dirs, title=None):
    if title:
        printc(title, 'white', attrs=['bold'])

    printc(os.path.basename(start_dir), 'magenta')

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
