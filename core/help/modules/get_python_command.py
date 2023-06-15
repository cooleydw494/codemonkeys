
from core.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Get Python Command Module Help", "important")
    print_t("This module, 'get__command', is designed to set reliable, globally-available "
            "PYTHON_COMMAND and PIP_COMMAND variables for the CodeMonkeys framework.", "info")

    print_t("Functionality", "special")
    print_t("- get__command(): Determines a valid Python command by testing a predefined list "
            "of common Python commands and returns the first valid one.")
    print_t("- get_pip_command(): Determines a valid Pip command by testing a predefined list of "
            "common Pip commands and returns the first valid one.")
    print_t("- test_command(command): Returns 'True' if the given command is valid, and 'False' "
            "otherwise. Utilizes the '--version' flag to test commands.")

    print_t("Usage", "special")
    print_t("To use 'get__command' in other modules within the CodeMonkeys framework, "
            "simply import the desired functions from the module.", "info")
    print_t("Example:", "input")
    print_t("from get__command import get__command, get_pip_command")
    print_t("Then, simply call the function to get a valid Python or Pip command as needed.", "info")

if __name__ == "__main__":
    main()
