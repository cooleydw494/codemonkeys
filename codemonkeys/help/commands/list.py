from codemonkeys.utils.monk.theme_functions import print_t, print_table
from codemonkeys.entities.command import Command
from codemonkeys.defs import nl

print_t(f"List.py Help{nl}", "important")

print_t("The `list` command prints a structure of ongoing Monk file paths, "
        "allowing you to navigate and manage your projects with ease. "
        f"You can pass an optional 'all' argument to the command to have it print additional file paths.{nl}")

print_t(f"Usage: `monk list [--all]`{nl}", "info")


USAGE_EXAMPLES_TABLE = {
    "headers": [
        "Command",
        "Description"
    ],
    "show_headers": True,
    "rows": [
        [
            "monk list",
            "Lists the default file paths."
        ],
        [
            "monk list --all",
            "Lists the base file paths, as well as any optional paths (such as Automations and Barrels)."
        ],
    ]
}

print_table(USAGE_EXAMPLES_TABLE, "Example Commands")

print()
print_t("Note: Be mindful when using the 'all' argument, as it could result in a large amount of output depending on the structure of your project.", "warning")

print_t("{nl}In the table above, you can see examples of how to use the `list` command. "
        "The first command lists the base file paths, while the second command lists all file paths, including optional ones like Automations and Barrels. "
        "Remember that the 'all' argument is not required but can be extremely useful if you want a more comprehensive list of your project's file paths. ", "info") 
