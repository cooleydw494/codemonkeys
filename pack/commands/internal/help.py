import json
import os
from pathlib import Path

from definitions import STORAGE_MONK_PATH
from pack.modules.custom.theme.theme_functions import print_banner, print_table, print_t, apply_t


def main():
    print_banner()

    # Overview
    print_t("Welcome to CodeMonkeys, an AI-ready automations framework! The Monk CLI aims to prioritize simplicity, "
            "power, and extensibility. It provides hard-coded framework utility and transforms the commands directory "
            "into readily usable CLI commands. Additionally, its flags make it an essential tool for both direct use "
            "and extension of the framework.", 'white')
    print()

    # Recursive Name-Matching Logic
    print_t("`monk` employs recursive name-matching logic to locate existing/custom entities. This requires unique "
            "filenames within each entity directory. While this is limiting, it also keeps things simple, "
            "customizable, and powerful.",
            'important')
    print()

    # Handling of Barrels, Automations, and Modules
    print_t("Entity Type flags allow `monk` to target barrels (-b), automations (-a), and modules (-m).", 'info')
    print()

    # Action Flags
    print_t("Action flags in Monk CLI enable you to edit, print, copy content or path, or seek help using simple "
            "commands.", 'info')
    print()
    print()

    min_col_widths = [23, 25, 13]

    monk_general_file = os.path.join(STORAGE_MONK_PATH, 'monk-commands-general.json')
    monk_general_json = json.loads(Path(monk_general_file).read_text())
    print_table(monk_general_json, apply_t("Monk CLI", 'special'), min_col_width=min_col_widths)

    monk_type_file = os.path.join(STORAGE_MONK_PATH, 'monk-commands-type.json')
    monk_type_json = json.loads(Path(monk_type_file).read_text())
    print_table(monk_type_json, apply_t("Entity Types", 'special'), min_col_width=min_col_widths)

    monk_action_file = os.path.join(STORAGE_MONK_PATH, 'monk-commands-action.json')
    monk_action_json = json.loads(Path(monk_action_file).read_text())
    print_table(monk_action_json, apply_t("Actions", 'special'), min_col_width=min_col_widths)

    # Wrap up
    print_t("That's it! For more info, run `monk -h <entity>` or view the CodeMonkeys' docs.",
            'done')


if __name__ == "__main__":
    main()
