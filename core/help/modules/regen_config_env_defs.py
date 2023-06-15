
from core.utils.monk.theme.theme_functions import print_t


def main():
    print_t("regen_config_env_defs Help", "important")
    print_t("The regen_config_env_defs module is a part of the CodeMonkeys framework and is designed to be used within the Monk CLI.", "info")

    print_t("regenerate_config_env_defs() is the main function of the module that performs the following tasks:", "info")

    print_t("1. Update the environment class (update_env_class) within the definitions by regenerating its definition file using the current environment variables.", "tip")

    print_t("2. Update the Monkey configuration class (update_monkey_config_class) by regenerating its definition file using the current configuration variables.", "tip")

    print_t("3. Generate the monks (generate_monkeys), i.e., update the list of available automations, barrels, and other entities in the framework based on the current environment.", "tip")

    print_t("The regen_config_env_defs module is a crucial part of the CodeMonkeys ecosystem, as it helps to maintain the framework's consistency and ensures that any changes to the environment or configuration are propagated throughout the system.", "warning")

    print_t("Example usage within a script:", "input")
    print_t("from regen_config_env_defs import regenerate_config_env_defs", "file")
    print_t("regenerate_config_env_defs()", "file")
