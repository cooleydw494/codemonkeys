import os
import textwrap

from termcolor import colored
from definitions import STORAGE_CUSTOM_PATH


def print_banner():
    with open(os.path.join(STORAGE_CUSTOM_PATH, 'art.txt'), 'r') as f:
        art = f.read()
    print(colored(art, 'white'))

    monkey_emojis = """                🐵    🐵     🐵    🐵    🐵    🐵
                👕 💻 👕     👕 💻 👕    👕 💻 👕
                👖    👖     👖    👖    👖    👖"""
    print(monkey_emojis)
    print("\n\n")


def print_nice(*args, color='white', max_width=80, **kwargs):
    """
    Improved print function that automatically wraps long lines to fit the terminal width.
    """

    # Default values for print() parameters
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", "\n")
    file = kwargs.get("file", None)
    flush = kwargs.get("flush", False)

    # Get terminal width
    terminal_width = min(os.get_terminal_size().columns, max_width)

    # Combine arguments into a single string
    text = sep.join(str(arg) for arg in args)

    # Wrap long lines
    text = "\n".join(textwrap.fill(line, terminal_width) for line in text.split("\n"))

    # Print the result using the standard print() function
    print(colored(text, color), end=end, file=file, flush=flush)


def print_table(table, title=None):
    if title:
        print_nice(title + "\n", color="white", attrs=['bold'])

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
        colored_row = [colored(str(val).ljust(width), 'green' if i == 0 else 'cyan' if i == 1 else 'yellow') for
                       i, (val, width) in enumerate(zip(row, col_widths))]
        print_nice('   '.join(colored_row))

    print_nice("\n\n")


def print_tree(start_dir, exclude_dirs, title=None):
    if title:
        print(colored(title + "\n", 'white', attrs=['bold']))

    print(colored(os.path.basename(start_dir), 'magenta'))

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
            if f.startswith('.'):  # ignore hidden files
                continue

            name = os.path.splitext(f)[0]
            print('{}{}'.format(sub_indent, colored(name, 'green')))

    print("\n\n")
