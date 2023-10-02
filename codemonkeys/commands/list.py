from codemonkeys.cm_paths import CM_COMMANDS_PATH
from codemonkeys.defs import COMMANDS_PATH, AUTOMATIONS_PATH, BARRELS_PATH
from codemonkeys.entities.command import Command
from codemonkeys.utils.monk.theme_functions import print_tree


class List(Command):
    """
    This is a subclass of Command class which lists certain file paths,
    and has an optional 'all' argument to list additional file paths.
    The 'all' argument is False by default.

    :param bool all: An optional argument to list additional file paths. Default is False.
    """
    named_arg_keys = ['all']
    all: bool = False

    def run(self) -> None:
        """
        Prints the file paths in a tree structure.

        If the 'all' argument is set to True, it prints additional file paths.

        :return: None
        """
        print_tree(CM_COMMANDS_PATH, exclude_file_starts=['.', '_'],
                   title="📁  Commands - Run CLI commands", incl_prefix=False)
        print_tree(COMMANDS_PATH, exclude_file_starts=['.', '_'], incl_prefix=False)

        if self.all:
            print_tree(AUTOMATIONS_PATH, exclude_file_starts=['.', '_'],
                       title="🤖  Automations - Run automations with monkey configs", incl_prefix=False)
        if self.all:
            print_tree(BARRELS_PATH, exclude_file_starts=['.', '_'],
                       title="🛢️   Barrels - Combine and orchestrate automations", incl_prefix=False)
