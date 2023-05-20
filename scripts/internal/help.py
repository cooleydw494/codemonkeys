import os
from pathlib import Path

from termcolor import colored

from misc import print_banner, print_tree, print_table, print_nice

from dotenv import load_dotenv

load_dotenv()
BASE_PATH = os.getenv("BASE_DIR_ABS_PATH")


def main():
    scripts_dir = Path(__file__).parent.parent

    print_banner()

    print_nice("At the heart of CodeMonkeys is Monk. It's not just a Python script, it's a streamlined interface "
               "that mimics sophisticated CLI tools. The goal? Simplify script execution through intuitive matching "
               "methods and make adding new scripts to the CodeMonkeys boilerplate a breeze. But Monk doesn't stop "
               "at execution - its flags also support script development, making it an essential tool for both "
               "routine use and boilerplate customization.", color='yellow')
    print("\n\n")

    print_table(os.path.join(BASE_PATH, 'storage/internal/monk_commands.json'), "🚀 Monk Script Usage")

    print_tree(scripts_dir, ['internal'], "📁 Scripts")


if __name__ == "__main__":
    main()
