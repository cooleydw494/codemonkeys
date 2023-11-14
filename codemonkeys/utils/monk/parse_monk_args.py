from typing import List, Tuple, Dict

from codemonkeys.help.help import run_default_help


def _split_unknown_args(unknown_args: List[str]) -> Tuple[Dict[str, bool], List[str]]:
    """
    Splits unknown args into named/unnamed args.
    
    Takes a list of arguments provided in an unknown format and separates
    them into named arguments (options) and unnamed arguments (positional).
    Named arguments are expected to start with `--` or `-` and may include
    `=` for inline values. Any argument following a named argument is
    considered a value for that argument, unless it also starts with `--` or `-`.

    :param unknown_args: A list of command-line arguments to be split.
    :type unknown_args: List[str]
    :return: A tuple consisting of a dictionary for named arguments and a list
             for unnamed arguments.
    :rtype: Tuple[Dict[str, bool], List[str]]
    """
    from collections import OrderedDict
    unknown_named_args = OrderedDict()
    unknown_unnamed_args = []

    iterator = iter(unknown_args)
    for arg in iterator:
        if arg.startswith('--') or arg.startswith('-'):
            if "=" in arg:
                key, value = arg.split("=", 1)  # Split on the first "="
            else:
                key = arg
                try:
                    value = next(iterator)
                    if value.startswith('--') or value.startswith('-'):
                        unknown_unnamed_args.append(value)
                        value = True
                except StopIteration:
                    value = True
            unknown_named_args[key] = value
        else:
            unknown_unnamed_args.append(arg)

    return unknown_named_args, unknown_unnamed_args


def parse_monk_args():
    """
    Parses the args supplied to the monk command.

    Interprets arguments given to the 'monk' CLI command by first using argparse
    to identify action and entity type flags, then processes any remaining known
    and unknown arguments. Unknown arguments are handled by _split_unknown_args
    to separate them into named and unnamed arguments.

    :return: A tuple containing the dictionaries and lists of named and unnamed
             arguments, the action to perform, the entity name, and the entity type.
    :rtype: Tuple[Dict[str, bool], List[str], str, str, str]
    """
    import argparse

    # Create argument parser - use custom help
    parser = argparse.ArgumentParser(add_help=False)

    # Action flags - mutually exclusive, overrides default of "run"
    action_flags = parser.add_mutually_exclusive_group()
    action_flags.add_argument('-e', '--edit', action='store_true')
    action_flags.add_argument('-h', '--help', action='store_true')

    # Entity Type flags - mutually exclusive, overrides default of "command"
    entity_type_flags = parser.add_mutually_exclusive_group()
    entity_type_flags.add_argument('-a', '--automation', action='store_true')
    entity_type_flags.add_argument('-b', '--barrel', action='store_true')

    # Entity is the name of the command or overridden entity_type
    parser.add_argument('entity_name', nargs='?')

    # Parse Arguments
    monk_args, unknown_args = parser.parse_known_args()

    # Split unknown args into named/unnamed
    named_args, unnamed_args = _split_unknown_args(unknown_args)

    # Action
    action = 'run'
    if monk_args.edit is True:
        action = 'edit'

    # Entity Type
    entity_type = 'command'
    if monk_args.automation is True:
        entity_type = 'automation'
    elif monk_args.barrel is True:
        entity_type = 'barrel'
    elif monk_args.help is True:
        entity_type = 'help'

    if entity_type in ['help', 'command'] and monk_args.entity_name in [None, 'help']:
        run_default_help()

    return named_args, unnamed_args, action, monk_args.entity_name, entity_type
