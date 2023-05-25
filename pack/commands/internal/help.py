import json
import os
from pathlib import Path

from ...definitions import STORAGE_INTERNAL_PATH, COMMANDS_PATH
from pack.modules.custom.style.visuals import print_banner, printc, print_table, print_tree


def main():
    print_banner()

    printc("At the heart of CodeMonkeys is the `monk` command. It's not just a Python script, it's a streamlined "
           "interface that mimics sophisticated CLI tools. The goal? Simplify command execution through intuitive "
           "matching methods and make adding/editing scripts a breeze. But Monk doesn't stop "
           "at execution - its flags also support script development, making it an essential tool for both "
           "routine use and boilerplate customization.", 'important')
    print("\n\n")

    commands_file = os.path.join(STORAGE_INTERNAL_PATH, 'monk', 'monk-commands.json')
    commands_json = json.loads(Path(commands_file).read_text())
    print_table(commands_json, "🚀 Monk Command Usage")

    print_tree(COMMANDS_PATH, [], "📁 Commands")  # second argument is exclude_dirs (ex: ['internal'])


if __name__ == "__main__":
    main()
