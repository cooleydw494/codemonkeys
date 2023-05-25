import json
import os
from pathlib import Path

from definitions import STORAGE_INTERNAL_PATH, COMMANDS_PATH, BARRELS_PATH, AUTOMATIONS_PATH, MODULES_PATH
from pack.modules.custom.style.visuals import print_banner, print_table, print_tree, printc, apply_theme


def main():
    print_banner()
    #
    # printc("At the heart of CodeMonkeys is the `monk` command. It's not just a Python script, it's a streamlined "
    #        "interface that mimics sophisticated CLI tools. The goal? Simplify command execution through intuitive "
    #        "matching methods and make adding/editing scripts a breeze. But Monk doesn't stop "
    #        "at execution - its flags also support script development, making it an essential tool for both "
    #        "routine use and boilerplate customization.", 'important')
    # print("\n\n")

    # Overview
    printc("Monk CLI transforms Python scripts in your commands directory into readily usable CLI commands. It offers "
           "simplicity, power, and extensibility to your coding environment.", 'important')
    print()

    # Handling of Barrels, Automations, and Modules
    printc("Monk CLI can also execute barrels and automations with the '-b' and '-a' flags respectively. To target a "
           "module, use the '-m' flag. Monk ensures that all entities are accessible and manageable.", 'important')
    print()

    # Action Flags
    printc("Action flags in Monk CLI enable you to edit, print, copy content or path, or seek help using simple "
           "commands. They simplify complex tasks, making your coding experience smooth and enjoyable.", 'special')
    print()

    commands_file = os.path.join(STORAGE_INTERNAL_PATH, 'monk', 'monk-commands.json')
    commands_json = json.loads(Path(commands_file).read_text())
    print_table(commands_json, apply_theme("Monk CLI Usage", 'monkey'))

    # Recursive Name-Matching Logic
    printc("Monk CLI employs recursive name-matching logic to locate your entities. This means every filename within "
           "an entity directory must be unique. While this is certainly a limitation, it encourages thoughtful naming "
           "and ensures a clean, well-organized workspace, making Monk a highly customizable and powerful CLI tool.",
           'special')
    print()

    # Wrap up
    printc("That's the basic usage of the Monk CLI! For more detailed information on specific commands, please use "
           "the -h action flag (--help). For example: `monk -h generate-monkeys`", 'done')

    # second argument is exclude_dirs (ex: ['internal'])
    print_tree(COMMANDS_PATH, [], False)     # "📁 Commands - core framework CLI commands")
    print_tree(BARRELS_PATH, [], False)      # "🛢️ Barrels - scripts that orchestrate multiple Automations")
    print_tree(AUTOMATIONS_PATH, [], False)  # "🤖 Automations - scripts that run automated tasks using monkey configs")
    print_tree(MODULES_PATH, [], False)      # "📦 Modules - project modules that can be imported")


if __name__ == "__main__":
    main()
