import os
from typing import Generator, List, Tuple
from dotenv import load_dotenv

from scripts.internal.levenshtein_distance import levenshtein_distance

load_dotenv()
base_dir_abs_path = os.getenv("BASE_DIR_ABS_PATH")
scripts_root_dir = os.path.join(base_dir_abs_path, "scripts")


def write_to_file(file_path: str, text: str) -> None:
    with open(file_path, "w") as f:
        f.write(text)


def select_script(prompt: str, script_options: List[Tuple[str, int, str]]) -> str:
    print(prompt)
    print("-------------------")
    for i, (name, _, _) in enumerate(script_options):
        print(f"{i}. {name}")
    print("-------------------")

    input_ = input("Enter the number corresponding to the script, or type 'no' to exit: ")
    print("User input received.")

    if input_ == "no":
        print("✋ Exiting.")
        sys.exit(1)
    elif input_ == "tab":
        return select_script("📜 All available scripts:", script_options)
    elif input_.isdigit() and 0 <= int(input_) < len(script_options):
        return script_options[int(input_)][2]
    else:
        print("❌ Invalid input. Please try again.")
        return select_script(prompt, script_options)


def find_scripts(directory: str, script_name: str) -> Generator[Tuple[str, int, str], None, None]:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.sh', '.py')):
                filename = os.path.basename(file)
                name, _ = os.path.splitext(filename)
                if name == script_name:
                    yield name, 0, os.path.join(root, file)
                    return
                distance = levenshtein_distance(name, script_name)
                if distance <= 3:
                    yield name, distance, os.path.join(root, file)


def find_script(script_name: str) -> None:
    matches = sorted(find_scripts(scripts_root_dir, script_name), key=lambda x: x[1])
    selected_script = ""

    if matches:
        prompt = f"⚠️ Script '{script_name}' not found. Did you mean one of these?"
        selected_script = select_script(prompt, matches[:5])
    else:
        print(f"⚠️ Script '{script_name}' not found.")
        all_scripts = sorted(find_scripts(scripts_root_dir, ""), key=lambda x: x[1])
        if all_scripts:
            selected_script = select_script("📜 Available scripts:", all_scripts)
        else:
            print("No scripts found.")
            sys.exit(1)

    write_to_file(os.path.join(base_dir_abs_path, "storage/found-script.txt"), selected_script)
