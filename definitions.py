import os

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
MONKEYS_CUSTOMIZABLE_PATH = os.path.join(MONKEYS_PATH, "customizable")


# AUTOMATIONS
AUTOMATIONS_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "scripts/automations")

AUTOMATIONS_INTERNAL_PATH = os.path.join(AUTOMATIONS_PATH, "internal")
AUTOMATIONS_CUSTOMIZABLE_PATH = os.path.join(AUTOMATIONS_PATH, "customizable")


# SCRIPTS
SCRIPTS_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "scripts")

SCRIPTS_INTERNAL_PATH = os.path.join(SCRIPTS_PATH, "internal")
SCRIPTS_CUSTOMIZABLE_PATH = os.path.join(SCRIPTS_PATH, "customizable")


# MODULES
MODULES_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "modules")

MODULES_INTERNAL_PATH = os.path.join(MODULES_PATH, "internal")
MODULES_CUSTOMIZABLE_PATH = os.path.join(MODULES_PATH, "customizable")


# STORAGE
STORAGE_PATH = os.path.join(ROOT_PATH, "storage")

STORAGE_INTERNAL_PATH = os.path.join(STORAGE_PATH, "internal")
STORAGE_CUSTOMIZABLE_PATH = os.path.join(STORAGE_PATH, "customizable")


# PERSONALITY
PERSONALITY_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "personality")

PERSONALITY_CUSTOMIZABLE_PATH = os.path.join(PERSONALITY_PATH, "customizable")
PERSONALITY_INTERNAL_PATH = os.path.join(PERSONALITY_PATH, "internal")


# OTHER
HELP_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "help")
