
from codemonkeys.utils.monk.theme_functions import print_t, print_table


def main():
    print_t("Add-Monkey Help", "important")
    print_t("This script allows you to create a new monkey configuration and add it to the 'monkey-manifest.yaml' file. "
            "The 'monk add-monkey' command will guide you through a series of prompts for entering your monkey's settings."
            " If a monkey with the specified name already exists, you will be prompted to confirm the overwrite.", "info")

    print_t("monk add-monkey", "input")

    USAGE_EXAMPLES_TABLE = {
        "headers": [
            "Description",
            "Command"
        ],
        "show_headers": True,
        "rows": [
            [
                "Add a new monkey configuration",
                "monk add-monkey"
            ],
            [
                "Add a new monkey configuration with a specific name",
                "monk add-monkey --monkey my-custom-monkey"
            ],
        ]
    }

    print_table(USAGE_EXAMPLES_TABLE, "Usage")
