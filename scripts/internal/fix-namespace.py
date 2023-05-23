import os
import pathlib
import re

from definitions import ROOT_PATH, ROOT_DIR_NAME


def rename_directory(new_name):
    parent_directory = os.path.dirname(ROOT_PATH)
    new_directory_path = os.path.join(parent_directory, new_name)
    os.rename(ROOT_PATH, new_directory_path)
    return new_directory_path


def replace_imports_in_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    # Use a regex to replace 'from code_monkeys' with 'from base_dir_name'
    data = re.sub(r'from code_monkeys', f'from {ROOT_DIR_NAME}', data)

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
      "option to change the directory name and automatically rewrite the namespaced imports to avoid this issue.")

new_directory_name = input(
    "Please enter the new directory name (e.g. project-name-monkeys), or press Enter to skip: ").strip()
if new_directory_name:
    rename_directory(new_directory_name)
else:
    print(
        "You've chosen to skip this (totally fine for a single copy). If you have issues later, you can still do "
        "this with `monk fix-namespace`.")

replace_imports_in_dir(ROOT_DIR_NAME)
