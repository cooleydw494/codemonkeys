import os
import subprocess
import sys
from dotenv import load_dotenv
from typing import List

# Load environment variables from .env file
load_dotenv()

# Get the value of BASE_DIR_ABS_PATH from the environment
base_dir_abs_path = os.getenv("BASE_DIR_ABS_PATH")

# Check if the value is present and valid
if not base_dir_abs_path:
    print("⚠️ BASE_DIR_ABS_PATH environment variable is not set. This must be an absolute path.")
    exit(1)

scripts_root_dir = os.path.join(base_dir_abs_path, "scripts")

def select_script(prompt: str, script_options: List[str]) -> None:
    script_count = len(script_options)
    print(prompt)
    print("-------------------")
    for i in range(script_count):
        print(f"{i}. {script_options[i]}")
    print("-------------------")
    input_ = input("Enter the number corresponding to the script, or type 'no' to exit: ")

    if input_ == "no":
        print("✋ Exiting.")
        sys.exit(1)
    elif input_ == "tab":
        select_script("📜 All available scripts:", script_options)
    elif input_.isdigit() and 0 <= int(input_) < script_count:
        selected_script = script_options[int(input_)]
        print(get_script_path(selected_script))
    else:
        print("❌ Invalid input. Please try again.")
        select_script(prompt, script_options)

def get_script_path(script_path: str) -> str:
    extension = os.path.splitext(script_path)[1]

    if extension not in [".sh", ".py"]:
        print(f"⚠️ Unsupported script type: {extension}")
        sys.exit(1)

    return os.path.abspath(script_path)


def find_script(directory: str, script_name: str) -> None:
    matches = []

    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            filename = os.path.basename(file)
            extension = os.path.splitext(filename)[1]
            name, _ = os.path.splitext(filename)

            if name == script_name:
                print(os.path.abspath(os.path.join(directory, file)))
                return

            distance = subprocess.check_output(["python3", os.path.join(scripts_root_dir, "internal/levenshtein-distance.py"), script_name, name])
            if int(distance) <= 3:
                matches.append(name)

    matches.sort()

    if len(matches) > 0:
        prompt = f"⚠️ Script '{script_name}' not found. Did you mean one of these?"
        max_matches = 5
        if len(matches) > max_matches:
            prompt += f" (Showing first {max_matches} matches)"
            select_script(prompt, matches[:max_matches])
        else:
            select_script(prompt, matches)
    else:
        print(f"⚠️ Script '{script_name}' not found.")
        all_scripts = [os.path.splitext(file)[0] for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        if len(all_scripts) > 0:
            select_script("📜 Available scripts:", all_scripts)
        else:
            print("No scripts found.")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Please provide the name of the script as a command-line argument.")
        sys.exit(1)

    command_name = sys.argv[1]
    find_script(scripts_root_dir, command_name)
