from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Get Monkey Name Help", "important")
    print_t("The get_monkey_name module is a part of the CodeMonkeys framework. It helps in retrieving the name and "
            "corresponding config file path of a configuration from a list of available monkeys stored in the project's "
            "configuration folder (MONKEYS_PATH).")

    print_t("import get_monkey_name", "input")
    print_t("get_monkey_name.get_monkey_name(given_monkey_name, prompt_user)", "input")

    print_t("Parameters:", "special")
    print_t("- given_monkey_name: A name of the monkey configuration that may be provided.", 'info')
    print_t("- prompt_user: A boolean indicating whether to prompt the user to select a monkey from the available list "
             "or not. Defaults to False.", 'info')

    print_t("Return:", "special")
    print_t("A tuple containing the selected monkey name and its respective configuration file path.", 'info')

    print_t("Usage Example:", "tip")
    print_t("Example 1: Without any arguments", "info")
    print_t(">>> import get_monkey_name", "input")
    print_t(">>> name, config_path = get_monkey_name.get_monkey_name()", "input")
    print_t("This will first check for the default configuration, and if not found, it will prompt the user to select "
            "a monkey from the available list.", "info")

    print_t("Example 2: Providing a specific monkey name", "info")
    print_t(">>> import get_monkey_name", "input")
    print_t(">>> name, config_path = get_monkey_name.get_monkey_name(given_monkey_name='custom_monkey')", "input")
    print_t("This will try to fetch the 'custom_monkey' configuration, and if it doesn't exist, the user will be "
            "prompted to select a monkey from the available list.", "info")

    print_t("Example 3: Always prompt user to select monkey", "info")
    print_t(">>> import get_monkey_name", "input")
    print_t(">>> name, config_path = get_monkey_name.get_monkey_name(prompt_user=True)", "input")
    print_t("This will always prompt the user to select a monkey from the available list, regardless of whether "
            "a default configuration exists or not.", "info")
    
main()