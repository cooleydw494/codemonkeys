import argparse
import json
import os
from pathlib import Path

from defs import CM_STOR_MONK_PATH, nl2, nl
from codemonkeys.utils.monk.theme_functions import print_banner, print_table, print_t, apply_t


def run_default_help(monk_args: argparse.Namespace = None):

    # CodeMonkeys Banner
    print_banner()

    # Overview
    print_t("Welcome to CodeMonkeys, an AI-ready automations codemonkeys! The Monk CLI aims to prioritize simplicity, "
            "power, and extensibility. It provides hard-coded codemonkeys utility and transforms the commands directory "
            "into readily usable CLI commands. Additionally, its flags make it an essential tool for both direct use "
            f"and extension of the codemonkeys-codemonkeys.{nl}", 'white')

    # Recursive Name-Matching Logic
    print_t("`monk` employs recursive name-matching logic to locate codemonkeys/usr entities. This requires unique "
            "filenames within each entity directory. While this is limiting, it also keeps things simple, "
            f"customizable, and powerful.{nl}", 'important')

    # Handling of Barrels, Automations, and Modules
    print_t("Entity Type flags allow you to target barrels (-b), automations (-a), and modules (-m).", 'info')

    # Action Flags
    print_t(f"Action flags allow you to perform a variety of operations on any targetable entity.{nl2}", 'info')

    min_col_widths = [23, 25, 13]

    monk_general_file = os.path.join(CM_STOR_MONK_PATH, 'monk-commands-general.json')
    monk_general_json = json.loads(Path(monk_general_file).read_text())
    print_table(monk_general_json, apply_t("Monk CLI", 'special'), min_col_width=min_col_widths)

    monk_type_file = os.path.join(CM_STOR_MONK_PATH, 'monk-commands-type.json')
    monk_type_json = json.loads(Path(monk_type_file).read_text())
    print_table(monk_type_json, apply_t("Entity Types", 'special'), min_col_width=min_col_widths)

    monk_action_file = os.path.join(CM_STOR_MONK_PATH, 'monk-commands-action.json')
    monk_action_json = json.loads(Path(monk_action_file).read_text())
    print_table(monk_action_json, apply_t("Actions", 'special'), min_col_width=min_col_widths)

    # Wrap up
    print_t("That's it! For more info, run `monk -h <entity>` or view the CodeMonkeys' docs.", 'done')
