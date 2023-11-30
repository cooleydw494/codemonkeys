import os

# Version of the module
VERSION = '1.0.12'

"""
CORE PATHS

This is a framework-level PATH definitions file.
It is separate from defs.py for usage in monk-new, when there is no project ROOT_PATH.
It is also used anywhere else a framework-level path is needed.
"""

# Getting the root directory of the current script
CM_ROOT_PATH = os.path.dirname(__file__)

# Define important directory paths rooted in CM_ROOT_PATH
CM_BUILDERS_PATH = os.path.join(CM_ROOT_PATH, "builders")
CM_COMMANDS_PATH = os.path.join(CM_ROOT_PATH, "commands")
CM_FUNCS_PATH = os.path.join(CM_ROOT_PATH, "funcs")
CM_CONFIG_PATH = os.path.join(CM_ROOT_PATH, "config")
CM_HELP_PATH = os.path.join(CM_ROOT_PATH, "help")
CM_STOR_PATH = os.path.join(CM_ROOT_PATH, "stor")

# Define specific file paths in CM_CONFIG_PATH
CM_THEME_CONFIG_PATH = os.path.join(CM_CONFIG_PATH, 'theme.py')

# Define sub-directory paths in CM_STOR_PATH
CM_STOR_TEMP_PATH = os.path.join(CM_STOR_PATH, "temp")
CM_STOR_MONK_PATH = os.path.join(CM_STOR_PATH, "monk")
CM_STOR_DEFAULTS_PATH = os.path.join(CM_STOR_PATH, "defaults")
CM_STOR_SNIPPETS_PATH = os.path.join(CM_STOR_PATH, "snippets")
CM_BANNER_PATH = os.path.join(CM_STOR_SNIPPETS_PATH, 'banner.txt')

# Define default file paths in CM_STOR_DEFAULTS_PATH
CM_ENV_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, ".env")
CM_ENV_CLASS_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, "env.py")
CM_THEME_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, "theme.py")
CM_MONKEYS_DIR_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, "monkeys")
CM_AUTOMATIONS_DIR_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, 'automations')
CM_COMMANDS_DIR_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, 'commands')
CM_GITIGNORE_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, '._gitignore')
CM_DEFAULT_REQUIREMENTS_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, '_requirements.txt')
CM_README_DEFAULT_PATH = os.path.join(CM_STOR_DEFAULTS_PATH, 'README.md')

# Define example entity file paths in CM_STOR_PATH
CM_ENTITY_EXAMPLES_PATH = os.path.join(CM_STOR_PATH, "examples")
CM_EXAMPLE_COMMAND_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, "command.py")
CM_EXAMPLE_AUTOMATION_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, "default.py")
CM_EXAMPLE_BARREL_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, "barrel.py")
CM_EXAMPLE_FUNC_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, "func.py")
CM_EXAMPLE_MIXIN_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, 'mixin.py')
CM_CONTEXT_FILE_EXAMPLE_PATH = os.path.join(CM_ENTITY_EXAMPLES_PATH, 'context-file.txt')
