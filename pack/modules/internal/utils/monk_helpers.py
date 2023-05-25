import os
import subprocess
import argparse
import sys
import importlib.util

from pack.modules.custom.style.visuals import printc, inputc
from pack.modules.internal.utils.symlinks import check_definitions
from pack.commands.internal.help import main as run_help

# IMPORTANT! PLEASE READ
# definitions.py should not be imported here. It is better to make all direct monk command functionality accept related
# arguments that are passed from monk (in root), so that definitions.py symlink issues don't break core monk features.


def parse_monk_args(commands_path, automations_path, barrels_path, modules_path):
    default_action = 'run'
    default_entity_type = 'command'

    # Create argument parser - use custom help
    parser = argparse.ArgumentParser(add_help=False)

    # Special flags - flags that override normal behaviors significantly.
    parser.add_argument('-v', '--version', action='store_true')

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
    args = parser.parse_args()

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
    entity_path = commands_path
    if args.module is True:
        entity_type = 'module'
        entity_path = modules_path
    elif args.automation is True:
        entity_type = 'automation'
        entity_path = automations_path
    elif args.barrel is True:
        entity_type = 'barrel'
        entity_path = barrels_path

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
        printc(
            f"You are attempting to use the 'run' action a module with. This could work if there is a default behavior "
            f"for the module (like a main function), but you may want to exercise caution.", 'warning')
        inputc("Press Enter to continue or Ctrl+C to cancel...")

    return args, action, args.entity, entity_type, entity_path


def handle_alternate_actions(action, script_path):

    if action == 'edit':
        subprocess.run(['vim', script_path.strip()])

    elif action == 'print':
        subprocess.run(['cat', script_path.strip()])

    elif action == 'copy_path':
        subprocess.run(['pbcopy'], input=script_path.strip().encode('utf-8'))
        printc("Copied script absolute path to clipboard", 'file')

    elif action == 'copy_contents':
        subprocess.run(['pbcopy'], input=open(script_path.strip(), 'rb').read())
        printc("Copied script contents to clipboard", 'file')
    else:
        return False
    return True


# This function is used to handle special commands that are not actually entities.
# The entity argument maintains that nomenclature for consistency with the rest of the code.
# It seems intuitive enough given these 'commands' are clearly exceptions.
def handle_special_commands(args, action, entity, entity_type, root_path, python_command, version):

    # If -v or --version, print version and sys.exit. Maybe eventually implement versioning for entities?
    if args.version:
        printc(f"CodeMonkeys v{version}", 'monkey')

    # Help needs to work in many contexts, and it would be a pain to place help executables throughout the framework,
    # so it is a lot easier to detect it outright and run through custom logic, with a central location for help files.
    elif action == 'help' or entity == 'help':
        handle_help(args, action, entity, entity_type, root_path, python_command)

    # This must be called from the root directory and passed an absolute root_path that is verifiable in the absence
    # of a functional definitions.py symlink (pack/definitions.py).
    elif entity == 'check-definitions':
        root_definitions = os.path.join(root_path, 'definitions.py')
        pack_definitions = os.path.join(root_path, 'pack', 'definitions.py')
        check_definitions(root_definitions, pack_definitions, verify_symlink=True)
    else:
        return False
    return True


def handle_help(args, action, entity, entity_type, root_path, python_command):
    if entity_type != 'command':
        printc(f"Help is not available for {entity_type}.", 'error')
        sys.exit(1)
    if entity is None or entity == 'help':
        run_help()
    else:
        printc(f"Help is not available for specific commands. Working on it.", 'error')


# This function is important for maintaining the pack "pseudo-package" paradigm.
# Python will not allow you to use the relative imports this framework relies on (within pack)
def run_command_as_module(module_path, function_name, args):
    spec = importlib.util.spec_from_file_location('module', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    function = getattr(module, function_name)
    return function(*args)
