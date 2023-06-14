import os

from core.utils.get_python_command import get_python_command, get_pip_command

"""  PREFERENCES
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - """

# Improved readability for psychopaths
LIGHT_MODE_ENABLED = False
# Looks 👌 with very lil space, but you do you boo-boo
MAX_TERMINAL_WIDTH = 120

"""  USER-DEFINED PATHS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
*Always* begin user-defined PATHs with predefined PATHs.
Ex) TRANSLATION_AUTOMATIONS_PATH = os.path.join(AUTOMATIONS_USR_PATH, "translations") """

# <User-defined PATHs go here>


"""  PREDEFINED PATHS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Unless modifying the core itself, you probably shouldn't touch this. """

# ROOT_PATH
ROOT_PATH = os.path.dirname('..')

# ROOT_DIR_NAME
ROOT_DIR_NAME = os.path.basename(ROOT_PATH)

# MONK
MONK_PATH = os.path.join(ROOT_PATH, "monk")

# ENV
ENV_PATH = os.path.join(ROOT_PATH, ".env")

# CONFIG
CONFIG_PATH = os.path.join(ROOT_PATH, "config")

# MONKEY MANIFEST
MONKEY_MANIFEST_PATH = os.path.join(CONFIG_PATH, "monkey-manifest.yaml")

# MONKEY CONFIG DEFAULTS
MONKEY_CONFIG_DEFAULTS_PATH = os.path.join(CONFIG_PATH, "monkey-config-defaults.yaml")

# MONKEY CONFIGS
MONKEYS_PATH = os.path.join(CONFIG_PATH, "monkeys")

# STOR
STOR_PATH = os.path.join(ROOT_PATH, "stor")
STOR_CORE_PATH = os.path.join(STOR_PATH, "core")
STOR_TEMP_PATH = os.path.join(STOR_CORE_PATH, "temp")
STOR_MONK_PATH = os.path.join(STOR_CORE_PATH, "monk")
STOR_DEFAULTS_PATH = os.path.join(STOR_CORE_PATH, "defaults")

# DEFAULTS
ENV_DEFAULT_PATH = os.path.join(STOR_DEFAULTS_PATH, ".env.default")

# MODULES
MODULES_PATH = os.path.join(ROOT_PATH, "modules")

# CORE (framework)
CORE_PATH = os.path.join(ROOT_PATH, "core")
CORE_CONFIG_MGMT_PATH = os.path.join(CORE_PATH, "config_mgmt")

# ENV CLASS
ENV_CLASS_PATH = os.path.join(CORE_CONFIG_MGMT_PATH, "env", "env_class.py")
MONKEY_CONFIG_CLASS_PATH = os.path.join(CORE_CONFIG_MGMT_PATH, "monkey_config", "monkey_config_class.py")

# AUTOMATIONS
AUTOMATIONS_PATH = os.path.join(ROOT_PATH, "automations")

# BARRELS
BARRELS_PATH = os.path.join(ROOT_PATH, "barrels")

# MONK COMMANDS
COMMANDS_PATH = os.path.join(ROOT_PATH, "commands")


"""  MISC FRAMEWORK VARS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - """

# GET user's available python and pip commands
PYTHON_COMMAND = get_python_command()
PIP_COMMAND = get_pip_command()

# KEYWORDS (bold in CLI prints)
KEYWORDS = (lambda words: sorted(words, key=len, reverse=True))([
    'pseudo-package', 'entity types', 'defs.py', 'CodeMonkeys', 'automations', 'action flags', 'entity type',
    'barrels', 'modules', 'commands', 'monkeys', 'actions', 'barrel', 'module', 'action flag', 'automation', 'command',
    'monkey', 'types', 'pack', 'cli', 'monk'])

TOKEN_UNCERTAINTY_BUFFER = 10

# OS-agnostic newline characters
nl = os.linesep
nl2 = nl * 2


# prop or empty string helper
def _or(obj_or_class_prop, default=''):
    try:
        return obj_or_class_prop
    except AttributeError:
        return default
