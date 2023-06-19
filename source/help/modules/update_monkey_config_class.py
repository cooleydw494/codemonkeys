
from source.utils.monk.theme.theme_functions import print_t


def main():
    print_t("Update Monkey Config Class Help", "important")
    print_t("The update_monkey_config_class module is designed to automate the"
            " process of updating the MonkeyConfig class in the CodeMonkeys framework."
            " This module fetches the latest default configuration values and generates"
            " type-safe properties and validations for each configuration item.")

    print_t("The main function in this module, `update_monkey_config_class`, does the following:", "info")
    print_t("1. Fetches the latest default configuration using `get_monkey_config_defaults`", "info")
    print_t("2. Formats properties and validations based on the fetched data", "info")
    print_t("3. Updates the MonkeyConfig class with the new configuration values, formatted properties, and validations", "info")

    print_t("Example usage:", "input")
    print_t("from update_monkey_config_class import update_monkey_config_class", "file")
    print_t("update_monkey_config_class()", "file")

    print_t("Note:", "tip")
    print_t("Before running this module, ensure that all the markers, such as MONKEY_CONFIG_PROPS_START and"
            " MONKEY_CONFIG_VALIDATIONS_START, are correctly placed within the MonkeyConfig class.")
    print_t("This module should be used whenever there are updates to the default configuration"
            " to maintain consistency and type-safety across the framework.")

if __name__ == "__main__":
    main()
