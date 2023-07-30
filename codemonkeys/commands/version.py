from codemonkeys.base_entities.command_class import Command
from codemonkeys.cmdefs import VERSION
from codemonkeys.utils.monk.theme_functions import print_t


class Version(Command):
    """
    Version is a command class that prints out the current version of 
    the CodeMonkeys software.
    """

    def run(self) -> None:
        """
        Prints the version of the CodeMonkeys framework.
        """

        print_t(f"CodeMonkeys v{VERSION}", 'monkey')
