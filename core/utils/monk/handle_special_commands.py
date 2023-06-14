import os

from __init__ import __version__
from config.defs import ROOT_PATH, COMMANDS_PATH, BARRELS_PATH, AUTOMATIONS_PATH, MODULES_PATH, nl
from core.utils.monk.theme.theme_functions import print_t, print_tree
from core.utils.monk.handle_alternate_actions import handle_help


# This function is used to handle special commands that are not actually entities.
# The entity argument maintains that nomenclature for consistency with the rest of the code.
# It seems intuitive enough given these 'commands' are clearly exceptions.
def handle_special_commands(args, action, entity, entity_type):
    # If -v or --version, print version and sys.exit. Maybe eventually implement versioning for entities?
    if args.version:
        print_t(f"CodeMonkeys v{__version__}", 'monkey')

    # Toggle light mode
    elif args.toggle_light_mode:
        with open(os.path.join(ROOT_PATH, "defs.py"), "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if "LIGHT_MODE_ENABLED" in line:
                    is_light_mode = "True" in line
                    print_t(f"{'Disabling' if is_light_mode else 'Enabling'} Light Mode...", 'monkey')
                    line = f"LIGHT_MODE_ENABLED = False{nl}" if is_light_mode else f"LIGHT_MODE_ENABLED = True{n}"
                file.write(line)
            file.truncate()

    # Help needs to work in many contexts, and it would be a pain to place help executables throughout the core,
    # so it is a lot easier to detect it outright and run through custom logic, with a central location for help files.
    elif action == 'help' or entity == 'help':
        handle_help(args, action, entity, entity_type)
    elif entity == 'list':
        if entity_type == 'command' or args.all:
            print()
            print_tree(COMMANDS_PATH, exclude_file_starts=['.', '_'],
                       title="📁  Commands - Run CLI commands", incl_prefix=False)
        if entity_type == 'barrel' or args.all:
            print()
            print_tree(BARRELS_PATH, exclude_file_starts=['.', '_'],
                       title="🛢️   Barrels - Combine and orchestrate automations", incl_prefix=False)
        if entity_type == 'automation' or args.all:
            print()
            print_tree(AUTOMATIONS_PATH, exclude_file_starts=['.', '_'],
                       title="🤖  Automations - Run automations with monkey configs", incl_prefix=False)
        if entity_type == 'module' or args.all:
            print()
            print_tree(MODULES_PATH, exclude_file_starts=['.', '_'],
                       title="📦  Modules - project modules that can be imported", incl_prefix=False)
    else:
        return False
    return True
