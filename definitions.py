import os

from modules.internal.utils.get_python_command import get_python_command, get_pip_command

# Set a python command that can be called in subprocesses with confidence
# This is a convenience that works for most, and if it doesn't support your needs, just hard-code it here.
PYTHON_COMMAND = get_python_command()
PIP_COMMAND = get_pip_command()


# ROOT
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR_NAME = os.path.basename(ROOT_PATH)


# MONK
MONK_PATH = os.path.join(ROOT_PATH, "monk")


# CODE_MONKEYS dirname
PSEUDO_PACKAGE_PATH = os.path.join(ROOT_PATH, ROOT_DIR_NAME.replace("-", "_"))
PSEUDO_PACKAGE_DIR_NAME = os.path.basename(PSEUDO_PACKAGE_PATH)


# MONKEYS
MONKEYS_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "monkeys")

MONKEYS_INTERNAL_PATH = os.path.join(MONKEYS_PATH, "internal")
MONKEYS_CUSTOM_PATH = os.path.join(MONKEYS_PATH, "custom")


# AUTOMATIONS
AUTOMATIONS_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "scripts/automations")

AUTOMATIONS_INTERNAL_PATH = os.path.join(AUTOMATIONS_PATH, "internal")
AUTOMATIONS_CUSTOM_PATH = os.path.join(AUTOMATIONS_PATH, "custom")


# SCRIPTS
SCRIPTS_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "scripts")

SCRIPTS_INTERNAL_PATH = os.path.join(SCRIPTS_PATH, "internal")
SCRIPTS_CUSTOM_PATH = os.path.join(SCRIPTS_PATH, "custom")


# MODULES
MODULES_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "modules")

MODULES_INTERNAL_PATH = os.path.join(MODULES_PATH, "internal")
MODULES_CUSTOM_PATH = os.path.join(MODULES_PATH, "custom")


# STORAGE
STORAGE_PATH = os.path.join(ROOT_PATH, "storage")

STORAGE_INTERNAL_PATH = os.path.join(STORAGE_PATH, "internal")
STORAGE_CUSTOM_PATH = os.path.join(STORAGE_PATH, "custom")


# PERSONALITY
PERSONALITY_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "personality")

PERSONALITY_CUSTOM_PATH = os.path.join(PERSONALITY_PATH, "custom")
PERSONALITY_INTERNAL_PATH = os.path.join(PERSONALITY_PATH, "internal")


# OTHER
HELP_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "help")
