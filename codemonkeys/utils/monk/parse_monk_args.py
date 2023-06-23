import argparse

from codemonkeys.utils.monk.theme_functions import print_t, input_t


def parse_monk_args():
    default_action = 'run'
    default_entity_type = 'command'

    # Create argument parser - use custom help
    parser = argparse.ArgumentParser(add_help=False)

    # Unique args
    parser.add_argument("-monkey", "--monkey", type=str)

    # Special flags - flags that override normal behaviors significantly.
    parser.add_argument('-v', '--version', action='store_true')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--toggle-light-mode', action='store_true')

    # Action flags - mutually exclusive, overrides default of "run"
    action_flags = parser.add_mutually_exclusive_group()
    action_flags.add_argument('-r', '--run', action='store_true')
    action_flags.add_argument('-e', '--edit', action='store_true')
    action_flags.add_argument('-p', '--print', action='store_true')
    action_flags.add_argument('-cp', '--copy-path', action='store_true')
    action_flags.add_argument('-cc', '--copy-contents', action='store_true')
    action_flags.add_argument('-h', '--help', action='store_true')

    # Entity Type flags - mutually exclusive, overrides default of "command"
    entity_type_flags = parser.add_mutually_exclusive_group()
    entity_type_flags.add_argument('-m', '--module', action='store_true')
    entity_type_flags.add_argument('-a', '--automation', action='store_true')
    entity_type_flags.add_argument('-b', '--barrel', action='store_true')

    # Entity is the name of the command or overridden entity_type
    parser.add_argument('entity', nargs='?')

    # Parse Arguments
    args, unknown_args = parser.parse_known_args()

    # Action
    action = None
    if args.edit is True:
        action = 'edit'
    elif args.print is True:
        action = 'print'
    elif args.copy_path is True:
        action = 'copy_path'
    elif args.copy_contents is True:
        action = 'copy_contents'
    elif args.help is True:
        action = 'help'

    # Entity Type
    entity_type = None
    if args.module is True:
        entity_type = 'module'
    elif args.automation is True:
        entity_type = 'automation'
    elif args.barrel is True:
        entity_type = 'barrel'

    if entity_type == 'module':
        default_action = 'edit'

    if action is None and args.entity is None and entity_type is None:
        # If all values are default (run <None> command), simulate `monk --help`
        action = 'help'

    # Apply any relevant defaults
    action = action or default_action
    entity_type = entity_type or default_entity_type

    # Warning For "run" action on non-commands
    if action == 'run' and entity_type == 'module':
        print_t(
            f"You are attempting to use the 'run' action a module with. This could work if there is a default behavior "
            f"for the module (like a main function), but you may want to exercise caution.", 'warning')
        input_t("Press Enter to continue or Ctrl+C to cancel...")

    return args, unknown_args, action, args.entity, entity_type