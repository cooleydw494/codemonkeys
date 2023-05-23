import os
import pathlib
import re

from definitions import ROOT_PATH, ROOT_DIR_NAME, PSEUDO_PACKAGE_PATH


def rename_directory(existing_dir_absolute_path, new_name):
    # get the directory containing the existing directory
    parent_directory = os.path.dirname(existing_dir_absolute_path)
    new_directory_path = os.path.join(parent_directory, new_name)
    os.rename(existing_dir_absolute_path, new_directory_path)
    return new_directory_path


def replace_imports_in_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    # Use a regex to replace 'from /Users/david/local-git/code-monkeys/code_monkeys' with 'from base_dir_name'
    data = re.sub(r'from /Users/david/local-git/code-monkeys/code_monkeys', f'from {PSEUDO_PACKAGE_PATH}', data)

    with open(file_path, 'w') as file:
        file.write(data)


def replace_imports_in_dir(dir_path):
    # Use pathlib to recursively go through each file in the directory
    for file_path in pathlib.Path(dir_path).rglob('*.py'):
        print(f"Processing {file_path}...")
        try:
            replace_imports_in_file(file_path)
            print(f"Successfully updated imports in {file_path}.")
        except Exception as e:
            print(f"Failed to update imports in {file_path} due to error: {e}")


print("The CodeMonkeys project uses `sys.path` to globally import modules. If this isn't the only version of "
      "CodeMonkeys on your local machine you might run into conflicts. For that reason (or any other) you have the "
      "option to change project name and automatically rewrite the namespaced imports to avoid this issue.")

new_root_name = input(
    "Please enter a new name (like [project-name]-monkeys), or press Enter to skip: ").strip()
if new_root_name:
    rename_directory(ROOT_PATH, new_root_name)
    new_pseudo_directory_name = new_root_name.replace('-', '_')
    rename_directory(PSEUDO_PACKAGE_PATH, new_pseudo_directory_name)
else:
    print(
        "You've chosen to skip this (totally fine for a single copy). If you have issues later, you can run this again "
        "with `monk fix-namespace`.")

replace_imports_in_dir(ROOT_PATH)
