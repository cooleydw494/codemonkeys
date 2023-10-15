from codemonkeys.defs import nl
from codemonkeys.entities.command import Command
from codemonkeys.utils.monk.theme_functions import print_t


class Version(Command):
    def run(self):
        print_t(f"Version Command Help{nl}", "important")

        print_t("The `version` command prints the current version of the CodeMonkeys' framework."
                " Did you really need help with this? :P", 'info')
