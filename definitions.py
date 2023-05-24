import os

from modules.internal.utils.get_python_command import get_python_command, get_pip_command

"""
IMPORTANT - PLEASE READ!

This file is symlinked in code-monkeys/modules/definitions.py by the setup script.
This is because the modules of CodeMonkeys are a "pseudo-package". See README.md for more of "pseudo-package" concept.
This does have some implications on how to use it, but if you follow the rules below, you should be fine.

RULES:
1. *Always use ROOT_PATH to get other paths*, leaving the ROOT_PATH logic in this file untouched.
2. Do not change the base structure of the modules directory, or move the symlinked definitions.py file.
3. If you want to add a new directory, add it to the ROOT_PATH definition below, and then add a new variable

If you don't need python code to set a custom variable, you can just use the code-monkeys/.env file.
"""

# ROOT_PATH (works in symlink and original)
if os.path.islink(os.path.abspath(__file__)):
    # Symlink: use the parent directory
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
else:
    # Original: use the current directory
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# ROOT_DIR_NAME
ROOT_DIR_NAME = os.path.basename(ROOT_PATH)


# MONK
MONK_PATH = os.path.join(ROOT_PATH, "monk")


# MONKEYS
MONKEYS_PATH = os.path.join(ROOT_PATH, "monkeys")

MONKEYS_INTERNAL_PATH = os.path.join(MONKEYS_PATH, "internal")
MONKEYS_CUSTOM_PATH = os.path.join(MONKEYS_PATH, "custom")


# AUTOMATIONS
AUTOMATIONS_PATH = os.path.join(ROOT_PATH, "modules/scripts/automations")

AUTOMATIONS_INTERNAL_PATH = os.path.join(AUTOMATIONS_PATH, "internal")
AUTOMATIONS_CUSTOM_PATH = os.path.join(AUTOMATIONS_PATH, "custom")


# SCRIPTS
SCRIPTS_PATH = os.path.join(ROOT_PATH, "modules/scripts")

SCRIPTS_INTERNAL_PATH = os.path.join(SCRIPTS_PATH, "internal")
SCRIPTS_CUSTOM_PATH = os.path.join(SCRIPTS_PATH, "custom")


# MODULES
MODULES_PATH = os.path.join(ROOT_PATH, "modules")

MODULES_INTERNAL_PATH = os.path.join(MODULES_PATH, "internal")
MODULES_CUSTOM_PATH = os.path.join(MODULES_PATH, "custom")


# STORAGE
STORAGE_PATH = os.path.join(ROOT_PATH, "storage")

STORAGE_INTERNAL_PATH = os.path.join(STORAGE_PATH, "internal")
STORAGE_CUSTOM_PATH = os.path.join(STORAGE_PATH, "custom")


# PERSONALITY
PERSONALITY_PATH = os.path.join(ROOT_PATH, "modules/personality")

PERSONALITY_CUSTOM_PATH = os.path.join(PERSONALITY_PATH, "custom")
PERSONALITY_INTERNAL_PATH = os.path.join(PERSONALITY_PATH, "internal")


# OTHER
HELP_PATH = os.path.join(ROOT_PATH, "help")


# It is ok to hard-code this if you have issues
PYTHON_COMMAND = get_python_command()
PIP_COMMAND = get_pip_command()
