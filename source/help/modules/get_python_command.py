
from source.utils.monk.theme.theme_functions import print_t, print_table


def main():
    print_t("get__command Module Help", "important")
    print_t("This module provides a way to set a reliable, globally-available PYTHON_COMMAND and PIP_COMMAND,"
            " by finding the first valid  and pip commands available in the system from a predefined list.")

    print_t("In the CodeMonkeys framework, get__command is imported into defs.py to set the PYTHON_COMMAND and PIP_COMMAND,"
            " which are used throughout the project for consistent version usage and better compatibility.", "info")

    FUNCTIONS_TABLE = {
        "headers": [
            "Function",
            "Description",
            "Example Usage"
        ],
        "show_headers": True,
        "rows": [
            [
                "get__command()",
                "Return the first valid  command from list",
                "PYTHON_COMMAND = get__command()"
            ],
            [
                "get_pip_command()",
                "Return the first valid pip command from list",
                "PIP_COMMAND = get_pip_command()"
            ],
        ]
    }

    print_table(FUNCTIONS_TABLE, "Functions")

    print_t("Note: If no valid command is found, the script will print a suggestion to either add one of the predefined commands to your path, "
            "or manually set the respective command in defs.py.", "warning")
    print_t("\nExample list of commands to check in order:", "info")
    print_t("\nPython commands: 3, 3.11, 3.10, 3.9, 3.8, 3.7, 3.6, ", "file")
    print_t("\nPip commands: pip3, pip", "file")
