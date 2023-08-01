import os
import sys
from typing import Generator, List, Tuple

from codemonkeys.cmdefs import CM_COMMANDS_PATH, CM_HELP_PATH
from codemonkeys.defs import nl, nl2, COMMANDS_PATH, AUTOMATIONS_PATH, BARRELS_PATH
from codemonkeys.utils.defs_utils import levenshtein_distance
from codemonkeys.utils.monk.theme_functions import print_t, input_t

entity_paths = {
    'command': [COMMANDS_PATH, CM_COMMANDS_PATH],
    'automation': [AUTOMATIONS_PATH],
    'barrel': [BARRELS_PATH],
    'help': [CM_HELP_PATH],
}


def user_select_entity(prompt: str, entity_options: List[Tuple[str, int, int, str, str]]) -> str:
    """
    Process user input for selecting an entity from a list of available options.

    :param str prompt: Text displayed to user before options listing.
    :param list entity_options: A list of tuples each indicating an available entity option.
        Each tuple is of the form (entity name, match level, distance, entity type, entity path)
    :return str: Path of the selected entity.
    """
    print_t(f"{nl}{prompt}{nl2}", 'monkey')
    print('`' * 40)
    for i, (name, _, _, entity_type, _) in enumerate(entity_options):
        print_t(f" ({i + 1}) {name} ({entity_type})", 'option')
    print('.' * 40)

    input_ = input_t("Select an option", "(^C to quit)")
    index = int(input_) - 1

    if input_.isdigit() and 0 <= index < len(entity_options):
        return entity_options[index][4]

    print_t("Invalid input. Please try again.", 'error')
    return user_select_entity(prompt, entity_options)


def find_entity(entity_name: str, entity_type: str, exact_match_only: bool = False) -> str:
    """
    Search for an entity of a certain type.

    :param str entity_name: Name of entity.
    :param str entity_type: Type of entity (command/automation/barrel/help).
    :param bool exact_match_only: Boolean flag to only accept exact matches.
    :return str: The absolute path of the found entity.
    """
    entity_paths_ = entity_paths[entity_type]
    matches = []

    if entity_name is None:
        matches = []
    else:
        for entity_path in entity_paths_:
            matches.extend(
                sorted(_find_entities(entity_path, entity_name, entity_type), key=lambda x: (x[1], len(x[0]))))

    if matches:
        matches_groups = [[m for m in matches if m[1] == i] for i in range(3)]
        for i, group in enumerate(matches_groups):
            if group:
                if i == 0 and len(group) == 1:  # Accept exact match if there is only one
                    return group[0][4]
                if exact_match_only:
                    raise ValueError(f"Exact match not found for '{entity_name}' in {entity_type}s.")
                match_type = ['exact', 'substring', 'close'][i]
                count = 'Multiple' if len(group) > 1 else ''
                prompt = f"{count} {match_type} matches for '{entity_name}' {entity_type} found. Please choose one..."

                return user_select_entity(prompt, group)

    else:
        print_t(f"No matches found for '{entity_name}'.", 'warning')
        all_entities = []
        for entity_path in entity_paths_:
            all_entities.extend(sorted(_find_entities(entity_path, "", entity_type), key=lambda x: (x[1], len(x[0]))))
        if all_entities:
            return user_select_entity(f"All Available {str.capitalize(entity_type)}s:", all_entities)
        print_t("No entities available. You may want to check your setup or use `monk list` command for available "
                "entities.", 'error')
        sys.exit(1)


def _find_entities(entity_directory: str, entity_name: str, entity_type: str) -> Generator[
    Tuple[str, int, int, str, str], None, None]:
    """
    Generate all entities in a certain directory that match a name.

    :param str entity_directory: Directory to search for entities.
    :param str entity_name: Name of the entity to search for.
    :param str entity_type: Type of the entity(command/automation/barrel/help).
    :return Generator: A generator yielding tuples for each entity that matches the search criteria.
        Each tuple is of the form (entity name, match level, distance, entity type, entity path)
    """
    for root, _, files in os.walk(entity_directory):
        for file in files:
            if file.endswith(('.sh', '.py')) and not file.startswith(('.', '_')):
                name, _ = os.path.splitext(os.path.basename(file))
                distance = levenshtein_distance(name, entity_name or "")
                full_path = os.path.join(root, file)
                if name == entity_name:
                    yield name, 0, 0, entity_type, full_path
                elif entity_name in name:
                    yield name, 1, distance, entity_type, full_path
                elif distance <= 3:
                    yield name, 2, distance, entity_type, full_path
