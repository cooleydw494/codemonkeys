import os

from pkg_resources import resource_filename

VERSION = '0.2.3'

"""  CORE PATHS

This is a framework-level PATH definitions file.
It is separate from defs.py for usage in monk-new, when there is no project ROOT_PATH.
It is also used anywhere else a framework-level path is needed.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  """

CM_ROOT_PATH = os.path.dirname(__file__)

CM_AUTOMATIONS_PATH = os.path.join(CM_ROOT_PATH, "automations")
CM_BARRELS_PATH = os.path.join(CM_ROOT_PATH, "barrels")
CM_COMPOSABLES_PATH = os.path.join(CM_ROOT_PATH, "composables")
CM_ABILITIES_PATH = os.path.join(CM_ROOT_PATH, "abilities")
CM_COMMANDS_PATH = os.path.join(CM_ROOT_PATH, "commands")
CM_CONFIG_PATH = os.path.join(CM_ROOT_PATH, "config")
CM_HELP_PATH = os.path.join(CM_ROOT_PATH, "help")
CM_STOR_PATH = os.path.join(CM_ROOT_PATH, "stor")

CM_ENV_CLASS_PATH = os.path.join(CM_CONFIG_PATH, "env_class.py")
CM_MONKEY_CONFIG_CLASS_PATH = os.path.join(CM_CONFIG_PATH, "monkey_config_class.py")
CM_THEME_CONFIG_PATH = os.path.join(CM_CONFIG_PATH, 'theme.py')


CM_STOR_TEMP_PATH = os.path.join(CM_STOR_PATH, "temp")
CM_STOR_MONK_PATH = os.path.join(CM_STOR_PATH, "monk")
CM_STOR_DEFAULTS_PATH = os.path.join(CM_STOR_PATH, "defaults")
CM_STOR_SNIPPETS_PATH = os.path.join(CM_STOR_PATH, "snippets")

CM_ENV_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, ".env.default")
CM_MONKEY_MANIFEST_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, "monkey-manifest.yaml")
CM_MONKEY_CONFIG_DEFAULTS_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, "monkey-config-defaults.yaml")
CM_CONTEXT_FILE_EXAMPLE_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, 'context-file.txt')
CM_DEFAULT_AUTOMATION_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, 'default-automation.py')
CM_GITIGNORE_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, '.default-gitignore')
CM_DEFAULT_REQUIREMENTS_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, 'default-requirements.txt')
CM_README_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, 'DEFAULT-README.md')

CM_ENTITY_EXAMPLES_PATH = os.path.join(CM_STOR_PATH, "entity_examples")
CM_EXAMPLE_COMMAND_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, "example-command.py")
CM_EXAMPLE_AUTOMATION_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, "example-automation.py")
CM_EXAMPLE_BARREL_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, "example-barrel.py")
