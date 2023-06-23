from codemonkeys.utils.monk.theme_functions import print_t, print_table


def main():
    print_t("List Processes Help", "important")
    print_t("The `list-processes` command provides an overview of all ongoing Monk processes, their process IDs (PIDs),"
            "and commands to kill the respective processes. This is useful for managing and controlling Monk-related"
            "tasks and ensuring the smooth operation of the framework.")

    print_t("monk list-processes", "input")

    print_t("Usage:", "info")
    print_t("1. Execute `monk list-processes` to display a table with detailed information", "info")
    print_t("2. Use the provided kill commands to terminate a specific Monk process if needed", "info")

    print_t("Example of a table displayed after running `monk list-processes`:", "tip")

    USAGE_EXAMPLES_TABLE = {
        "headers": [
            "PID",
            "Command",
            "Kill Command"
        ],
        "show_headers": True,
        "rows": [
            [
                "1234",
                "monk add-monkey",
                "kill 1234"
            ],
            [
                "4567",
                "monk -a Default",
                "kill 4567"
            ],
        ]
    }

    print_table(USAGE_EXAMPLES_TABLE, "Usage")

    print_t("Important: Always exercise caution when terminating processes to avoid disrupting your workspace.", "warning")
