import argparse
import importlib.util
import subprocess
import sys

from __init__ import __version__
from definitions import COMMANDS_PATH, BARRELS_PATH, AUTOMATIONS_PATH, MODULES_PATH
from pack.commands.internal.help import main as run_help
from pack.modules.custom.theme.theme_functions import print_t, input_t, print_tree


def parse_monk_args():
    default_action = 'run'
    default_entity_type = 'command'

    # Create argument parser - use custom help
    parser = argparse.ArgumentParser(add_help=False)

    # Special flags - flags that override normal behaviors significantly.
    parser.add_argument('-v', '--version', action='store_true')
    parser.add_argument('--all', action='store_true')

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


def handle_alternate_actions(action, script_path):
    if action == 'edit':
        subprocess.run(['vim', script_path.strip()])

    elif action == 'print':
        subprocess.run(['cat', script_path.strip()])

    elif action == 'copy_path':
        subprocess.run(['pbcopy'], input=script_path.strip().encode('utf-8'))
        print_t("Copied script absolute path to clipboard", 'file')

    elif action == 'copy_contents':
        subprocess.run(['pbcopy'], input=open(script_path.strip(), 'rb').read())
        print_t("Copied script contents to clipboard", 'file')
    else:
        return False
    return True


# This function is used to handle special commands that are not actually entities.
# The entity argument maintains that nomenclature for consistency with the rest of the code.
# It seems intuitive enough given these 'commands' are clearly exceptions.
def handle_special_commands(args, action, entity, entity_type):
    # If -v or --version, print version and sys.exit. Maybe eventually implement versioning for entities?
    if args.version:
        print_t(f"CodeMonkeys v{__version__}", 'monkey')

    # Help needs to work in many contexts, and it would be a pain to place help executables throughout the framework,
    # so it is a lot easier to detect it outright and run through custom logic, with a central location for help files.
    elif action == 'help' or entity == 'help':
        handle_help(args, action, entity, entity_type)
    elif entity == 'list':
        if entity_type == 'command' or args.all:
            print()
            print_tree(COMMANDS_PATH, [], "📁 Commands - core framework CLI commands")
        if entity_type == 'barrel' or args.all:
            print()
            print_tree(BARRELS_PATH, [], "🛢️  Barrels - scripts that orchestrate multiple Automations")
        if entity_type == 'automation' or args.all:
            print()
            print_tree(AUTOMATIONS_PATH, [], "🤖 Automations - scripts that run automated tasks using monkey configs")
        if entity_type == 'module' or args.all:
            print()
            print_tree(MODULES_PATH, [], "📦 Modules - project modules that can be imported")
    else:
        return False
    return True


def handle_help(args, action, entity, entity_type):
    if entity_type != 'command':
        print_t(f"Help is not available for {entity_type}.", 'error')
        sys.exit(1)
    if entity is None or entity == 'help':
        run_help()
    else:
        print_t(f"Help is not available for specific commands. Working on it.", 'error')


# This function is important for maintaining the pack "pseudo-package" paradigm.
# Python will not allow you to use the relative imports this framework relies on (within pack)
def run_command_as_module(module_path, function_name, args):
    spec = importlib.util.spec_from_file_location('module', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    function = getattr(module, function_name)
    return function(*args)
