import os
import re
import sys
import textwrap
from math import floor

from termcolor import colored, COLORS

from __init__ import __version__
from defs import import_env_class
from defs import CM_STOR_MONK_PATH, nl

ENV = import_env_class()
ENV = ENV()
text_themes = ENV.text_themes
light_mode_enabled = ENV.light_mode_enabled
max_terminal_width = ENV.max_terminal_width
keywords = ENV.keywords


def get_theme(theme):
    theme_values = text_themes.get(theme)
    if theme_values:
        prefix = theme_values['pre']
        color = theme_values['light_mode'] if light_mode_enabled else theme_values['color']
        return True, color, prefix
    return False, None, None


def apply_t(text, theme, incl_prefix=False, attrs=None):
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


def print_t(text, theme=None, incl_prefix=True, attrs=None):
    sub_indent = ''
    if theme:
        text = apply_t(text, theme, incl_prefix=incl_prefix)
        _, __, prefix = get_theme(theme)
        sub_indent = ' ' * (len(prefix) + 1)
    if light_mode_enabled:
        attrs = attrs if isinstance(attrs, list) else [attrs]
        attrs.append('dark')
    print_nice(text, sub_indent=sub_indent, attrs=attrs)


def input_t(text, input_options=None, theme='input'):
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


def print_nice(*args, sub_indent='', **kwargs):
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", nl)
    file = kwargs.get("file", None)
    flush = kwargs.get("flush", False)

    terminal_width = min(os.get_terminal_size().columns, max_terminal_width)

    text = sep.join(str(arg) for arg in args)

    if len(strip_color_and_bold_codes(text)) > terminal_width:
        text = nl.join(
            textwrap.fill(line, terminal_width, subsequent_indent=sub_indent)
            for i, line in enumerate(text.split(nl))
        )

    color_pattern = re.compile(r'(\x1b\[[0-9;]*m)(.*?)(\x1b\[0m)', re.DOTALL)

    text = color_pattern.sub(lambda m: m.group(1) + apply_bold_to_keywords(m.group(2)) + m.group(3), text)

    print(text, end=end, file=file, flush=flush)


def apply_bold_to_keywords(text):
    return re.sub(fr"(?i)\b{'|'.join(keywords)}\b", r'\033[1m\g<0>\033[22m', text)


def strip_color_and_bold_codes(s):
    return re.sub(r'\x1b\[[0-9;]*m', '', s)


def print_banner():
    with open(os.path.join(CM_STOR_MONK_PATH, 'banner.txt'), 'r') as f:
        art = f.read()
    print_t(art.replace('vX.X.X', f'v{__version__}') + nl, 'light_yellow')


def print_table(table, title=None, sub_indent='   ', min_col_width=10):
    terminal_width = min(os.get_terminal_size().columns, max_terminal_width)
    terminal_width -= len(sub_indent)

    if title:
        print_t(title, 'special')

    if not isinstance(min_col_width, list):
        min_col_width = [min_col_width] * len(table["headers"])

    raw_col_widths = [max(len(str(x)) for x in col) for col in zip(*table["rows"])]
    raw_col_widths = [max(width, min_width) for width, min_width in zip(raw_col_widths, min_col_width)]

    col_widths = [min(width + 2, floor((terminal_width - len(table["headers"]) + 1) / len(table["headers"]))) for width
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
    print()


def print_tree(start_dir: str, exclude_dirs=None, exclude_file_starts=None, title: str = None, show_exts=False,
               incl_prefix=True):
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
            print('{}{}'.format(' ' * 2 * level, apply_t(f'{base_root}:', dir_color)))

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

                print('{}{}'.format(sub_indent, apply_t(filename, file_theme)))


