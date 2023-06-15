import os
import subprocess
import sys

from config.defs import CORE_HELP_PATH
from core.help.help import run_help
from core.utils.find_entity import find_entity
from core.utils.monk.run_as_module import run_as_module
from core.utils.monk.theme.theme_functions import print_t


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


def handle_help(args, action, entity, entity_type):
    if entity is None or entity == 'help':
        run_help()
    else:
        entity_path = os.path.join(CORE_HELP_PATH, f'{entity_type}s', f'{entity}.py')
        run_as_module(entity_path.strip(), function_name='main', monk_args=args)
