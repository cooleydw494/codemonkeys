from codemonkeys.entities.command import Command


class PrintMonkey(Command):

    def run(self) -> None:

        from codemonkeys.utils.monk.theme_functions import print_t, print_table
        from codemonkeys.defs import nl

        """Help script for the `print-monkey` command."""

        print_t(f"Print Monkey Help{nl}", "important")

        print_t("The `print-monkey` command is a debugging tool that prints the final computed properties of a "
                "specified Monkey. This can be especially useful for checking the state of a Monkey during "
                f"implementation and testing phases.{nl}")

        print_t(f"Usage: `monk print-monkey [monkey-name]`{nl}", "info")

        USAGE_EXAMPLES_TABLE = {
            "headers": [
                "Monkey Name",
                "Command",
                "Monkey Details Output"
            ],
            "show_headers": True,
            "rows": [
                [
                    "MyMonkey",
                    "monk print-monkey MyMonkey",
                    "[Here will be displayed the detailed properties of MyMonkey]"
                ],
            ]
        }

        print_table(USAGE_EXAMPLES_TABLE, "Example Usage")

        print()
