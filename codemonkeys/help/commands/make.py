from codemonkeys.defs import nl
from codemonkeys.utils.monk.theme_functions import print_t, print_table

"""Help script for the `make` command."""

print_t(f"Make Command Help{nl}", "important")

print_t("The `make` command creates a new command, automation, or barrel entity by copying an example entity and renaming based on the input parameters. "
        f"It is required to specify the entity type (command, automation, or barrel) and entity name in kebab-case (e.g. entity-name). This is useful for quickly creating new command files.{nl}")

print_t(f"Usage: `monk make [entity_type] [entity_name]`{nl}", "info")

USAGE_EXAMPLES_TABLE = {
    "headers": [
        "Entity Type",
        "Entity Name",
        "Command",
        "Resultant File"
    ],
    "show_headers": True,
    "rows": [
        [
            "command",
            "test-command",
            "monk make command test-command",
            "test-command.py - created under the command's path"
        ],
        [
            "automation",
            "example-automation",
            "monk make automation example-automation",
            "example-automation.py - created under the automation's path"
        ],
        [
            "barrel",
            "default-barrel",
            "monk make barrel default-barrel",
            "default-barrel.py - created under the barrel's path"
        ],
    ]
}

print_table(USAGE_EXAMPLES_TABLE, "Usage Examples")

print()
print_t("Important: If the specified entity_name isn't in a valid format (kebab-case), the command will raise a ValueError.","warning")
