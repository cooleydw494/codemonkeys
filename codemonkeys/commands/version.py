from codemonkeys.cm_paths import VERSION
from codemonkeys.entities.command import Command
from codemonkeys.utils.monk.theme_functions import print_t


class Version(Command):
    """
    Print the CodeMonkeys framework version.

    The Version command retrieves the current version number of the CodeMonkeys
    software from a constant and displays it prominently in the console,
    highlighting the commitment to keep users informed about the version they're using.
    """

    def run(self) -> None:
        """
        Execute the command to print the framework's version.

        When invoked, this command retrieves the current version number from the
        VERSION constant and prints it out with emphasis, utilizing the theming
        capabilities of the CodeMonkeys framework.
        """

        print_t(f"CodeMonkeys v{VERSION}", 'important')
