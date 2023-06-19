
from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Monkey Config Validations Summary", "important")
    print_t(
        "The monkey_config_validations module provides various utility "
        "functions that are used throughout the CodeMonkeys framework. "
        "These functions are primarily responsible for validating paths, "
        "names, and other configuration settings used in the framework.",
        "info"
    )

    print_t("Important Functions", "special")

    print_t("- get_user_config_value(key: str, validate_func, hint='')", "input")
    print_t("  This function retrieves a configuration value from the user, then "
            "validates the input using the provided validation function.", "info")

    print_t("- validate_path(key, path: str) -> (str, None)", "input")
    print_t("  Validates if the provided path exists, and returns the absolute path "
            "if it does. Raises a TypeError if the path does not exist.", "info")

    print_t("- validate_monkey_name(key: str = 'Monkey Name', monkey_name: str = None) -> str", "input")
    print_t("  Validates that the provided monkey name contains only letters and hyphens.", "info")

    print_t("- validate_bool(key, value: bool) -> (bool, None)", "input")
    print_t("  Validates that the provided value is a boolean, and raises a TypeError "
            "if it is not.", "info")

    print_t("- validate_type(key, value, expected_type: type)", "input")
    print_t("  Validates that the provided value is of the expected type, and raises a TypeError "
            "if it is not.", "info")

    print_t("- validate_str(key, value)", "input")
    print_t("  Validates that the provided value is a string, and raises a TypeError "
            "if it is not.", "info")

    print_t("Usage Example", "special")
    print_t("The following example demonstrates how to use the get_user_config_value() "
            "function to receive input from the user and validate it:")
    
    example_code = (
        "from monkey_config_validations import get_user_config_value, validate_int\n\n"
        "def config_value_example():\n"
        "    user_int = get_user_config_value(\n"
        "        key='Enter a number',\n"
        "        validate_func=validate_int,\n"
        "        hint='Ex: 5'\n"
        "    )\n"
        "    print('You entered:', user_int)\n\n"
        "config_value_example()"
    )
    print_t(example_code, "file")

if __name__ == '__main__':
    main()
