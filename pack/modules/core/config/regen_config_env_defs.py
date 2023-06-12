# from definitions import STOR_DEFAULTS_PATH, ROOT_PATH, MODULES_CONFIG_MGMT_PATH
from pack.modules.core.config.env.update_env_class import update_env_class
from pack.modules.core.config.monkey_config.update_monkey_config_class import update_monkey_config_class


def regenerate_config_env_defs():

    # print_t("updating env class", 'special')
    update_env_class()

    # print_t("updating monkey config class", 'special')
    update_monkey_config_class()
