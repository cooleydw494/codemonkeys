from codemonkeys.cm_paths import VERSION
from codemonkeys.defs import nl2, nl
from codemonkeys.utils.monk.theme_functions import print_table, print_t, apply_t


def run_default_help():

    print_t(f"CodeMonkeys v{VERSION}", 'important')
    print()

    # Overview
    print_t("Welcome to CodeMonkeys! The Monk CLI is used to run Automations, Barrels, and framework"
            f"Commands. It also makes your own `commands` directory readily usable. {nl}", 'white')

    # Handling of Barrels, Automations, and Modules
    print_t(f"Entity Type flags target non-Command entities (Commands are the default entity).{nl}", 'info')

    # Action Flags
    print_t(
        f"Action flags perform alternate operations on targetable entities ('run' is the default action).{nl2}",
        'info'
    )

    monk_general_json = {
        "headers": [
            "Command",
            "Description",
            "Note"
        ],
        "show_headers": True,
        "rows": [
            ['', '', ''],
            [
                "monk help",
                "Run this help script",
                ""
            ],
            [
                "monk list",
                "List existing Commands",
                "--all (list all entities)"
            ],
            [
                "monk version",
                "Print version",
                ""
            ],
            [
                "monk <command>",
                "Run a command",
                "default action/entity"
            ],
            ['', '', ''],
            ['', '', ''],
            [
                "monk -a <automation> --monkey=[name]",
                "Run an automation",
                "--automation"
            ],
            [
                "monk -b <barrel>",
                "Run a barrel",
                "--barrel"
            ],
            ['', '', ''],
            ['', '', ''],
            [
                "monk -e <entity>",
                "Open in vim",
                "--edit"
            ],
            [
                "monk -h <command>",
                "Help for a Command",
                "--help"
            ],
        ]
    }
    print_table(monk_general_json, apply_t("Basic Commands", 'special'))

    # Wrap up
    print()
    print()
    print_t("That's it! For more, run `monk -h <command>` or read the docs.", 'done')
    print()
    print_t("Developer Docs    https://codemonkeys.lol", 'info')
    print_t("Sphinx Docs       https://sphinx.codemonkeys.lol", 'info')
    print_t("GitHub            https://github.com/cooleydw494/codemonkeys", 'info')
    print()
    exit(0)
