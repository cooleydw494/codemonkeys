from pathlib import Path

from art import *
from termcolor import colored


def print_tree(directory, file_callback=None, _prefix=""):
    contents = list(directory.iterdir())
    pointers = [colored("├── ", "cyan")] * (len(contents) - 1) + [colored("└── ", "cyan")]

    for pointer, path in zip(pointers, contents):
        yield _prefix + pointer + colored(path.name, "magenta")
        if path.is_dir():
            extension = colored("    ", "cyan") if pointer == colored("├── ", "cyan") else colored("│   ", "cyan")
            yield from print_tree(path, file_callback, _prefix=_prefix + extension)


def main():
    scripts_dir = Path(__file__).parent.parent

    # Generate ASCII art for "CodeMonkeys"
    art_txt = text2art("CodeMonkeys")
    print(art_txt)

    # Manually create ASCII art representing a "Code Monkey"
    code_monkey_art = """
   🐵    🐵     🐵    🐵    🐵    🐵
   👕 💻 👕     👕 💻 👕    👕 💻 👕
   👖    👖     👖    👖    👖    👖
   """
    print(code_monkey_art)

    print()
    print(colored("At the heart of CodeMonkeys is Monk. It's not just a Python script, it's a streamlined interface "
                  "that mimics sophisticated CLI tools. The goal? Simplify script execution through intuitive matching "
                  "methods and make adding new scripts to the CodeMonkeys boilerplate a breeze. But Monk doesn't stop "
                  "at execution - its flags also support script development, making it an essential tool for both "
                  "routine use and boilerplate customization.", "yellow"))
    print()
    print(colored("🚀 Monk Script Usage:", "blue"))
    print(f"{colored('monk [script-name]', 'green')}         : Run a monk script")
    print(f"{colored('monk kickoff [monkey-name]', 'green')} : Run a Monkey by specifying its name")
    print(f"{colored('monk -e [script-name]', 'green')}      : Open the script in vim                 (--edit)")
    print(f"{colored('monk -p [script-name]', 'green')}      : Print script contents                  (--print)")
    print(f"{colored('monk -cp [script-name]', 'green')}     : Copy script path to clipboard          (--cp-path)")
    print(
        f"{colored('monk -cc [script-name]', 'green')}       : Copy script contents to clipboard      (--cp-contents)")
    print()

    print(colored("📁 Scripts Directory Structure:", "blue"))
    for line in print_tree(scripts_dir):
        print(line)


if __name__ == "__main__":
    main()
