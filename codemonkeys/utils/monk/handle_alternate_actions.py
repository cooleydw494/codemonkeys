import subprocess
from codemonkeys.utils.monk.theme_functions import print_t


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
