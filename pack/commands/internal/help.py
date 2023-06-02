import json
import os
from pathlib import Path

from definitions import STORAGE_INTERNAL_PATH
from pack.modules.custom.theme.theme_functions import print_banner, print_table, print_t, apply_theme


def main():
    print_banner()

    # Overview
    print_t("The Monk CLI transforms scripts in your commands directory into readily usable CLI commands. It offers "
            "simplicity, power, and extensibility. Additionally, its flags support development, making it an "
            "essential tool for both direct use and extension of the framework.")
    print()

    # Recursive Name-Matching Logic
    print_t("`monk` employs recursive name-matching logic to locate existing and custom entities. This requires "
            "unique filenames within each entity directory. While perhaps limiting, it encourages thoughtful naming "
            "and keeps things simple, while enabling an easily customizable and powerful CLI.",
            'important')
    print()

    # Handling of Barrels, Automations, and Modules
    print_t("Entity Type flags allow `monk` to target barrels (-b), automations (-a), and modules (-m).", 'info')
    print()

    # Action Flags
    print_t("Action flags in Monk CLI enable you to edit, print, copy content or path, or seek help using simple "
            "commands.", 'info')
    print()

    min_col_widths = [25, 25, 13]

    monk_general_file = os.path.join(STORAGE_INTERNAL_PATH, 'monk', 'monk-commands-general.json')
    monk_general_json = json.loads(Path(monk_general_file).read_text())
    print_table(monk_general_json, apply_theme("Monk CLI", 'special'), min_col_width=min_col_widths)

    monk_type_file = os.path.join(STORAGE_INTERNAL_PATH, 'monk', 'monk-commands-type.json')
    monk_type_json = json.loads(Path(monk_type_file).read_text())
    print_table(monk_type_json, apply_theme("Entity Types", 'special'), min_col_width=min_col_widths)

    monk_action_file = os.path.join(STORAGE_INTERNAL_PATH, 'monk', 'monk-commands-action.json')
    monk_action_json = json.loads(Path(monk_action_file).read_text())
    print_table(monk_action_json, apply_theme("Actions", 'special'), min_col_width=min_col_widths)

    # Wrap up
    print_t("That's it! For more info, run `monk -h <entity>` or view the CodeMonkeys' docs.",
            'done')


if __name__ == "__main__":
    main()
