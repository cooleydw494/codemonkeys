from codemonkeys.base_entities.command_class import Command
from codemonkeys.cmdefs import CM_COMMANDS_PATH
from codemonkeys.defs import COMMANDS_PATH, AUTOMATIONS_PATH, BARRELS_PATH
from codemonkeys.utils.monk.theme_functions import print_tree


class List(Command):
    named_arg_keys = ['all']
    all: bool = False

    def run(self) -> None:

        print_tree(CM_COMMANDS_PATH, exclude_file_starts=['.', '_'],
                   title="📁  Commands - Run CLI commands", incl_prefix=False)
        print_tree(COMMANDS_PATH, exclude_file_starts=['.', '_'], incl_prefix=False)

        if self.all:
            print_tree(AUTOMATIONS_PATH, exclude_file_starts=['.', '_'],
                       title="🤖  Automations - Run automations with monkey configs", incl_prefix=False)
        if self.all:
            print_tree(BARRELS_PATH, exclude_file_starts=['.', '_'],
                       title="🛢️   Barrels - Combine and orchestrate automations", incl_prefix=False)
