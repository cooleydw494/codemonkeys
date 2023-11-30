#!/usr/bin/env python
import os
import shutil
import sys

from termcolor import colored

from codemonkeys.cm_paths import (CM_ENV_DEFAULT_PATH, CM_THEME_DEFAULT_PATH, CM_AUTOMATIONS_DIR_DEFAULT_PATH,
                                  CM_ENV_CLASS_DEFAULT_PATH, CM_GITIGNORE_DEFAULT_PATH, CM_README_DEFAULT_PATH,
                                  CM_CONTEXT_FILE_EXAMPLE_PATH, CM_DEFAULT_REQUIREMENTS_PATH,
                                  CM_MONKEYS_DIR_DEFAULT_PATH, CM_EXAMPLE_MIXIN_PATH, CM_EXAMPLE_FUNC_PATH,
                                  CM_EXAMPLE_BARREL_PATH, CM_COMMANDS_DIR_DEFAULT_PATH)

top_level_dirs = [
    'barrels',
    'funcs',
    'config',
    'builders',
    'mixins',
    'stor',
]

stor_dirs = [
    'context',
    'output',
    'work_path',
    'temp',
]


def main():
    """
    Create a new CodeMonkeys project directory structure and initial files.

    This script initializes a new CodeMonkeys project with the necessary directory structure
    and a set of starting files, including a default .env file, config files, automation scripts,
    monkey definitions, functions, and barrels. It also copies example mixin and func classes
    to help the user get started with custom logic.
    """

    # Get the new project name from the command line arguments
    try:
        new_project_name = sys.argv[1]
    except IndexError:
        print(colored('Please provide a project name, like `monk-new my_project`.', 'red'))
        sys.exit(1)

    if os.path.exists(new_project_name):
        print(colored(f"Directory '{new_project_name}' already exists.", 'red'))
        sys.exit(1)

    if not new_project_name.replace('_', '').isalpha():
        print(
            colored("Project name must only contain letters/underscores to enable relative imports within user modules",
                    'red'))
        sys.exit(1)

    print(colored(f"Initializing new CodeMonkeys project '{new_project_name}'...", 'green'))

    # Create the project root directory
    print(colored(f"Creating directory: {new_project_name}", 'cyan'))
    os.makedirs(new_project_name, exist_ok=True)

    project_path = os.path.join(os.getcwd(), new_project_name)

    # Create the default .env file
    print(colored("Creating default .env file", 'cyan'))
    shutil.copyfile(CM_ENV_DEFAULT_PATH, os.path.join(project_path, ".env"))

    # Create the top level directories
    for top_level_dir in top_level_dirs:
        print(colored(f"Creating directory: {top_level_dir}", 'cyan'))
        os.makedirs(os.path.join(project_path, top_level_dir), exist_ok=True)

    # Create the stor directories
    for stor_dir in stor_dirs:
        print(colored(f"Creating directory: stor/{stor_dir}", 'cyan'))
        os.makedirs(os.path.join(project_path, 'stor', stor_dir), exist_ok=True)

    # Create the config files
    print(colored("Creating config/example files...", 'cyan'))
    config_path = os.path.join(project_path, 'config')
    print(colored("Creating default monkeys...", 'cyan'))
    shutil.copytree(CM_MONKEYS_DIR_DEFAULT_PATH, os.path.join(project_path, 'monkeys'))
    shutil.copyfile(CM_CONTEXT_FILE_EXAMPLE_PATH, os.path.join(project_path, 'stor', 'context', 'context-file.txt'))
    shutil.copyfile(CM_THEME_DEFAULT_PATH, os.path.join(config_path, 'theme.py'))

    # Create Env class
    env_class_path = os.path.join(config_path, 'env.py')
    shutil.copyfile(CM_ENV_CLASS_DEFAULT_PATH, env_class_path)
    # Fix theme import for project config files
    with open(env_class_path, 'r') as f:
        lines = f.readlines()
    with open(env_class_path, 'w') as f:
        for line in lines:
            f.write(line.replace('from codemonkeys.config.theme', 'from config.theme'))

    # Create the default commands
    print(colored("Creating default commands...", 'cyan'))
    shutil.copytree(os.path.join(CM_COMMANDS_DIR_DEFAULT_PATH), os.path.join(project_path, 'commands'))

    # Create the default automation
    print(colored("Creating default automations...", 'cyan'))
    shutil.copytree(CM_AUTOMATIONS_DIR_DEFAULT_PATH, os.path.join(project_path, 'automations'))

    # Create the example barrels
    print(colored("Creating default barrels...", 'cyan'))
    shutil.copyfile(CM_EXAMPLE_BARREL_PATH, os.path.join(project_path, 'barrels', 'example_barrel.py'))

    # Create the default mixins
    print(colored("Creating default mixins...", 'cyan'))
    shutil.copyfile(CM_EXAMPLE_MIXIN_PATH, os.path.join(project_path, 'mixins', 'my_project_workspace.py'))

    # Create the default funcs
    print(colored("Creating default funcs...", 'cyan'))
    shutil.copyfile(CM_EXAMPLE_FUNC_PATH, os.path.join(project_path, 'funcs', 'example_func.py'))

    # Create the default gitignore
    print(colored("Creating default .gitignore...", 'cyan'))
    shutil.copyfile(CM_GITIGNORE_DEFAULT_PATH, os.path.join(project_path, '.gitignore'))

    # Create the default requirements
    print(colored("Creating default requirements...", 'cyan'))
    shutil.copyfile(CM_DEFAULT_REQUIREMENTS_PATH, os.path.join(project_path, 'requirements.txt'))

    # Create the default README
    print(colored("Creating default README...", 'cyan'))
    shutil.copyfile(CM_README_DEFAULT_PATH, os.path.join(project_path, 'README.md'))

    print(colored('CodeMonkeys setup complete', 'green'))
