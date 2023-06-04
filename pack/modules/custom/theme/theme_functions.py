import os
import sys
import textwrap
import re
from math import floor
from termcolor import colored, COLORS

from __init__ import __version__
from definitions import STORAGE_PATH, LIGHT_MODE_ENABLED, KEYWORDS, MAX_TERMINAL_WIDTH
from pack.modules.custom.theme.theme_config import text_themes


def get_theme(theme):
    theme_values = text_themes.get(theme)
    if theme_values:
        prefix = theme_values['pre']
        color = theme_values['light_mode'] if LIGHT_MODE_ENABLED else theme_values['color']
        return True, color, prefix
    return False, None, None


def apply_t(text, theme, include_prefix=False, attrs=None):
    has_theme, color, prefix = get_theme(theme)
    if has_theme:
        if include_prefix:
            text = f"{prefix}{text}"
        text = colored(text, color, attrs=attrs)
    elif theme in COLORS:
        text = colored(text, theme, attrs=attrs)
    return text


def print_t(text, theme=None, attrs=None):
    sub_indent = ''
    if theme:
        text = apply_t(text, theme, include_prefix=True)
        _, __, prefix = get_theme(theme)
        sub_indent = ' ' * len(prefix or '')
    if LIGHT_MODE_ENABLED:
        attrs = attrs if isinstance(attrs, list) else [attrs]
        attrs.append('dark')
    print_nice(text, sub_indent=sub_indent, attrs=attrs)


def input_t(text, input_options=None, theme='input'):
    text = apply_t(text, theme, include_prefix=True)
    if input_options:
        text += f' ( {apply_t(input_options, "magenta")} )' if len(input_options) <= 20\
            else os.linesep + apply_t(' (', 'cyan') + apply_t(input_options, "option") + apply_t(')', 'cyan')
    try:
        input_ = input(f'{text}:{os.linesep}>> ')
    except KeyboardInterrupt:
        print()
        print_t("KeyboardInterrupt", 'yellow')
        sys.exit(1)
    if input_ in ("exit", "quit"):
        print_t("✋ Exiting.", 'done')
        sys.exit(0)
    return input_


def print_nice(*args, sub_indent='', **kwargs):
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

    color_pattern = re.compile(r'(\x1b\[[0-9;]*m)(.*?)(\x1b\[0m)', re.DOTALL)

    text = color_pattern.sub(lambda m: m.group(1) + apply_bold_to_keywords(m.group(2)) + m.group(3), text)

    print(text, end=end, file=file, flush=flush)


def apply_bold_to_keywords(text):
    return re.sub(fr"(?i)\b{'|'.join(KEYWORDS)}\b", r'\033[1m\g<0>\033[22m', text)


def strip_color_and_bold_codes(s):
    return re.sub(r'\x1b\[[0-9;]*m', '', s)


def print_banner():
    with open(os.path.join(STORAGE_PATH, 'monk', 'art.txt'), 'r') as f:
        art = f.read()
    print_t(art.replace('vX.X.X', f'v{__version__}'), 'light_yellow')
    print()


def print_table(table, title=None, sub_indent='   ', min_col_width=None):
    terminal_width = min(os.get_terminal_size().columns, MAX_TERMINAL_WIDTH)
    terminal_width -= len(sub_indent)

    if title:
        print_t(title, 'special')

    if not isinstance(min_col_width, list):
        min_col_width = [min_col_width] * len(table["headers"])

    raw_col_widths = [max(len(str(x)) for x in col) for col in zip(*table["rows"])]
    raw_col_widths = [max(width, min_width) for width, min_width in zip(raw_col_widths, min_col_width)]

    col_widths = [min(width + 2, floor((terminal_width - len(table["headers"]) + 1) / len(table["headers"]))) for width in raw_col_widths]
    col_widths = [min(width, raw_width + 2) for width, raw_width in zip(col_widths, raw_col_widths)]

    if table["show_headers"]:
        header = ''.join([apply_t(name.ljust(width), 'magenta') for name, width in zip(table["headers"], col_widths)])
        print_t(sub_indent + header, 'yellow')
        print_t(sub_indent + '-' * len(header), 'magenta')

    for row in table["rows"]:
        colored_row = [apply_t(str(val).ljust(width), 'cyan' if i == 0 else 'green' if i == 1 else 'dark_grey')
                       for i, (val, width) in enumerate(zip(row, col_widths))]
        print_t(sub_indent + ''.join(colored_row))
    print()


def print_tree(start_dir, exclude_dirs, title=None):
    if title:
        print_t(title, 'white', attrs=['bold'])

    for root, dirs, files in os.walk(start_dir):
        dirs[:] = [d for d in dirs if not d[0] in ['.', '_']]

        relative_root = os.path.relpath(root, start_dir)
        if relative_root in exclude_dirs:
            continue

        if relative_root != ".":
            level = relative_root.count(os.sep) + 1
            print('{}{}'.format(' ' * 4 * level, apply_t(os.path.basename(root), 'magenta')))

        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            if not f.startswith('.') and not f.startswith('_'):
                print('{}{}'.format(sub_indent, apply_t(os.path.splitext(f)[0], 'green')))
