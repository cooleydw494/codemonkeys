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

def select_script(prompt: str, script_options: List[tuple[str, int, str]]) -> None:
    script_count = len(script_options)
    print(prompt)
    print("-------------------")
    for i in range(script_count):
        print(f"{i}. {script_options[i][0]}")
    print("-------------------")
    print("Waiting for user input...")
    input_ = input("Enter the number corresponding to the script, or type 'no' to exit: ")
    print("User input received.")

    if input_ == "no":
        print("✋ Exiting.")
        sys.exit(1)
    elif input_ == "tab":
        select_script("📜 All available scripts:", script_options)
    elif input_.isdigit() and 0 <= int(input_) < script_count:
        # Set selected_script to the script at the index of the user's input, choosing the absolute_path value
        selected_script = script_options[int(input_)][2]
        # make sure storage/found-script.txt is empty
        with open(os.path.join(base_dir_abs_path, "storage/found-script.txt"), "w") as f:
            f.write("")
        #write selected_script's value to the file at base path /storage/found-script.txt
        with open(os.path.join(base_dir_abs_path, "storage/found-script.txt"), "w") as f:
            f.write(selected_script)
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
    absolute_matches = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.sh', '.py')):
                filename = os.path.basename(file)
                extension = os.path.splitext(filename)[1]
                name, _ = os.path.splitext(filename)

                if name == script_name:
                    selected_script = os.path.join(root, filename)
                    # make sure storage/found-script.txt is empty
                    with open(os.path.join(base_dir_abs_path, "storage/found-script.txt"), "w") as f:
                        f.write("")
                    #write selected_script's value to the file at base path /storage/found-script.txt
                    with open(os.path.join(base_dir_abs_path, "storage/found-script.txt"), "w") as f:
                        f.write(selected_script)
                    return

                distance = subprocess.check_output(["python3", os.path.join(scripts_root_dir, "internal/levenshtein-distance.py"), script_name, name])
                if int(distance) <= 3:
                    absolute_path = os.path.join(root, file)
                    matches.append((name, int(distance), absolute_path))
    # Sort matches based on distance, keeping the full match object which is a tuple of (name, distance, absolute_path)
    # we need to do this in a way that doesn't convert it to an array of strings, but maintains the tuples
    matches.sort(key=lambda x: x[1])

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
        all_scripts = []
        for root, _, files in os.walk(directory):
            for filename in files:
                if filename.endswith(('.sh', '.py')):
                    name, _ = os.path.splitext(filename)
                    absolute_path = os.path.join(root, filename)
                    all_scripts.append((name, 0, absolute_path))

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