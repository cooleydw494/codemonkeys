import os
import platform
import subprocess

from codemonkeys.utils.monk.theme_functions import print_t


def verify_or_create_symlink(target, symlink_path, output=True):
    if output:
        print_t(f'Verifying or creating symlink from {symlink_path} to {target}', 'link')

    try:
        existing_link_target = os.readlink(symlink_path)
        if existing_link_target == str(target):
            return
        elif output:
            print_t('The symlink points to the wrong file. Fixing symlink...', 'warning')
    except OSError:
        if output:
            print_t('The symlink does not exist. Creating symlink...', 'warning')

    if platform.system() == 'Windows':
        try:
            if os.path.islink(symlink_path):
                os.unlink(symlink_path)
            subprocess.check_call(['cmd', '/c', 'mklink', symlink_path, target])
        except (OSError, subprocess.CalledProcessError):
            print_t(f'Unable to create {symlink_path} symlink. Run script as Administrator or enable Developer Mode.', 'error')
    else:
        try:
            if os.path.islink(symlink_path):
                os.unlink(symlink_path)
            os.symlink(target, symlink_path)
        except OSError as e:
            print_t(f'Unable to create {symlink_path} symlink: {str(e)}', 'error')
