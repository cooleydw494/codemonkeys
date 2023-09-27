from codemonkeys.utils.monk.theme_functions import print_t, print_table
from codemonkeys.defs import nl

"""Help script for the `list-processes` command."""

print_t(f"List Processes Help{nl}", "important")

print_t("The `list-processes` command will print a table of ongoing Monk processes, their process IDs (PIDs), "
        f"and kill commands. This is useful for managing long-running CLI runnable entities such as Automations.{nl}")

print_t(f"Usage: `monk list-processes`{nl}", "info")


USAGE_EXAMPLES_TABLE = {
    "headers": [
        "PID",
        "Command",
        "Kill Command"
    ],
    "show_headers": True,
    "rows": [
        [
            "4432",
            "monk gpt-models-info --update",
            "kill 4432"
        ],
        [
            "1234",
            "monk -b NotatePrivateMethods",
            "kill 1234"
        ],
        [
            "4567",
            "monk -a Default",
            "kill 4567"
        ],
    ]
}

print_table(USAGE_EXAMPLES_TABLE, "Example Output")

print()
print_t("Important: Always exercise caution when terminating processes.","warning")
