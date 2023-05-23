# import os
# import pathlib
# import re
#
# from termcolor import colored
#
# from definitions import ROOT_PATH, PSEUDO_PACKAGE_PATH, PSEUDO_PACKAGE_DIR_NAME, STORAGE_INTERNAL_PATH, ROOT_DIR_NAME
#
#
# def rename_directory(existing_dir_absolute_path, new_name):
#     print(f"Renaming {existing_dir_absolute_path} to {new_name}...")
#     # get the directory containing the existing directory
#     parent_directory = os.path.dirname(existing_dir_absolute_path)
#     new_directory_path = os.path.join(parent_directory, new_name)
#     os.rename(existing_dir_absolute_path, new_directory_path)
#     return new_directory_path
#
#
# def replace_imports_in_file(file_path, old_name, new_name):
#     with open(file_path, 'r') as f:
#         data = f.read()
#
#     # Use regex to replace 'from [old name]' with 'from [new name]'
#     data = re.sub(rf'from \b{old_name}\b', f'from {new_name}', data)
#
#     with open(file_path, 'w') as f:
#         f.write(data)
#
#
# def replace_imports_in_dir(root_path, old_name, new_name):
#     print(f"Updating module imports in {root_path}...")
#     # Use pathlib to recursively go through each file in the directory
#     files_updated = 0
#     for file_path in pathlib.Path(root_path).rglob('*.py'):
#         try:
#             replace_imports_in_file(file_path, old_name, new_name)
#             files_updated += 1
#         except Exception as e:
#             print(f"Failed to update module imports in {file_path} due to error: {e}")
#     print(f"Successfully updated module imports in {files_updated} files.")
#
#
# print("The CodeMonkeys project uses `sys.path` to globally import modules. If this isn't the only version of "
#       "CodeMonkeys on your local machine you might run into conflicts. For that reason (or any other) you have the "
#       "option to change project name and automatically rewrite the namespaced imports to avoid this issue.")
#
# while True:
#     new_root_dir_name = input(
#         "Please enter a new name (like [project-name]-monkeys), or press Enter to skip: ").strip()
#     if not new_root_dir_name:
#         print("You've chosen to skip this (totally fine for a single copy). If you have issues later, you can run "
#               "this again with `monk fix-namespace`.")
#         exit(1)
#     elif re.match(r"^[a-zA-Z\-]+$", new_root_dir_name):
#         break  # Name is valid , break the loop
#     else:
#         print(colored("Invalid name. Please use only letters and hyphens.", "red"))
#
# # imported paths from definitions.py will not update in this script after updating, so let's just store old and new
# # paths and names in local variables to avoid confusion (trust me, it was confusing)
# old_root_path = ROOT_PATH
# old_root_dir_name = ROOT_DIR_NAME
# old_pseudo_package_path = PSEUDO_PACKAGE_PATH
# old_pseudo_package_name = PSEUDO_PACKAGE_DIR_NAME
# old_storage_internal_path = STORAGE_INTERNAL_PATH
#
# new_root_path = old_root_path.replace(old_root_dir_name, new_root_dir_name)
# new_pseudo_package_name = new_root_dir_name.replace('-', '_')
# new_pseudo_package_path = old_pseudo_package_path.replace(old_pseudo_package_name, new_pseudo_package_name)
#
# # write new pseudo package name to storage for use in setup.py, which also will not receive updated path definitions
# # Note: we haven't changed anything yet, so we use the old storage path for the write operations
# with open(os.path.join(old_storage_internal_path, 'pseudo_package_dir_name.txt'), 'w') as file:
#     file.write(new_pseudo_package_name)
#
# # do the same for the new root path
# with open(os.path.join(old_storage_internal_path, 'root_path.txt'), 'w') as file:
#     file.write(new_root_path)
#
# # now we can rename the directories
# try:
#     rename_directory(old_root_path, new_root_dir_name)
# except Exception as e:
#     print(f"Failed to rename {old_root_path} to {new_root_dir_name} due to error: {e}")
#     exit(1)
# # We have to use a combination of new root path and old pseudo-package path here to get the temp pseudo-package path
# temp_pseudo_package_path = os.path.join(new_root_path, old_pseudo_package_name)
# try:
#     rename_directory(temp_pseudo_package_path, new_pseudo_package_name)
# except Exception as e:
#     print(f"Failed to rename {old_pseudo_package_path} to {new_pseudo_package_name} due to error: {e}")
#     exit(1)
#
# # now we need to update imports (using the newly renamed pseudo-package directory's path)
# replace_imports_in_dir(new_pseudo_package_path, old_pseudo_package_name, new_pseudo_package_name)
