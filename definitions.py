import os

from pack.modules.internal.utils.get_python_command import get_python_command, get_pip_command

"""
IMPORTANT - PLEASE READ!

The pack/definitions.py version of this file is a symlink (created in the setup.py script) to the root definitions.py.
This is to give the pack "pseudo-package" access to root definitions. See README.md for more on the pseudo-package.
This does have some implications on how to use it, but if you follow the rules below, you should be fine.

RULES:
1. *Always use ROOT_PATH to get other paths*, leaving the ROOT_PATH logic in this file untouched.
2. Do not change the base structure of the modules directory, or move the symlinked definitions.py file.
3. Unless you're modifying fundamental framework logic or changing the directory structure of CodeMonkeys...
   YOU REALLY SHOULDN'T BE EDITING THIS!
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

# MONKEYS (configs)
MONKEYS_PATH = os.path.join(ROOT_PATH, "monkeys")

MONKEY_MANIFEST_PATH = os.path.join(ROOT_PATH, "monkey-manifest.yaml")
MONKEYS_INTERNAL_PATH = os.path.join(MONKEYS_PATH, "internal")
MONKEYS_CUSTOM_PATH = os.path.join(MONKEYS_PATH, "custom")

# STORAGE
STORAGE_PATH = os.path.join(ROOT_PATH, "storage")

STORAGE_INTERNAL_PATH = os.path.join(STORAGE_PATH, "internal")
STORAGE_CUSTOM_PATH = os.path.join(STORAGE_PATH, "custom")

# PSEUDO_PACKAGE
PSEUDO_PACKAGE_PATH = os.path.join(ROOT_PATH, "pack")

# MODULES
MODULES_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "modules")

MODULES_INTERNAL_PATH = os.path.join(MODULES_PATH, "internal")
MODULES_CUSTOM_PATH = os.path.join(MODULES_PATH, "custom")

# AUTOMATIONS
AUTOMATIONS_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "automations")

AUTOMATIONS_INTERNAL_PATH = os.path.join(AUTOMATIONS_PATH, "internal")
AUTOMATIONS_CUSTOM_PATH = os.path.join(AUTOMATIONS_PATH, "custom")

# BARRELS
BARRELS_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "barrels")

BARRELS_INTERNAL_PATH = os.path.join(BARRELS_PATH, "internal")
BARRELS_CUSTOM_PATH = os.path.join(BARRELS_PATH, "custom")

# MONK COMMANDS
COMMANDS_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "commands")

COMMANDS_INTERNAL_PATH = os.path.join(COMMANDS_PATH, "internal")
COMMANDS_CUSTOM_PATH = os.path.join(COMMANDS_PATH, "custom")

# It is ok to hard-code this if you have issues
PYTHON_COMMAND = get_python_command()
PIP_COMMAND = get_pip_command()
