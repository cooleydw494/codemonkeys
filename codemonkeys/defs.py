import os

from codemonkeys.utils.defs_utils import find_project_root

"""  PREDEFINED FRAMEWORK INSTANCE PATHS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  """

ROOT_PATH = find_project_root()

AUTOMATIONS_PATH = os.path.join(ROOT_PATH, "automations")
BARRELS_PATH = os.path.join(ROOT_PATH, "barrels")
COMPOSABLES_PATH = os.path.join(ROOT_PATH, "builders")
COMMANDS_PATH = os.path.join(ROOT_PATH, "commands")

ENV_PATH = os.path.join(ROOT_PATH, ".env")
CONFIG_PATH = os.path.join(ROOT_PATH, "config")
MONKEYS_PATH = os.path.join(CONFIG_PATH, 'monkeys')
MONKEY_CONFIG_DEFAULTS_PATH = os.path.join(CONFIG_PATH, 'monkey-config-defaults.yaml')

FRAMEWORK_CONFIG_PATH = os.path.join(CONFIG_PATH, 'framework')
THEME_CONFIG_PATH = os.path.join(FRAMEWORK_CONFIG_PATH, 'theme.py')
ENV_CLASS_PATH = os.path.join(FRAMEWORK_CONFIG_PATH, "env.py")
MONKEY_CONFIG_CLASS_PATH = os.path.join(FRAMEWORK_CONFIG_PATH, "monkey_config.py")

STOR_PATH = os.path.join(ROOT_PATH, "stor")
TEMP_PATH = os.path.join(STOR_PATH, "temp")

"""  'GLOBAL' HELPERS/VARIABLES
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  """

TOKEN_UNCERTAINTY_BUFFER = 10

# OS-agnostic newline characters
nl = os.linesep
nl2 = nl * 2
content_sep = '```'


# prop or empty string helper
def _or(obj_or_class_prop, default=''):
    try:
        return obj_or_class_prop
    except AttributeError:
        return default
