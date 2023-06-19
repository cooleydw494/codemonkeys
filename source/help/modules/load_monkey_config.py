from source.utils.monk.theme.theme_functions import print_t


def main():
    print_t("Load Monkey Config Help", "important")
    print_t("The load_monkey_config module within the CodeMonkeys framework is responsible for "
            "loading and managing the Monkey configuration. This module allows users to set, "
            "get, and load Monkey configurations to streamline and optimize their automated tasks.")

    print_t("Functions", "success")

    print_t("1. set_loaded_monkey(given_monkey_name: str) -> None:", "info")
    print_t("This function sets the given_monkey_name as the loaded Monkey in the framework and "
            "persists the name in a local storage file.")

    print_t("2. get_loaded_monkey() -> str or None:", "info")
    print_t("This function returns the name of the currently loaded Monkey from local storage. "
            "If there is no loaded Monkey, it returns None.")

    print_t("3. load_monkey_config(given_monkey_name=None) -> MonkeyConfig:", "info")
    print_t("This function loads a MonkeyConfig object based on the given_monkey_name parameter. "
            "If given_monkey_name is not provided, the function will attempt to use the "
            "currently loaded Monkey. If there's no loaded Monkey, it prompts the user to "
            "provide a new Monkey name.")

    print_t("Usage Example", "success")
    print_t("To load a Monkey configuration named 'MyMonkey', you can use the following code snippet:", "tip")
    print_t("from load_monkey_config import load_monkey_config\n"
            "monkey_config = load_monkey_config('MyMonkey')", "file")


if __name__ == '__main__':
    main()
