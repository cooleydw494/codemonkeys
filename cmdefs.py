import os

from __init__ import __version__

VERSION = __version__

"""  CORE PATHS

This is a framework-level PATH definitions file.
It is separate from defs.py for usage in monk-new, when there is no project ROOT_PATH.
It is also used anywhere else a framework-level path is needed.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  """
# CORE ROOT PATH
CM_ROOT_PATH = os.path.dirname(__file__)

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
# CM CONFIG
CM_CONFIG_PATH = os.path.join(CM_PATH, "config")

# ENV CLASS
CM_ENV_CLASS_PATH = os.path.join(CM_CONFIG_PATH, "env_class.py")
# MONKEY CONFIG CLASS
CM_MONKEY_CONFIG_CLASS_PATH = os.path.join(CM_CONFIG_PATH, "monkey_config_class.py")
# THEME CONFIG
CM_THEME_CONFIG_PATH = os.path.join(CM_CONFIG_PATH, 'theme.py')

# HELP
CM_HELP_PATH = os.path.join(CM_PATH, "help")

# STOR CORE
CM_STOR_PATH = os.path.join(CM_ROOT_PATH, "stor")
CM_STOR_TEMP_PATH = os.path.join(CM_STOR_PATH, "temp")
CM_STOR_MONK_PATH = os.path.join(CM_STOR_PATH, "monk")
CM_STOR_DEFAULTS_PATH = os.path.join(CM_STOR_PATH, "defaults")

# DEFAULTS
CM_ENV_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, ".env.default")
CM_MONKEY_MANIFEST_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, "monkey-manifest.yaml")
CM_MONKEY_CONFIG_DEFAULTS_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, "monkey-config-defaults.yaml")
CM_CONTEXT_FILE_EXAMPLE_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, 'context-file.txt')
CM_DEFAULT_AUTOMATION_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, 'DefaultAutomation.py')
CM_GITIGNORE_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, '.default-gitignore')
CM_README_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, 'DEFAULT-README.md')

# ENTITY EXAMPLES
CM_ENTITY_EXAMPLES_PATH = os.path.join(CM_STOR_PATH, "entity_examples")
CM_EXAMPLE_COMMAND_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, "example-command.py")
CM_EXAMPLE_AUTOMATION_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, "example-automation.py")
CM_EXAMPLE_BARREL_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, "example-barrel.py")
