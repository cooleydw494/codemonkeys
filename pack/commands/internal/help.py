import json
import os
from pathlib import Path

from definitions import STORAGE_INTERNAL_PATH
from pack.modules.custom.theme.theme_functions import print_banner, print_table, print_t, apply_theme


def main():
    print_banner()

    # Overview
    print_t("At the heart of CodeMonkeys is the Monk CLI, which transforms scripts in your commands directory into "
            "readily usable CLI commands. It offers simplicity, power, and extensibility. But Monk doesn't stop at "
            "execution - its flags also support script development, making it an essential tool for both routine use "
            "and boilerplate customization.")
    print()

    # Recursive Name-Matching Logic
    print_t("Monk CLI employs recursive name-matching logic to locate your entities. This means every filename within "
            "an entity directory must be unique. While this is certainly a limitation, it encourages thoughtful naming "
            "and ensures a clean, well-organized workspace, making Monk a highly customizable and powerful CLI tool.",
            'important')
    print()

    # Handling of Barrels, Automations, and Modules
    print_t("Entity Type flags allow `monk` to target barrels (-b), automations (-a), and modules (-m).", 'info')
    print()

    # Action Flags
    print_t("Action flags in Monk CLI enable you to edit, print, copy content or path, or seek help using simple "
            "commands. They simplify complex tasks, making your coding experience smooth and enjoyable.", 'info')
    print()

    monk_general_file = os.path.join(STORAGE_INTERNAL_PATH, 'monk', 'monk-commands-general.json')
    monk_general_json = json.loads(Path(monk_general_file).read_text())
    print_table(monk_general_json, apply_theme("Monk CLI", 'special'))

    monk_type_file = os.path.join(STORAGE_INTERNAL_PATH, 'monk', 'monk-commands-type.json')
    monk_type_json = json.loads(Path(monk_type_file).read_text())
    print_table(monk_type_json, apply_theme("Types", 'special'))

    monk_action_file = os.path.join(STORAGE_INTERNAL_PATH, 'monk', 'monk-commands-action.json')
    monk_action_json = json.loads(Path(monk_action_file).read_text())
    print_table(monk_action_json, apply_theme("Actions", 'special'))

    # Wrap up
    print_t("That's it! For more info, use -h on an entity or view CodeMonkeys' docs.",
            'done')


if __name__ == "__main__":
    main()
