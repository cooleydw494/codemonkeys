import os
import sys
from typing import List, Tuple

import Levenshtein

from codemonkeys.cm_paths import CM_COMMANDS_PATH, CM_HELP_PATH
from codemonkeys.defs import nl2, COMMANDS_PATH, AUTOMATIONS_PATH, BARRELS_PATH, MONKEYS_PATH
from codemonkeys.utils.monk.theme_functions import print_t, input_t

entity_paths = {
    'command': [COMMANDS_PATH, CM_COMMANDS_PATH],
    'automation': [AUTOMATIONS_PATH],
    'barrel': [BARRELS_PATH],
    'monkey': [MONKEYS_PATH],
    'help': [CM_HELP_PATH],
}


def user_select_entity(prompt: str, entity_options: List[Tuple[str, str, str]]) -> tuple[str, str]:
    """
    Process user input for selecting an entity from a list of available options.

    :param str prompt: Text displayed to user before options listing.
    :param list entity_options: A list of tuples each indicating an available entity option.
        Each tuple is of the form (entity name, entity type, entity full path)
    :return str: Full path of the selected entity.
    """
    print_t(f"{prompt}{nl2}", 'important')
    print('`' * 40)
    for i, (name, entity_type, _) in enumerate(entity_options):
        print_t(f" ({i + 1}) {name} ({entity_type})")
    print('.' * 40)

    index = int(input_t("Select an option", "(^C to quit)")) - 1
    if 0 <= index < len(entity_options):
        name = entity_options[index][0]
        abspath = entity_options[index][2]
        return name, abspath
    print_t("Invalid input. Please try again.", 'error')
    return user_select_entity(prompt, entity_options)


def find_entity(entity_name: str, entity_type: str, exact_match_only: bool = False) -> tuple[str, str]:
    """
    Search for an entity of a certain type.

    :param str entity_name: Name of entity.
    :param str entity_type: Type of entity (command/automation/barrel/help).
    :param bool exact_match_only: Boolean flag to only accept exact matches.
    :return str: The full path of the found entity.
    """
    matches = [
        (name, entity_type, full_path)
        for path in entity_paths[entity_type]
        for name, full_path in _find_entities(path, entity_name)
    ]

    if not matches:
        print_t(f"No matches found for '{entity_name}'.", 'error')
        sys.exit(1)

    exact_matches = [m for m in matches if m[0] == entity_name]
    if len(exact_matches) == 1:
        name = exact_matches[0][0]
        abspath = exact_matches[0][2]
        return name, abspath

    if exact_match_only:
        raise ValueError(f"Exact match not found for '{entity_name}' in {entity_type}s.")

    prompt = f"Matches for '{entity_name}' {entity_type} found. Please choose one..."
    return user_select_entity(prompt, matches)


def _find_entities(entity_directory: str, entity_name: str) -> List[Tuple[str, str]]:
    """
    Find all entities in a certain directory that match a name.

    :param str entity_directory: Directory to search for entities.
    :param str entity_name: Name of the entity to search for.
    :return List[Tuple[str, str]]: A list of tuples for each entity that matches the search criteria.
        Each tuple is of the form (entity name, entity full path)
    """
    matches = []
    for root, _, files in os.walk(entity_directory):
        for file in files:
            if file.endswith(('.sh', '.py')) and not file.startswith(('.', '_')):
                name, _ = os.path.splitext(file)
                full_path = os.path.join(root, file)
                if name == entity_name or entity_name in name or Levenshtein.distance(name, entity_name) <= 3:
                    matches.append((name, full_path))
    return matches
