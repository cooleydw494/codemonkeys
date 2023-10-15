#!/usr/bin/env python
import os
import subprocess
import sys

from codemonkeys.utils.misc.defs_utils import find_project_root

sys.path.append(find_project_root())

from codemonkeys.utils.config.update_env_class import update_env_class
from codemonkeys.utils.misc.handle_exception import handle_exception

# Regenerate Env class
update_env_class()

from codemonkeys.utils.monk.find_entity import find_entity
from codemonkeys.utils.monk.parse_monk_args import parse_monk_args
from codemonkeys.utils.monk.run_entities import run_automation, run_command, run_barrel
from codemonkeys.utils.monk.theme_functions import print_t


# Some basic environment checks
version = sys.version_info[0]
if version < 3:
    print_t("It appears you're running Python 2. Please use Python 3.", 'error')
    sys.exit(1)

try:

    # Setup and Parse Monk Arguments
    named_args, unnamed_args, action, entity_name, entity_type = parse_monk_args()

    # Find Entity (includes interactive selection)
    entity_name, entity_path = find_entity(entity_name, entity_type)

    if action == 'edit':
        subprocess.run(['vim', entity_path.strip()])

    elif action == 'run':
        print_t(f'{entity_type}: {entity_name}', 'quiet')

        # Commands
        if entity_type in ['command', 'help']:
            extension = os.path.splitext(entity_path.strip())[1]

            if extension == ".py":
                run_command(entity_path.strip(), entity_name, named_args, unnamed_args)

            elif extension == ".sh":
                subprocess.call(['bash', entity_path.strip()] + sys.argv[2:])

            elif extension == ".bat":
                subprocess.call([entity_path.strip()] + sys.argv[2:])

            else:
                print_t(f"Unsupported Command ext: {extension}. find_entity should filter this.", 'error')
                exit(1)

        # Automations
        elif entity_type == 'automation':
            run_automation(entity_path.strip(), entity_name, named_args, unnamed_args)

        # Barrels
        elif entity_type == 'barrel':
            run_barrel(entity_path.strip(), entity_name, named_args, unnamed_args)

        # Unsupported
        else:
            print_t(f'unsupported entity_type: {entity_type}', 'error')
            exit(1)

    else:
        print_t(f'unsupported action: {action}', 'error')
        exit(1)

except BaseException as e:
    handle_exception(e)

exit(0)
