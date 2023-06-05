import os
import sys
from typing import Generator, List, Tuple

from pack.modules.custom.theme.theme_functions import print_t, input_t
from pack.modules.internal.utils.find_entity_helpers import get_entity_paths, verify_unique_entity_names
from pack.modules.internal.utils.general_helpers import levenshtein_distance


def select_entity(prompt: str, entity_options: List[Tuple[str, int, int, str, str]]) -> str:
    print()
    print_t(prompt, 'monkey')
    print()
    print('````````````````````````````````````````')
    for i, (name, _, _, entity_type, path) in enumerate(entity_options):
        print_t(f" ({i + 1}) {name} ({entity_type})", 'option')
    print('........................................')
    print()

    input_ = input_t("Select an option", "(^C to quit)")

    if input_.isdigit() and 0 <= int(input_) - 1 < len(entity_options):
        partial_path = entity_options[int(input_) - 1][4].split("pack/")[1]
        print_t(f"{partial_path}", 'quiet')
        print()
        return entity_options[int(input_) - 1][4]
    else:
        print_t("Invalid input. Please try again.", 'error')
        return select_entity(prompt, entity_options)


def find_entities(entity_directory: str, entity_name: str, entity_type: str) \
        -> Generator[Tuple[str, int, int, str, str], None, None]:
    for root, _, files in os.walk(entity_directory):
        for file in files:
            # if file isn't hidden and is a script
            if file.endswith(('.sh', '.py')) and not file.startswith(('.', '_')):
                filename = os.path.basename(file)
                name, _ = os.path.splitext(filename)
                distance = levenshtein_distance(name, entity_name or "")
                full_path = os.path.join(root, file)
                if name == entity_name:
                    yield name, 0, 0, entity_type, full_path
                elif entity_name in name:
                    yield name, 1, distance, entity_type, full_path
                elif distance <= 3:
                    yield name, 2, distance, entity_type, full_path


def find_entity(entity_name: str, entity_type: str):
    verify_unique_entity_names()
    entity_path = get_entity_paths()[entity_type]
    matches = sorted(find_entities(entity_path, entity_name, entity_type), key=lambda x: (x[1], len(x[0])))

    if matches:
        # Check for exact and substring matches
        exact_match = next((m for m in matches if m[1] == 0 and m[2] == 0), None)
        substring_match = next((m for m in matches if m[1] == 1 and m[2] < 3), None)

        if exact_match:
            # Return the full path of exact match
            return exact_match[4]
        elif substring_match:
            # Prompt the user to confirm the selection of substring match
            prompt = f"'{entity_name}' {entity_type} not found. Did you mean..."
            return select_entity(prompt, [substring_match])  # Wrap tuple in a list
        else:
            # No exact or substring matches, prompt the user with close matches
            prompt = f"'{entity_name}' {entity_type} not found. Did you mean..."
            return select_entity(prompt, matches[:5])
    else:
        # No matches, show all entities
        print_t(f"No matches found for '{entity_name}'.", 'warning')
        all_entities = sorted(find_entities(entity_path, "", entity_type), key=lambda x: (x[1], len(x[0])))
        if all_entities:
            return select_entity(f"📜 All Available {str.capitalize(entity_type)}s:", all_entities)
        else:
            print_t(
                "No entities available. You may want to check your setup or use `monk list` command for available "
                "entities.",
                'error')
            sys.exit(1)
