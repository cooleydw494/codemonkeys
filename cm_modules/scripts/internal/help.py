import os
from pathlib import Path

from cm_modules.personality.custom.visuals import print_banner, print_tree, print_table, print_nice
from cm_modules.definitions import ROOT_PATH, SCRIPTS_PATH


def main():
    print_banner()

    print_nice("At the heart of CodeMonkeys is the `monk` command. It's not just a Python script, it's a streamlined "
               "interface that mimics sophisticated CLI tools. The goal? Simplify script execution through intuitive "
               "matching methods and make adding/editing scripts a breeze. But Monk doesn't stop "
               "at execution - its flags also support script development, making it an essential tool for both "
               "routine use and boilerplate customization.", color='important')
    print("\n\n")

    commands_file = os.path.join(ROOT_PATH, 'storage/internal/monk_commands.json')
    commands_json = Path(commands_file).read_text()
    print_table(commands_json, "🚀 Monk Script Usage")

    print_tree(SCRIPTS_PATH, ['internal'], "📁 Scripts")


if __name__ == "__main__":
    main()
