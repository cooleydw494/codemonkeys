import argparse
from collections import OrderedDict
from typing import List, Tuple, Dict

from codemonkeys.utils.monk.theme_functions import print_t, input_t


def split_unknown_args(unknown_args: List[str]) -> Tuple[Dict[str, bool], List[str]]:
    unknown_named_args = OrderedDict()
    unknown_unnamed_args = []
    iterator = iter(unknown_args)
    for arg in iterator:
        if arg.startswith('--') or arg.startswith('-'):
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
    import argparse
    from collections import OrderedDict

    # Create argument parser - use custom help
    parser = argparse.ArgumentParser(add_help=False)

    # Unique args
    parser.add_argument("-monkey", "--monkey", type=str)

    # Special flags - flags that override normal behaviors significantly.
    parser.add_argument('-v', '--version', action='store_true')
    parser.add_argument('--toggle-light-mode', action='store_true')

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

    # Split unknown arguments into named and unnamed
    unknown_named_args, unknown_unnamed_args = split_unknown_args(unknown_args)

    # Action
    action = 'run'
    if monk_args.edit is True:
        action = 'edit'
    elif monk_args.help is True:
        action = 'help'

    # Entity Type
    entity_type = 'command'
    if monk_args.automation is True:
        entity_type = 'automation'
    elif monk_args.barrel is True:
        entity_type = 'barrel'

    if action == 'run' and entity_type == 'command' and monk_args.entity_name is None:
        # Simulate `monk help`
        monk_args.entity_name = 'help'

    return monk_args, unknown_named_args, unknown_unnamed_args, action, monk_args.entity_name, entity_type
