from codemonkeys.cm_paths import CM_COMMANDS_PATH
from codemonkeys.defs import COMMANDS_PATH, AUTOMATIONS_PATH, BARRELS_PATH
from codemonkeys.entities.command import Command
from codemonkeys.utils.monk.theme_functions import print_tree


class List(Command):
    """
    List entities in the command, automations, and barrels directories.

    This command provides a tree view of available entities within the CodeMonkeys project structure.
    Running the list command with the '--all' flag will include both automations and barrels in the output alongside commands.

    :param all: Include automations and barrels in the list if True.
    :type all: bool
    """
    named_arg_keys = ['all']
    all: bool = False

    def run(self) -> None:
        """
        Prints the file paths in a tree structure.

        If the 'all' argument is set to True, it prints additional file paths for automations and barrels.

        :return: None
        :rtype: NoneType
        """
        print_tree(CM_COMMANDS_PATH, exclude_file_starts=['.', '_'],
                   title="📁  Commands - Run CLI commands", incl_prefix=False)
        print_tree(COMMANDS_PATH, exclude_file_starts=['.', '_'], incl_prefix=False)

        if self.all:
            print_tree(AUTOMATIONS_PATH, exclude_file_starts=['.', '_'],
                       title="🤖  Automations - Run automations with Monkey configs", incl_prefix=False)
        if self.all:
            print_tree(BARRELS_PATH, exclude_file_starts=['.', '_'],
                       title="🛢️   Barrels - Combine and orchestrate automations", incl_prefix=False)
