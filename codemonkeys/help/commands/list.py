from codemonkeys.defs import nl
from codemonkeys.entities.command import Command
from codemonkeys.utils.monk.theme_functions import print_t, print_table


class List(Command):

    def run(self):
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
