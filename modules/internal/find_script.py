import os
import sys
from typing import Generator, List, Tuple
from modules.internal.levenshtein_distance import levenshtein_distance
from modules.personality.custom.visuals import printc, inputc
from modules.definitions import SCRIPTS_PATH


def write_to_file(file_path: str, text: str) -> None:
    with open(file_path, "w") as f:
        f.write(text)


def select_script(prompt: str, script_options: List[Tuple[str, int, str]]) -> str:
    printc(prompt, 'monkey')
    printc("-------------------", 'cyan')
    for i, (name, _, _) in enumerate(script_options):
        printc(f"{i}. {name}", 'cyan')
    printc("-------------------", 'cyan')

    input_ = inputc("Enter the number corresponding to the script, or type 'no' to exit: ", 'input')
    printc(f"Running option {input_}: {script_options[int(input_)]}", 'quiet')

    if input_ == "no":
        printc("✋ Exiting.", 'done')
        sys.exit(1)
    elif input_ == "tab":
        return select_script("📜 All available scripts:", script_options)
    elif input_.isdigit() and 0 <= int(input_) < len(script_options):
        return script_options[int(input_)][2]
    else:
        printc("Invalid input. Please try again.", 'error')
        return select_script(prompt, script_options)


def find_scripts(directory: str, script_name: str) -> Generator[Tuple[str, int, str], None, None]:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.sh', '.py')):
                filename = os.path.basename(file)
                name, _ = os.path.splitext(filename)
                if name == script_name:
                    yield name, 0, os.path.join(root, file)
                distance = levenshtein_distance(name, script_name or "")
                if distance <= 3:
                    yield name, distance, os.path.join(root, file)


def find_script(script_name: str):
    matches = sorted(find_scripts(SCRIPTS_PATH, script_name), key=lambda x: x[1])

    if matches:
        # if there is a perfect match, use that
        if matches[0][1] == 0:
            selected_script = matches[0][2]
        else:
            prompt = f"Script '{script_name}' not found. Did you mean one of these?"
            selected_script = select_script(prompt, matches[:5])
    else:
        printc(f"Script '{script_name}' not found.", 'warning')
        all_scripts = sorted(find_scripts(SCRIPTS_PATH, ""), key=lambda x: x[1])
        if all_scripts:
            selected_script = select_script("📜 Available scripts:", all_scripts)
        else:
            selected_script = None

    return selected_script
