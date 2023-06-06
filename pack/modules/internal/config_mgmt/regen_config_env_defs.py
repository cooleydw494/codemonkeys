from definitions import STORAGE_DEFAULTS_PATH, ROOT_PATH, MODULES_CONFIG_MGMT_PATH
from pack.modules.internal.config_mgmt.update_env_class import update_env_class
from pack.modules.internal.config_mgmt.update_env_defaults import update_env_defaults
from pack.modules.internal.config_mgmt.update_monkey_config_class import update_monkey_config_class

import os


def regenerate_config_env_defs():

    ENV_PATH = os.path.join(ROOT_PATH, ".env")
    ENV_DEFAULTS_PATH = os.path.join(STORAGE_DEFAULTS_PATH, ".env.default")
    ENV_CLASS_PATH = os.path.join(MODULES_CONFIG_MGMT_PATH, "env_class.py")
    MONKEY_CONFIG_DEFAULTS_PATH = os.path.join(STORAGE_DEFAULTS_PATH, "monkey-config-defaults.yaml")
    MONKEY_CONFIG_CLASS_PATH = os.path.join(MODULES_CONFIG_MGMT_PATH, "monkey_config_class.py")

    # print_t("updating env defaults", 'special')
    update_env_defaults()

    # print_t("updating env class", 'special')
    update_env_class()

    # print_t("updating monkey config class", 'special')
    update_monkey_config_class()
