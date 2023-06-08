import subprocess
import sys

from pack.modules.internal.theme.theme_functions import print_t
from pack.commands.internal.utils.help import main as run_help


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
    if entity_type != 'command':
        print_t(f"Help is not available for {entity_type}.", 'error')
        sys.exit(1)
    if entity is None or entity == 'help':
        run_help()
    else:
        print_t(f"Help is not available for specific commands. Working on it.", 'error')