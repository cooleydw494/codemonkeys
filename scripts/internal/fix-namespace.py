import pathlib
import re

from definitions import ROOT_DIR_NAME


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


replace_imports_in_dir(ROOT_DIR_NAME)
