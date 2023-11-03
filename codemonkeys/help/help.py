from codemonkeys.defs import nl2, nl
from codemonkeys.utils.monk.theme_functions import print_banner, print_table, print_t, apply_t


def run_default_help():
    # CodeMonkeys Banner
    print_banner()

    # Overview
    print_t("Welcome to CodeMonkeys, an AI-ready automations framework! The Monk CLI primarily is used to run "
            "Automations, Barrels, and framework Commands. It also makes your own `commands` directory readily usable."
            f"{nl}", 'white')

    # Recursive Name-Matching Logic
    print_t("`monk` uses recursive name-matching logic to locate runnable entities. This requires unique filenames "
            f"for each runnable entity type (Commands, Automations, Barrels).{nl}", 'white')

    # Handling of Barrels, Automations, and Modules
    print_t(f"Entity Type flags target Automations and Barrels.{nl}", 'info')

    # Action Flags
    print_t(f"Action flags perform alternate operations on targetable entities.{nl2}", 'info')

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
            ],
            ['', '', ''],
            ['', '', ''],
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
            ['', '', ''],
            ['', '', ''],
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
        ]
    }
    print_table(monk_general_json, apply_t("Monk CLI", 'special'))

    # Wrap up
    print()
    print()
    print_t("That's it! For more, run `monk -h <entity>` or read the docs.", 'done')
    print()
    print_t("🌐 https://cooleydw494.github.io/codemonkeys", 'cyan')
    print()
    exit(0)
