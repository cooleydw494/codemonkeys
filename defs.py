import os

from codemonkeys.utils.framework_utils import find_project_root
from codemonkeys.utils.get_python_command import get_python_command, get_pip_command


"""  PREDEFINED FRAMEWORK INSTANCE PATHS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  """

# ROOT_PATH
ROOT_PATH = find_project_root()

# AUTOMATIONS
AUTOMATIONS_PATH = os.path.join(ROOT_PATH, "automations")
# BARRELS
BARRELS_PATH = os.path.join(ROOT_PATH, "barrels")
# TASKS
TASKS_PATH = os.path.join(ROOT_PATH, "tasks")
# ABILITIES
ABILITIES_PATH = os.path.join(ROOT_PATH, "abilities")
# COMMANDS
COMMANDS_PATH = os.path.join(ROOT_PATH, "commands")

# ENV
ENV_PATH = os.path.join(ROOT_PATH, ".env")
# CONFIG
CONFIG_PATH = os.path.join(ROOT_PATH, "config")
# MONKEY MANIFEST
MONKEY_MANIFEST_PATH = os.path.join(CONFIG_PATH, 'monkey-manifest.yaml')
# MONKEY CONFIG DEFAULTS
MONKEY_CONFIG_DEFAULTS_PATH = os.path.join(CONFIG_PATH, 'monkey-config-defaults.yaml')

# FRAMEWORK CONFIG
FRAMEWORK_CONFIG_PATH = os.path.join(CONFIG_PATH, 'framework')
# ENV CLASS
ENV_CLASS_PATH = os.path.join(FRAMEWORK_CONFIG_PATH, "env_class.py")
# MONKEY CONFIG CLASS
MONKEY_CONFIG_CLASS_PATH = os.path.join(FRAMEWORK_CONFIG_PATH, "monkey_config_class.py")

# STOR
STOR_PATH = os.path.join(ROOT_PATH, "stor")

# MONKEY TEMP CONFIG FILES
MONKEYS_PATH = os.path.join(STOR_PATH, 'monkeys')


"""  CORE PATHS
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  """

# CORE ROOT PATH
CM_ROOT_PATH = os.path.dirname('.')

# CM PATH (root package)
CM_PATH = os.path.join(CM_ROOT_PATH, "codemonkeys")

# CM AUTOMATIONS
CM_AUTOMATIONS_PATH = os.path.join(CM_PATH, "automations")
# CM BARRELS
CM_BARRELS_PATH = os.path.join(CM_PATH, "barrels")
# CM TASKS
CM_TASKS_PATH = os.path.join(CM_PATH, "tasks")
# CM ABILITIES
CM_ABILITIES_PATH = os.path.join(CM_PATH, "abilities")
# CM COMMANDS
CM_COMMANDS_PATH = os.path.join(CM_PATH, "commands")

# HELP
CM_HELP_PATH = os.path.join(CM_PATH, "help")

# STOR CORE
CM_STOR_PATH = os.path.join(CM_ROOT_PATH, "stor")
CM_STOR_TEMP_PATH = os.path.join(CM_STOR_PATH, "temp")
CM_STOR_MONK_PATH = os.path.join(CM_STOR_PATH, "monk")
CM_STOR_DEFAULTS_PATH = os.path.join(CM_STOR_PATH, "defaults")

# DEFAULTS
ENV_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, ".env.default")


"""  'GLOBAL' HELPERS/VARIABLES
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  """

# GET user's available python and pip commands
PYTHON_COMMAND = get_python_command()
PIP_COMMAND = get_pip_command()

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
