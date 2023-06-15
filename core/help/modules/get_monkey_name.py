from core.utils.monk.theme.theme_functions import print_t


def main():
    print_t("Get Monkey Name Module Help", "important")
    print_t("This module helps in selecting and retrieving the monkey name and its corresponding configuration "
            "file path. It offers the functionality to list all available monkeys, check if a monkey configuration "
            "exists, and gives users the ability to select or input monkey names.")

    print_t("List all monkey configs:", "tip")
    print_t("Use the function list_monkeys() which returns a list of all monkey names.")

    print_t("Retrieve monkey name and config_mgmt path:", "tip")
    print_t("Use the function get_monkey_name(given_monkey_name, prompt_user) which accepts two parameters:"
            "\n  1. given_monkey_name: default is None, provide a monkey name if known."
            "\n  2. prompt_user: default is False, set it to True to prompt the user to select a monkey.")

    print_t("Example usage:", "input")
    print_t("from get_monkey_name import list_monkeys, get_monkey_name")
    print_t("\n# List all monkeys")
    print_t("all_monkeys = list_monkeys()")
    print_t("print(all_monkeys)")

    print_t("\n# Get a specific monkey by name (assuming 'default' monkey exists)")
    print_t("monkey_name, config_path = get_monkey_name('default')")
    print_t("print(f'Monkey Name: {monkey_name}, Config Path: {config_path}')")

    print_t("\n# Prompt user to select a monkey")
    print_t("monkey_name, config_path = get_monkey_name(prompt_user=True)")
    print_t("print(f'Monkey Name: {monkey_name}, Config Path: {config_path}')")

main()