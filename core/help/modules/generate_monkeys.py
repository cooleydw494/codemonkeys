
from core.utils.monk.theme.theme_functions import print_t, print_table

def generate_monkeys_help():
    print_t("Generate Monkeys Help", "important")
    print_t("The generate_monkeys module is used within the CodeMonkeys framework to maintain "
            "up-to-date monkey configurations, based on the monkey-manifest.yaml file. This module "
            "is responsible for creating and updating monkey configurations, as well as archiving "
            "previous configurations in a .history folder.", "info")

    print_t("Usage:", "input")
    print_t("To use the generate_monkeys module within the CodeMonkeys framework, simply import "
            "the generate_monkeys function and call it as needed.", "info")

    print_t("from generate_monkeys import generate_monkeys", "file")
    print_t("generate_monkeys()", "file")

    print_t("Note that the module expects a valid monkey-manifest.yaml file present in the "
            "config_mgmt folder for proper execution. Ensure you have a correctly formatted "
            "monkey-manifest.yaml file before running this module.", "tip")

    EXAMPLES_TABLE = {
        "headers": [
            "Configuration Example",
            "Description"
        ],
        "show_headers": True,
        "rows": [
            [
                "generate_monkeys()",
                "Generates and updates monkey configurations based on the monkey-manifest.yaml file"
            ],
        ]
    }
    print_table(EXAMPLES_TABLE, "Usage Examples")

generate_monkeys_help()
