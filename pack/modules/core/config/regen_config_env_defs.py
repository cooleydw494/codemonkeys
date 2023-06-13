# from definitions import STOR_DEFAULTS_PATH, ROOT_PATH, MODULES_CONFIG_MGMT_PATH
from pack.modules.core.config.env.update_env_class import update_env_class
from pack.modules.core.config.monkey_config.update_monkey_config_class import update_monkey_config_class
from pack.modules.core.utils.monk_helpers.generate_monkeys import generate_monkeys


def regenerate_config_env_defs():

    update_env_class()

    update_monkey_config_class()

    generate_monkeys()
