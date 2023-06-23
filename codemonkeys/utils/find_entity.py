import os
import sys
from typing import Generator, List, Tuple

from defs import nl, CM_COMMANDS_PATH, CM_AUTOMATIONS_PATH, CM_BARRELS_PATH, CM_TASKS_PATH, nl2
from codemonkeys.utils.framework_utils import levenshtein_distance
from codemonkeys.utils.monk.theme_functions import print_t, input_t

entity_paths = {
    'command': CM_COMMANDS_PATH,
    'automation': CM_AUTOMATIONS_PATH,
    'barrel': CM_BARRELS_PATH,
    'module': CM_TASKS_PATH,
}


def user_select_entity(prompt: str, entity_options: List[Tuple[str, int, int, str, str]]) -> str:
    print_t(f"{nl}{prompt}{nl2}", 'monkey')
    print('`' * 40)
    for i, (name, _, _, entity_type, _) in enumerate(entity_options):
        print_t(f" ({i + 1}) {name} ({entity_type})", 'option')
    print('.' * 40)

    input_ = input_t("Select an option", "(^C to quit)")
    index = int(input_) - 1

    if input_.isdigit() and 0 <= index < len(entity_options):
        print_partial_path(entity_options[index][4])
        return entity_options[index][4]

    print_t("Invalid input. Please try again.", 'error')
    return user_select_entity(prompt, entity_options)


def find_entities(entity_directory: str, entity_name: str, entity_type: str) -> Generator[
    Tuple[str, int, int, str, str], None, None]:
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


def find_entity(entity_name: str, entity_type: str, path_override: str = None) -> str:
    entity_path = path_override or entity_paths[entity_type]
    matches = sorted(find_entities(entity_path, entity_name, entity_type), key=lambda x: (x[1], len(x[0])))

    if matches:
        matches_groups = [[m for m in matches if m[1] == i] for i in range(3)]

        for i, group in enumerate(matches_groups):
            if group:
                if i == 0 and len(group) == 1:  # Accept exact match if there is only one
                    return group[0][4]
                match_type = ['exact', 'substring', 'close'][i]
                count = 'Multiple' if len(group) > 1 else ''
                prompt = f"{count} {match_type} matches for '{entity_name}' {entity_type} found. Please choose one..."

                return user_select_entity(prompt, group)

    else:
        # If entity_type is 'module' and no matches found, search in 'codemonkeys' path
        if entity_type == 'module':
            print_t(f"No module matches found for '{entity_name}'. Searching in codemonkeys files...", 'warning')
            return find_entity(entity_name, 'codemonkeys')

        print_t(f"No matches found for '{entity_name}'.", 'warning')
        all_entities = sorted(find_entities(entity_path, "", entity_type), key=lambda x: (x[1], len(x[0])))
        if all_entities:
            return user_select_entity(f"All Available {str.capitalize(entity_type)}s:", all_entities)
        print_t("No entities available. You may want to check your setup or use `monk list` command for available "
                "entities.", 'error')
        sys.exit(1)


def print_partial_path(path: str):
    print_t(f"{path.split('codemonkeys/')[1] if 'codemonkeys/' in path else path}{nl}", 'quiet')
