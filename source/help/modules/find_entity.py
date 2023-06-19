
from source.utils.monk.theme.theme_functions import print_t

def main():
    print_t("Find Entity Help", "important")
    print_t("The find_entity module allows you to search for and interact with entities in the CodeMonkeys framework. "
            "Entities include commands, automations, barrels, modules, and source components. This module implements "
            "recursive name-matching logic to find the best match for a given entity name.")

    print_t("Usage:", "info")
    print_t("Import the find_entity module in your own scripts or use it via the Monk CLI.")
    print_t("Example:", "input")
    print_t("from find_entity import find_entity")
    print_t("module_path = find_entity('some_module_name', 'module')")

    print_t("Functions", "info")
    print_t("user_select_entity(prompt, entity_options):", "tip")
    print_t("Given a list of entity options, prompts the user to select an entity and returns the selected entity's path.")
    
    print_t("find_entities(entity_directory, entity_name, entity_type):", "tip")
    print_t("A generator function that finds matching entities in the given entity directory and returns the results "
            "as a list of tuples with the name, priority, levenshtein distance, entity type, and full path information.")

    print_t("find_entity(entity_name, entity_type, path_override=None):", "tip")
    print_t("Finds the best matching entity for the given name and type, and returns its path. Can also take an optional "
            "path_override argument, which can be specified to search outside the standard entity path.")

    print_t("print_partial_path(path):", "tip")
    print_t("Takes a path as input and prints the path as relative to the codemonkeys directory.")
    
    print_t("Example Usage via Monk CLI:", "info")
    print_t("monk -m some_module_name")
    print_t("monk -a some_automation_name")
    print_t("monk -b some_barrel_name")
