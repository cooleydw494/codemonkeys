import os

from pack.modules.internal.utils.get_python_command import get_python_command, get_pip_command

"""  PREFERENCES
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - """

# Improved readability for everyone's favorite psychopaths
LIGHT_MODE_ENABLED = False
# Looks 👌 with very lil space, but you do you boo-boo
MAX_TERMINAL_WIDTH = 120

"""  USER-DEFINED PATHS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
*Always* begin user-defined PATHs with predefined PATHs.
Ex) TRANSLATION_AUTOMATIONS_PATH = os.path.join(AUTOMATIONS_CUSTOM_PATH, "translations") """

# <User-defined PATHs go here>


"""  PREDEFINED PATHS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Unless modifying the framework itself, you probably shouldn't touch this. """

# ROOT_PATH
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# ROOT_DIR_NAME
ROOT_DIR_NAME = os.path.basename(ROOT_PATH)

# MONK
MONK_PATH = os.path.join(ROOT_PATH, "monk")

# ENV
ENV_PATH = os.path.join(ROOT_PATH, "env")

# MONKEYS (configs)
MONKEYS_PATH = os.path.join(ROOT_PATH, "monkeys")
MONKEY_MANIFEST_PATH = os.path.join(ROOT_PATH, "monkey-manifest.yaml")
MONKEYS_INTERNAL_PATH = os.path.join(MONKEYS_PATH, "internal")
MONKEYS_CUSTOM_PATH = os.path.join(MONKEYS_PATH, "custom")

# STORAGE
STORAGE_PATH = os.path.join(ROOT_PATH, "storage")
STORAGE_INTERNAL_PATH = os.path.join(STORAGE_PATH, "internal")
STORAGE_TEMP_PATH = os.path.join(STORAGE_INTERNAL_PATH, "temp")
STORAGE_MONK_PATH = os.path.join(STORAGE_INTERNAL_PATH, "monk")
STORAGE_DEFAULTS_PATH = os.path.join(STORAGE_INTERNAL_PATH, "defaults")

# DEFAULTS
ENV_DEFAULT_PATH = os.path.join(STORAGE_DEFAULTS_PATH, ".env.default")

# PSEUDO_PACKAGE
PSEUDO_PACKAGE_PATH = os.path.join(ROOT_PATH, "pack")

# MODULES
MODULES_PATH = os.path.join(PSEUDO_PACKAGE_PATH, "modules")
MODULES_INTERNAL_PATH = os.path.join(MODULES_PATH, "internal")
MODULES_CUSTOM_PATH = os.path.join(MODULES_PATH, "custom")
MODULES_CONFIG_MGMT_PATH = os.path.join(MODULES_INTERNAL_PATH, "config_mgmt")

# ENV CLASS
ENV_CLASS_PATH = os.path.join(MODULES_CONFIG_MGMT_PATH, "env_class.py")
MONKEY_CONFIG_CLASS_PATH = os.path.join(MODULES_CONFIG_MGMT_PATH, "monkey_config_class.py")

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

"""  MISC FRAMEWORK VARS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - """

# GET user's available python and pip commands
PYTHON_COMMAND = get_python_command()
PIP_COMMAND = get_pip_command()

# KEYWORDS (bold in CLI prints)
KEYWORDS = (lambda words: sorted(words, key=len, reverse=True))([
    'pseudo-package', 'entity types', 'definitions.py', 'CodeMonkeys', 'automations', 'action flags', 'entity type',
    'barrels', 'modules', 'commands', 'monkeys', 'actions', 'barrel', 'module', 'action flag', 'automation', 'command',
    'monkey', 'types', 'pack', 'cli', 'monk'])
