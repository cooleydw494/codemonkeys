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

        When invoked, this command retrieves the current version number from the
        VERSION constant and prints it out with emphasis, utilizing the theming
        capabilities of the CodeMonkeys framework.
        """

        print_t(f"CodeMonkeys v{VERSION}", 'important')
