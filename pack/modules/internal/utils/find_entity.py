import os
import sys
from typing import Generator, List, Tuple

from pack.modules.custom.theme.theme_functions import print_t, input_t
from pack.modules.internal.utils.find_entity_helpers import get_entity_paths, verify_unique_entity_names
from pack.modules.internal.utils.general_helpers import levenshtein_distance


def select_entity(prompt: str, entity_options: List[Tuple[str, int, int, str, str]]) -> str:
    print_t(prompt, 'monkey')
    print_t("-------------------", 'cyan')
    for i, (name, _, _, entity_type, path) in enumerate(entity_options):
        print_t(f"{i}. {name} ({entity_type})", 'cyan')
    print_t("-------------------", 'cyan')

    input_ = input_t("Enter the number corresponding to the entity", "ctrl+c to exit")
    print_t(f"Selected option {input_}: {entity_options[int(input_)][4]}", 'quiet')

    if input_ == "no":
        print_t("✋ Exiting.", 'done')
        sys.exit(1)
    elif input_ == "tab":
        return select_entity(f"📜 Available Entities:", entity_options)
    elif input_.isdigit() and 0 <= int(input_) < len(entity_options):
        return entity_options[int(input_)][4]
    else:
        print_t("Invalid input. Please try again.", 'error')
        return select_entity(prompt, entity_options)


def find_entities(entity_directory: str, entity_name: str, entity_type: str) \
        -> Generator[Tuple[str, int, int, str, str], None, None]:
    for root, _, files in os.walk(entity_directory):
        for file in files:
            if file.endswith(('.sh', '.py')):
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
            prompt = f"Entity '{entity_name}' is not a complete match. Confirm selection:"
            return select_entity(prompt, [substring_match])  # Wrap tuple in a list
        else:
            # No exact or substring matches, prompt the user with close matches
            prompt = f"Entity '{entity_name}' not found. Did you mean one of these?"
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
