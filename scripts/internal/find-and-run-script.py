import os
import subprocess
import sys
from typing import List

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
        print(f"🏃 Running script: {selected_script}")
        run_script(selected_script)
    else:
        print("❌ Invalid input. Please try again.")
        select_script(prompt, script_options)

def run_script(script_path: str) -> None:
    extension = os.path.splitext(script_path)[1]

    if extension == ".sh":
        subprocess.run(["bash", script_path] + sys.argv[1:], check=True)
    elif extension == ".py":
        subprocess.run(["python3", script_path] + sys.argv[1:], check=True)
    else:
        print(f"⚠️ Unsupported script type: {extension}")
        sys.exit(1)

def find_script(directory: str, script_name: str) -> None:
    matches = []

    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            filename = os.path.basename(file)
            extension = os.path.splitext(filename)[1]
            name, _ = os.path.splitext(filename)

            if name == script_name:
                print(file)
                return

            distance = subprocess.check_output(["python3", os.path.join(directory, "levenshtein_distance.py"), script_name, name])
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
        print(f"⚠️ Script '{script_name}' not found. Showing available scripts:")
        all_scripts = [os.path.splitext(file)[0] for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        if len(all_scripts) > 0:
            select_script("📜 Available scripts:", all_scripts)
        else:
            print("No scripts found.")
            sys.exit(1)

