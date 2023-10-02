from codemonkeys.cm_paths import VERSION
from codemonkeys.entities.command import Command
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
