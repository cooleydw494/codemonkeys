import os
import importlib.util
import platform

from pack.modules.custom.theme.theme_functions import print_t

"""
IMPORTANT!
The reason absolute paths are passed to this instead of importing PATHs from definitions.py
is that this module needs to work in the absence of a functional definitions.py symlink.
(it is used to create or fix that symlink)
"""


def import_from_path(module_path):
    spec = importlib.util.spec_from_file_location('module', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_or_create_symlink(target, symlink_path, output=True):
    if output:
        print_t(f'Verifying or creating symlink from {symlink_path} to {target}', 'link')
    # Check if the symlink exists and points to the correct file
    if os.path.islink(symlink_path):
        if os.readlink(symlink_path) != str(target):
            if output:
                print_t('The symlink points to the wrong file. Fixing symlink...', 'warning')
        else:
            return
    else:
        print_t('The symlink does not exist. Creating symlink...', 'warning')

    if platform.system() == 'Windows':
        import subprocess
        try:
            if os.path.islink(symlink_path):
                os.unlink(symlink_path)
            subprocess.check_call(['cmd', '/c', 'mklink', symlink_path, target])
        except subprocess.CalledProcessError:
            print_t(f'Unable to create {symlink_path} symlink. Run script as Administrator or enable Developer Mode.',
                   'error')
    else:
        if os.path.islink(symlink_path):
            os.unlink(symlink_path)
        os.symlink(target, symlink_path)


def check_definitions(original_file_path, symlink_path, verify_symlink=False):
    # The `monk` command already does this, but this function can be overridden for special cases like setup.py
    if verify_symlink:
        verify_or_create_symlink(original_file_path, symlink_path)

    print_t(f'Checking definitions in {original_file_path} and {symlink_path}', 'monkey')

    # Import the original and symlinked definitions files
    original_definitions = import_from_path(original_file_path)
    symlink_definitions = import_from_path(symlink_path)

    # Count of differing definitions
    diff_count = 0

    # Iterate over all definitions in the original file
    for name in dir(original_definitions):
        if name.startswith('__'):  # Skip Python internal names
            continue
        original_value = getattr(original_definitions, name)
        symlink_value = getattr(symlink_definitions, name, None)
        if symlink_value is None:
            print_t(f'Missing in symlink: {name}', 'error')
            diff_count += 1
        elif original_value != symlink_value:
            print_t(f'Conflicting {name}: original={original_value}, symlink={symlink_value}', 'error')
            diff_count += 1
        else:
            print_t(f'{name}={original_value}', 'quiet')

    conflicts_text = f'Found {diff_count} definition conflicts.'
    if diff_count > 0:
        print_t(conflicts_text, 'error')
        print_t('Please ensure all definitions are compatible with the symlink.', 'error')
        sys.exit(1)
    else:
        print_t(conflicts_text, 'success')
