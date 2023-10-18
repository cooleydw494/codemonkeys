from codemonkeys.defs import nl
from codemonkeys.entities.command import Command
from codemonkeys.utils.monk.theme_functions import print_t, print_table


class GptModelsInfo(Command):

    """Help script for the `gpt-models-info` command."""

    def run(self):

        print_t(f"Gpt-Models-Info Help{nl}", "important")

        print_t("The `gpt-models-info` command retrieves and displays information about available GPT Models. "
                f"It collects the data either from the cache or updates the info cache if specified by user. "
                f"This is useful for identifying the available GPT models in a clear and convenient format.{nl}")

        print_t(f"Usage: `monk gpt-models-info` or `monk gpt-models-info --update`{nl}", "info")

        USAGE_EXAMPLES_TABLE = {
            "headers": [
                "Command",
                "Description"
            ],
            "show_headers": True,
            "rows": [
                [
                    "monk gpt-models-info",
                    "Fetches GPT model information from cache and displays"
                ],
                [
                    "monk gpt-models-info --update",
                    "Updates the GPT Model Info Cache and displays the refreshed list"
                ],
            ]
        }

        print_table(USAGE_EXAMPLES_TABLE, "Usage Examples")

        print()
        print_t("Note: Call `monk gpt-models-info --update` whenever you need the most up-to-date list of GPT models.",
                "special")
