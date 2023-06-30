from cmdefs import CM_COMMANDS_PATH, CM_BARRELS_PATH, CM_AUTOMATIONS_PATH
from codemonkeys.base_entitiies.command_class import Command
from codemonkeys.utils.monk.theme_functions import print_tree
from defs import COMMANDS_PATH, AUTOMATIONS_PATH, BARRELS_PATH


class List(Command):
    named_arg_keys = ['all']
    all: bool = False

    def main(self):

        print_tree(CM_COMMANDS_PATH, exclude_file_starts=['.', '_'],
                   title="📁  Commands - Run CLI commands", incl_prefix=False)
        print_tree(COMMANDS_PATH, exclude_file_starts=['.', '_'], incl_prefix=False)

        if self.all:
            print_tree(CM_AUTOMATIONS_PATH, exclude_file_starts=['.', '_'],
                       title="🤖  Automations - Run automations with monkey configs", incl_prefix=False)
            print_tree(AUTOMATIONS_PATH, exclude_file_starts=['.', '_'], incl_prefix=False)

        if self.all:
            print_tree(CM_BARRELS_PATH, exclude_file_starts=['.', '_'],
                       title="🛢️   Barrels - Combine and orchestrate automations", incl_prefix=False)
            print_tree(BARRELS_PATH, exclude_file_starts=['.', '_'], incl_prefix=False)

