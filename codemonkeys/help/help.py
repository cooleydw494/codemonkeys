import argparse
import json
import os
from pathlib import Path

from cmdefs import CM_STOR_MONK_PATH
from defs import nl2, nl
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

    monk_general_json = {
      "headers": [
        "Command",
        "Description",
        "Note"
      ],
      "show_headers": False,
      "rows": [
        [
          "monk help",
          "Run this help script",
          ""
        ],
        [
          "monk list",
          "List existing entities",
          "-b/a/m, --all"
        ],
        [
          "monk -v",
          "Print version",
          "--version"
        ],
        [
          "monk <command>",
          "Run a command",
          "default action/entity"
        ]
      ]
    }
    print_table(monk_general_json, apply_t("Monk CLI", 'special'), min_col_width=min_col_widths)

    monk_types = {
      "headers": [
        "Command",
        "Description",
        "Note"
      ],
      "show_headers": False,
      "rows": [
        [
          "monk -a <automation>",
          "Run an automation",
          "--automation"
        ],
        [
          "monk -b <barrel>",
          "Run a barrel",
          "--barrel"
        ],
        [
          "monk -m <module>",
          "Edit a module",
          "--module"
        ]
      ]
    }
    print_table(monk_types, apply_t("Entity Types", 'special'), min_col_width=min_col_widths)

    monk_actions = {
      "headers": [
        "Command",
        "Description",
        "Note"
      ],
      "show_headers": False,
      "rows": [
        [
          "monk -r <entity>",
          "Run an entity",
          "--run"
        ],
        [
          "monk -e <entity>",
          "Open in vim",
          "--edit"
        ],
        [
          "monk -p <entity>",
          "Print file contents",
          "--print"
        ],
        [
          "monk -cp <entity>",
          "Copy file abspath",
          "--copy-path"
        ],
        [
          "monk -cc <entity>",
          "Copy file contents",
          "--copy-contents"
        ],
        [
          "monk -h <entity>",
          "Help for an entity",
          "--help"
        ]
      ]
    }
    print_table(monk_actions, apply_t("Actions", 'special'), min_col_width=min_col_widths)

    # Wrap up
    print_t("That's it! For more info, run `monk -h <entity>` or view the CodeMonkeys' docs.", 'done')
