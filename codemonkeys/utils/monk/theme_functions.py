"""
This module contains various functions that provide themes and print styles for terminal.
This includes applying colors and themes to text, handling text input and output with respect to themes,
printing stylized tables and trees, and ensuring that the written output fits nicely into the terminal.
"""
import os
import re
import sys
import textwrap
import threading
from math import floor
from typing import List, Tuple, Union

from termcolor import colored, COLORS

from codemonkeys.cmdefs import VERSION, CM_STOR_SNIPPETS_PATH
from codemonkeys.defs import nl

try:
    from config.framework.env_class import Env
except ImportError:
    print('Could not import user Env class from config.framework.env_class. Using default Env class.')
    from codemonkeys.config.env_class import Env

env = Env.get()
text_themes = env.text_themes
light_mode_enabled = env.light_mode_enabled
verbose_logs = env.verbose_logs_enabled
max_terminal_width = env.max_terminal_width
keywords = env.keywords

print_lock = threading.Lock()
terminal_width = min(os.get_terminal_size().columns, max_terminal_width)


def get_theme(theme: str) -> Tuple[bool, Union[None, str], Union[None, str]]:
    """
    Retrieves the color code and prefix for the specified theme,
    or None if the theme does not exist.
    """
    theme_values = text_themes.get(theme)
    if theme_values:
        prefix = theme_values['pre']
        color = theme_values['light_mode'] if light_mode_enabled else theme_values['color']
        return True, color, prefix
    return False, None, None


def apply_t(text: str, theme: str, incl_prefix: bool = False, attrs: Union[None, List[str]] = None) -> str:
    """
    Applies the specified theme to the given text and returns the themed text.
    """
    has_theme, color, prefix = get_theme(theme)
    if has_theme:
        if theme == 'super_important':
            attrs = attrs if isinstance(attrs, list) else []
            attrs.append('blink')
        if incl_prefix:
            text = f"{prefix}{text}"
        text = colored(text, color, attrs=attrs)
    elif theme in COLORS:
        text = colored(text, theme, attrs=attrs)
    return text


def print_t(text: str, theme: str = None, incl_prefix: bool = True, attrs: Union[None, List[str]] = None,
            verbose: bool = False) -> None:
    """
    Prints the given text with the specified theme applied and optional attributes.
    Can be set to only print whenever verbose logging is enabled.
    """
    if verbose and not verbose_logs:
        return
    sub_indent = ''
    if theme:
        text = apply_t(text, theme, incl_prefix=incl_prefix)
        _, __, prefix = get_theme(theme)
        sub_indent = ' ' * (len(prefix) + 1)
    if light_mode_enabled:
        attrs = attrs if isinstance(attrs, list) else [attrs]
        attrs.append('dark')
    _print_nice(text, sub_indent=sub_indent, attrs=attrs)


def input_t(text: str, input_options: str = None, theme: str = 'input') -> str:
    """
    Prompts for user input with the given question and options,
    both of which will be presented with the current theme applied.
    """
    text = apply_t(text, theme, incl_prefix=True)
    if input_options:
        text += f' {apply_t(input_options, "magenta")}' if len(input_options) <= 20 \
            else nl + apply_t(input_options, "magenta")
    try:
        input_ = input(f'{nl}{text}:{nl}' + apply_t('>> ', 'light_cyan', False, ['blink']))
    except KeyboardInterrupt:
        print_t(f"{nl}KeyboardInterrupt", 'yellow')
        sys.exit(1)
    if input_ in ("exit", "exit()", "quit"):
        print_t("✋ Exiting.", 'done')
        sys.exit(0)
    return input_


def _print_nice(*args, sub_indent: str = '', **kwargs) -> None:
    """
    Internal function to print the given texts (args) with improved indentation and line wrapping.
    Subsequent lines will be indented according to the sub_indent parameter.
    """
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", nl)
    file = kwargs.get("file", None)
    flush = kwargs.get("flush", False)

    text = sep.join(str(arg) for arg in args)

    if len(_strip_color_and_bold_codes(text)) > terminal_width:
        text = nl.join(
            textwrap.fill(line, terminal_width, subsequent_indent=sub_indent)
            for i, line in enumerate(text.split(nl))
        )

    color_pattern = re.compile(r'(\x1b\[[0-9;]*m)(.*?)(\x1b\[0m)', re.DOTALL)

    text = color_pattern.sub(lambda m: m.group(1) + _apply_bold_to_keywords(m.group(2)) + m.group(3), text)

    with print_lock:
        print(text, end=end, file=file, flush=flush)


def _apply_bold_to_keywords(text: str) -> str:
    """
    Internal function that applies the bold ANSI escape code to all occurrences of 
    the defined keywords within the text.
    """
    return re.sub(fr"(?i)\b{'|'.join(keywords)}\b", r'\033[1m\g<0>\033[22m', text)


def _strip_color_and_bold_codes(s: str) -> str:
    """
    Internal function that removes all ANSI escape codes for colors and bold from the string.
    """
    return re.sub(r'\x1b\[[0-9;]*m', '', s)


def print_banner() -> None:
    """
    Prints "banner.txt", the banner of this project.
    """
    with open(os.path.join(CM_STOR_SNIPPETS_PATH, 'banner.txt'), 'r') as f:
        art = f.read()
    print_t(art.replace('vX.X.X', f'v{VERSION}') + nl, 'light_yellow')


def print_table(table: dict, title: str = None, sub_indent: str = '   ',
                min_col_width: Union[int, List[int]] = 10) -> None:
    """
    Prints the given table in a nicely formatted manner within the terminal,
    with the specified title and minimum column widths.
    """
    t_width = terminal_width - len(sub_indent)

    if title:
        print_t(title, 'special')

    if not isinstance(min_col_width, list):
        min_col_width = [min_col_width] * len(table["headers"])

    raw_col_widths = [max(len(str(x)) for x in col) for col in zip(*table["rows"])]
    raw_col_widths = [max(width, min_width) for width, min_width in zip(raw_col_widths, min_col_width)]

    col_widths = [min(width + 2, floor((t_width - len(table["headers"]) + 1) / len(table["headers"]))) for width
                  in raw_col_widths]
    col_widths = [min(width, raw_width + 2) for width, raw_width in zip(col_widths, raw_col_widths)]

    if table["show_headers"]:
        header = ''.join([apply_t(name.ljust(width), 'magenta') for name, width in zip(table["headers"], col_widths)])
        print_t(sub_indent + header, 'yellow')
        print_t(sub_indent + '-' * len(header), 'magenta')

    for row in table["rows"]:
        colored_row = [apply_t(str(val).ljust(width), 'cyan' if i == 0 else 'green' if i == 1 else 'dark_grey')
                       for i, (val, width) in enumerate(zip(row, col_widths))]
        print_t(sub_indent + ''.join(colored_row))
    _print_nice()


def print_tree(start_dir: str, exclude_dirs: List[str] = None, exclude_file_starts:
               List[str] = None, title: str = None, show_exts: bool = False, incl_prefix: bool = True) -> None:
    """
    Prints the file structure starting from start_dir in a nicely formatted tree-like style.
    directories and files that should be excluded can be specified as well as a title for the tree.
    """
    if exclude_file_starts is None:
        exclude_file_starts = ['.', '_']
    if exclude_dirs is None:
        exclude_dirs = []

    if title:
        print_t(f'{nl}{title}{nl}', 'yellow', attrs=['bold'], incl_prefix=incl_prefix)

    level = 0
    within_excluded_dir = False

    for root, dirs, files in os.walk(start_dir):
        base_root = os.path.basename(root)
        # If the current directory is in the exclude list, skip it and its subdirectories
        if base_root in exclude_dirs:
            within_excluded_dir = True
            dirs[:] = []  # This will prevent os.walk from visiting the subdirectories
            continue
        # If we're currently within an excluded directory, skip this iteration
        elif within_excluded_dir:
            continue
        else:
            within_excluded_dir = False  # We're no longer within an excluded directory

        dirs[:] = [d for d in dirs if d[0] not in exclude_file_starts]

        relative_root = os.path.relpath(root, start_dir)

        if relative_root != ".":
            level = relative_root.count(os.sep) + 1
            dir_color = 'magenta'
            if base_root == 'codemonkeys':
                dir_color = 'white'
            elif base_root == 'usr':
                dir_color = 'light_cyan'
            _print_nice('{}{}'.format(' ' * 2 * level, apply_t(f'{base_root}:', dir_color)))

        sub_indent = ' ' * 2 * (level + 1)
        for f in files:
            if not any(f.startswith(start) for start in exclude_file_starts):
                without_ext = os.path.splitext(f)[0]
                filename = f if show_exts else without_ext
                if f.endswith('.py'):
                    file_theme = 'green'
                elif f.endswith('.md'):
                    file_theme = 'light_blue'
                elif f.endswith('.yaml'):
                    file_theme = 'yellow'
                elif f == 'monk':
                    file_theme = 'light_yellow'
                elif f == 'c':
                    continue
                else:
                    file_theme = 'cyan'

                _print_nice('{}{}'.format(sub_indent, apply_t(filename, file_theme)))
