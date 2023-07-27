from codemonkeys.base_entities.command_class import Command
from codemonkeys.cmdefs import VERSION
from codemonkeys.utils.monk.theme_functions import print_t


class Version(Command):

    def run(self) -> None:
        print_t(f"CodeMonkeys v{VERSION}", 'monkey')