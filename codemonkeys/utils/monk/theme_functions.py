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
from typing import List, Tuple, Union, Optional

from termcolor import colored, COLORS

from codemonkeys.cm_paths import VERSION, CM_BANNER_PATH
from codemonkeys.defs import nl
from codemonkeys.types import OStr
from codemonkeys.utils.imports.theme import Theme
from codemonkeys.utils.misc.file_ops import get_file_contents

_print_lock = threading.Lock()


def verbose_logs_enabled() -> bool:
    return Theme.verbose_logs_enabled


def get_theme(theme: str) -> Tuple[bool, Union[None, str], Union[None, str]]:
    """
    Retrieves the color code and prefix for the specified theme,
    or None if the theme does not exist.
    """
    text_themes = Theme.text_themes
    theme_values = text_themes.get(theme)
    if theme_values:
        prefix = theme_values['pre']
        color = theme_values['light_mode'] if Theme.light_mode_enabled else theme_values['color']
        return True, color, prefix
    return False, None, None


def apply_t(text: str, theme: str, incl_prefix: bool = False, attrs: Optional[List[str]] = None) -> str:
    """
    Applies the specified theme to the given text and returns the themed text.
    """
    has_theme, color, prefix = get_theme(theme)
    if has_theme:
        if incl_prefix:
            text = f"{prefix}{text}"
        text = colored(text, color, attrs=attrs)
    elif theme in COLORS:
        text = colored(text, theme, attrs=attrs)
    return text


def print_t(text: str, theme: OStr = None, incl_prefix: bool = True, verbose: bool = False, not_verbose: bool = False)\
        -> None:
    """
    Prints the given text with the specified theme applied and optional attributes.
    Can be set to only print whenever verbose logging is enabled.
    """
    if verbose and not Theme.verbose_logs_enabled:
        return
    if not_verbose and Theme.verbose_logs_enabled:
        return
    sub_indent = ''
    if theme:
        text = apply_t(text, theme, incl_prefix=incl_prefix)
        _, __, prefix = get_theme(theme)
        if prefix:
            sub_indent = ' ' * (len(prefix) + 1)
    _print_nice(text, sub_indent=sub_indent)


def input_t(text: str, input_options: OStr = None, theme: str = 'input') -> str:
    """
    Prompts for user input with the given question and options,
    both of which will be presented with the current theme applied.
    """
    text = apply_t(text, theme, incl_prefix=True)
    if input_options:
        text += f' {apply_t(input_options, "magenta")}' if len(input_options) <= 20 \
            else nl + apply_t(input_options, "magenta")
    input_ = input(f'{nl}{text}:{nl}' + apply_t('>> ', 'light_cyan', False, ['blink']))
    if input_ in ("exit", "exit()", "quit"):
        print_t("✋ Exiting.", 'done')
        sys.exit(0)
    return input_


def _print_nice(*args, sub_indent: str = '') -> None:
    """
    Internal function to print the given texts (args) with improved indentation and line wrapping.
    Subsequent lines will be indented according to the sub_indent parameter.
    """

    text = " ".join(str(arg) for arg in args)

    terminal_width = min(os.get_terminal_size().columns, Theme.max_terminal_width)
    if len(_strip_color_and_bold_codes(text)) > terminal_width:
        text = nl.join(
            textwrap.fill(line, terminal_width, subsequent_indent=sub_indent)
            for i, line in enumerate(text.split(nl))
        )

    color_pattern = re.compile(r'(\x1b\[[0-9;]*m)(.*?)(\x1b\[0m)', re.DOTALL)

    text = color_pattern.sub(lambda m: m.group(1) + _apply_bold_to_keywords(m.group(2)) + m.group(3), text)

    with _print_lock:
        print(text, end=nl, file=None, flush=True)


def _apply_bold_to_keywords(text: str) -> str:
    """
    Internal function that applies the bold ANSI escape code to all occurrences of 
    the defined keywords within the text.
    """
    return re.sub(fr"(?i)\b{'|'.join(Theme.keywords)}\b", r'\033[1m\g<0>\033[22m', text)


def _strip_color_and_bold_codes(s: str) -> str:
    """
    Internal function that removes all ANSI escape codes for colors and bold from the string.
    """
    return re.sub(r'\x1b\[[0-9;]*m', '', s)


def calculate_col_widths(headers: List[str], rows: List[List[Union[str, int]]], min_col_widths: List[int],
                         terminal_width: int) -> List[int]:
    raw_col_widths = [max(len(str(x)) for x in col) for col in zip(*rows)]
    raw_col_widths = [max(raw, min_width) for raw, min_width in zip(raw_col_widths, min_col_widths)]
    total_width = sum(raw_col_widths) + len(headers) - 1
    remaining_space = terminal_width - total_width

    return [raw + floor(remaining_space / len(headers)) for raw in raw_col_widths]


def print_table(table: dict, title: str = None, sub_indent: str = '  ', min_col_width: Union[int, List[int]] = 10) -> None:
    terminal_width = min(os.get_terminal_size().columns, 120)  # Replace 120 with your Theme.max_terminal_width
    terminal_width -= len(sub_indent)

    if len(table["headers"]) != len(table["rows"][0]):
        raise ValueError("Mismatch between header and row column count")

    if not isinstance(min_col_width, list):
        min_col_width = [min_col_width] * len(table["headers"])

    col_widths = calculate_col_widths(table["headers"], table["rows"], min_col_width, terminal_width)

    if title:
        print_t(f'{sub_indent}{title}', 'special')
        print()

    if table.get("show_headers", True):
        header = ''.join([apply_t(h.ljust(w), 'magenta') for h, w in zip(table["headers"], col_widths)])
        print_t(f"{sub_indent}{header}", 'yellow')
        underline_length = sum(col_widths)
        print_t(f"{sub_indent}{'-' * underline_length}", 'magenta')

    for row in table["rows"]:
        row_str = ''.join([apply_t(str(r).ljust(w), 'cyan' if i == 0 else 'green' if i == 1 else 'dark_grey')
                           for i, (r, w) in enumerate(zip(row, col_widths))])
        print_t(f"{sub_indent}{row_str}")


def print_tree(start_dir: str, exclude_dirs: Optional[List[str]] = None, exclude_file_starts: Optional[List[str]] = None,
               title: OStr = None, show_exts: bool = False, incl_prefix: bool = True) -> None:
    """
    Prints the file structure starting from start_dir in a nicely formatted tree-like style.
    Directories and files that should be excluded can be specified as well as a title for the tree.
    """
    if exclude_file_starts is None:
        exclude_file_starts = ['.', '_']
    if exclude_dirs is None:
        exclude_dirs = []

    if title:
        print_t(f'{nl}{title}{nl}', 'yellow', incl_prefix=incl_prefix)

    level = 0

    for root, dirs, files in os.walk(start_dir):
        base_root = os.path.basename(root)

        # Skip excluded directories and their subdirectories
        if base_root in exclude_dirs:
            dirs.clear()
            continue

        # Filter out directories starting with exclude_file_starts
        dirs[:] = [d for d in dirs if d[0] not in exclude_file_starts]

        relative_root = os.path.relpath(root, start_dir)

        if relative_root != ".":
            level = relative_root.count(os.sep) + 1
            dir_color = 'white' if base_root == 'codemonkeys' else 'light_cyan' if base_root == 'usr' else 'magenta'
            _print_nice(f"{' ' * 2 * level}{apply_t(f'{base_root}:', dir_color)}")

        sub_indent = ' ' * 2 * (level + 1)
        for f in files:
            if not any(f.startswith(start) for start in exclude_file_starts):
                filename = f if show_exts else os.path.splitext(f)[0]
                _print_nice(f"{sub_indent}{apply_t(filename, 'green')}")
