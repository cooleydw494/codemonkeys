
from core.utils.monk.theme.theme_functions import print_t, print_table

def main():
    print_t("Handle Special Commands Module Help", "important")
    print_t("This module is responsible for handling special commands that are not entities within the "
            "CodeMonkeys framework. It manages non-entity actions such as toggling light mode, displaying the "
            "version of the CodeMonkeys framework, and listing available entities (commands, automations, barrels, and modules).")

    print_t("handle_special_commands(args, action, entity, entity_type)", "input")

    FUNCTION_USAGE_TABLE = {
        "headers": [
            "Argument",
            "Description"
        ],
        "show_headers": True,
        "rows": [
            [
                "args",
                "The parsed command line arguments (action, version, etc.)"
            ],
            [
                "action",
                "A string specifying the desired action (e.g. 'help', 'list', etc.)"
            ],
            [
                "entity",
                "A string that represents the name of the entity on which the action should be performed."
            ],
            [
                "entity_type",
                "A string that represents the type of the entity ('command', 'barrel', 'automation',"
                " or 'module')"
            ],
        ]
    }

    print_table(FUNCTION_USAGE_TABLE, "Function Arguments")

    print_t('monk handle_special_commands.py is found within the CodeMonkeys framework and is utilized'
            ' by various other components, making it a crucial part of the overall operation.', 'info')

main()
