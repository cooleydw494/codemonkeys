import os
import sys
from typing import Generator, List, Tuple
from pack.modules.internal.utils.levenshtein_distance import levenshtein_distance
from pack.modules.custom.theme.theme_functions import print_t, input_t


def write_to_file(file_path: str, text: str) -> None:
    with open(file_path, "w") as f:
        f.write(text)


def select_entity(prompt: str, entity_options: List[Tuple[str, int, str]]) -> str:
    print_t(prompt, 'monkey')
    print_t("-------------------", 'cyan')
    for i, (name, _, _) in enumerate(entity_options):
        print_t(f"{i}. {name}", 'cyan')
    print_t("-------------------", 'cyan')

    input_ = input_t("Enter the number corresponding to the entity, or type 'no' to sys.exit: ", 'input')
    print_t(f"Running option {input_}: {entity_options[int(input_)]}", 'quiet')

    if input_ == "no":
        print_t("✋ Exiting.", 'done')
        sys.exit(1)
    elif input_ == "tab":
        return select_entity("📜 All Available Commands:", entity_options)
    elif input_.isdigit() and 0 <= int(input_) < len(entity_options):
        return entity_options[int(input_)][2]
    else:
        print_t("Invalid input. Please try again.", 'error')
        return select_entity(prompt, entity_options)


def find_entities(directory: str, entity_name: str) -> Generator[Tuple[str, int, str], None, None]:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.sh', '.py')):
                filename = os.path.basename(file)
                name, _ = os.path.splitext(filename)
                if name == entity_name:
                    yield name, 0, os.path.join(root, file)
                distance = levenshtein_distance(name, entity_name or "")
                if distance <= 3:
                    yield name, distance, os.path.join(root, file)


def find_entity(entity_name: str, entity_path: str):
    matches = sorted(find_entities(entity_path, entity_name), key=lambda x: x[1])

    if matches:
        # if there is a perfect match, use that
        if matches[0][1] == 0:
            selected_entity = matches[0][2]
        else:
            prompt = f"Entity '{entity_name}' not found. Did you mean one of these?"
            selected_entity = select_entity(prompt, matches[:5])
    else:
        print_t(f"Entity '{entity_name}' not found.", 'warning')
        all_entities = sorted(find_entities(entity_path, ""), key=lambda x: x[1])
        if all_entities:
            selected_entity = select_entity("📜 Available Commands:", all_entities)
        else:
            selected_entity = None

    return selected_entity
