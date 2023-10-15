from codemonkeys.defs import nl
from codemonkeys.entities.command import Command
from codemonkeys.utils.monk.theme_functions import print_t, print_table


class Make(Command):
    """Help command for the `make` command."""

    def run(self):
        print_t(f"Make Command{nl}", "important")

        print_t(
            "The `make` command creates a new entity, copying an example and renaming based on the input parameters.")

        print_t(f"Usage: `monk make [entity_type] [entity_name]`{nl}", "info")

        USAGE_EXAMPLES_TABLE = {
            "headers": [
                "Entity Type",
                "Entity Name",
                "Command",
                "Result"
            ],
            "show_headers": True,
            "rows": [
                [
                    "command",
                    "my-command",
                    "monk make command my-command",
                    "commands/my-command.py"
                ],
                [
                    "automation",
                    "my-automation",
                    "monk make automation my-automation",
                    "automations/my-automation.py"
                ],
                [
                    "barrel",
                    "my-barrel",
                    "monk make barrel my-barrel",
                    "barrels/my-barrel.py"
                ],
                [
                    "func",
                    "my_func",
                    "monk make func my_func",
                    "funcs/my_func.py"
                ],
                [
                    "monkey",
                    "my_monkey",
                    "monk make monkey my_monkey",
                    "monkeys/my_monkey.py"
                ]
            ]
        }

        print_table(USAGE_EXAMPLES_TABLE, "Usage Examples")
        print()
