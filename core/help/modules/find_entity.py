from core.utils.monk.theme.theme_functions import print_t

def main():
    print_t("find_entity.py Help", "important")
    print_t("This module provides useful functionality for finding and selecting entities within the "
            "CodeMonkeys framework. It uses a recursive name-matching logic to search for commands, "
            "automations, barrels, and modules.")
    
    print_t("Features and Usage", "special")
    print_t("1. find_entities: This function searches for entities within the specified "
            "entity_directory, based on user specified entity_name and entity_type.", "info")
    print_t("   Usage: find_entities(entity_directory: str, entity_name: str, entity_type: str) -> Generator", "input")

    print_t("2. user_select_entity: This function presents users with a list of entity_options and "
            "prompts users to select one. Returns the selected entity's path.", "info")
    print_t("   Usage: user_select_entity(prompt: str, "
            "entity_options: List[Tuple[str, int, int, str, str]]) -> str", "input")

    print_t("3. find_entity: This function takes in an entity_name and entity_type, searches for entities "
            "matching them, and returns the path of the selected entity. "
            "It internally uses find_entities and user_select_entity functions.", "info")
    print_t("   Usage: find_entity(entity_name: str, entity_type: str)", "input")

    print_t("4. print_partial_path: This function prints the given path with a more readable format.", "info")
    print_t("   Usage: print_partial_path(path: str)", "input")

    print_t("Example Usage", "special")
    print_t("Imagine you want to find the path of a specific CodeMonkeys command with the name 'example-command':", "info")
    print_t("   path = find_entity('example-command', 'command')", "input")
    print_t("This will search for the command within entities and return its path if found.", "info")