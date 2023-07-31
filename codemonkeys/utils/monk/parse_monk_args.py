from typing import List, Tuple, Dict

from codemonkeys.help.help import run_default_help


def _split_unknown_args(unknown_args: List[str]) -> Tuple[Dict[str, bool], List[str]]:
    """
    Splits unknown args into named/unnamed args.
    
    :param List[str] unknown_args: Unknown args.
    :return: Tuple containing dictionary of named args and list of unnamed args.
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

    :return: Tuple representing monk_args (argparse.Namespace), named_args (dict),
             unnamed_args (list), action (str), entity_name (str),
             and entity_type (str).
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
    elif monk_args.help is True:
        action = 'help'

    # Entity Type
    entity_type = 'command'
    if action == 'help':
        entity_type = 'help'
    elif monk_args.automation is True:
        entity_type = 'automation'
    elif monk_args.barrel is True:
        entity_type = 'barrel'

    if entity_type in ['help', 'command'] and monk_args.entity_name in [None, 'help']:
        run_default_help()

    return monk_args, named_args, unnamed_args, action, monk_args.entity_name, entity_type
