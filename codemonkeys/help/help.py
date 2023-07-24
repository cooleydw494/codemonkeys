import argparse

from codemonkeys.utils.monk.theme_functions import print_banner, print_table, print_t, apply_t
from codemonkeys.defs import nl2, nl


def run_default_help(monk_args: argparse.Namespace = None):

    # CodeMonkeys Banner
    print_banner()

    # Overview
    print_t(f"Welcome to CodeMonkeys, an AI-ready automations framework! The Monk CLI includes built-in framework "
            f"Commands and transforms the user Commands directory into readily usable CLI commands. It is also used "
            f"to run Automations and Barrels.{nl}", 'white')

    # Recursive Name-Matching Logic
    print_t("`monk` uses recursive name-matching logic to locate runnable entities. This requires unique filenames "
            "for each runnable entity type (Commands, Automations, Barrels). While limiting, this keeps things simple "
            "and powerful.{nl}", 'important')

    # Handling of Barrels, Automations, and Modules
    print_t("Entity Type flags target Automations and Barrels.", 'info')

    # Action Flags
    print_t(f"Action flags perform alternate operations on targetable entities.{nl2}", 'info')

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
      ],
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
          "monk -e <entity>",
          "Open in vim",
          "--edit"
        ],
        [
          "monk -h <entity>",
          "Help for an entity",
          "--help"
        ],
      ],
    }
    print_table(monk_actions, apply_t("Actions", 'special'), min_col_width=min_col_widths)

    # Wrap up
    print_t("That's it! For more info, run `monk -h <entity>` or view the CodeMonkeys' docs.", 'done')
    exit(0)
