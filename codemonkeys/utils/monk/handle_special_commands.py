import os

from __init__ import __version__
from defs import ROOT_PATH, CM_COMMANDS_PATH, CM_BARRELS_PATH, CM_AUTOMATIONS_PATH, CM_TASKS_PATH, nl, CM_HELP_PATH, \
    CONFIG_PATH, THEME_CONFIG_PATH
from codemonkeys.help.help import run_default_help
from codemonkeys.utils.find_entity import find_entity
from codemonkeys.utils.monk.run_as_module import run_as_module
from codemonkeys.utils.monk.theme_functions import print_t, print_tree


# This function is used to handle special commands that are not actually entities.
# The entity argument maintains that nomenclature for consistency with the rest of the code.
# It seems intuitive enough given these 'commands' are clearly exceptions.
def handle_special_commands(args, action, entity, entity_type):
    # If -v or --version, print version and sys.exit. Maybe eventually implement versioning for entities?
    if args.version:
        print_t(f"CodeMonkeys v{__version__}", 'monkey')

    # Toggle light mode
    elif args.toggle_light_mode:
        with open(THEME_CONFIG_PATH, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if "light_mode_enabled" in line:
                    is_light_mode = "True" in line
                    print_t(f"{'Disabling' if is_light_mode else 'Enabling'} Light Mode...", 'monkey')
                    line = f"light_mode_enabled: bool = False{nl}" if is_light_mode else f"light_mode_enabled: bool = True{nl}"
                file.write(line)
            file.truncate()

    # Help needs to work in many contexts, and it would be a pain to place help executables throughout the codemonkeys,
    # so it is a lot easier to detect it outright and run through custom logic, with a central location for help files.
    elif action == 'help' or entity == 'help':
        handle_help(args, action, entity, entity_type)
    elif entity == 'list':
        if entity_type == 'command' or args.all:
            print()
            print_tree(CM_COMMANDS_PATH, exclude_file_starts=['.', '_'],
                       title="📁  Commands - Run CLI commands", incl_prefix=False)
        if entity_type == 'barrel' or args.all:
            print()
            print_tree(CM_BARRELS_PATH, exclude_file_starts=['.', '_'],
                       title="🛢️   Barrels - Combine and orchestrate automations", incl_prefix=False)
        if entity_type == 'automation' or args.all:
            print()
            print_tree(CM_AUTOMATIONS_PATH, exclude_file_starts=['.', '_'],
                       title="🤖  Automations - Run automations with monkey configs", incl_prefix=False)
        if entity_type == 'module' or args.all:
            print()
            print_tree(CM_TASKS_PATH, exclude_file_starts=['.', '_'],
                       title="📦  Modules - project modules that can be imported", incl_prefix=False)
    else:
        return False
    return True


def handle_help(args, action, entity, entity_type):
    if entity is None or entity == 'help':
        run_default_help()
    else:
        entity_path = find_entity(entity, entity_type, CM_HELP_PATH)
        run_as_module(entity_path.strip(), function_name='main', monk_args=args)
