from cmdefs import CM_COMMANDS_PATH, CM_BARRELS_PATH, CM_AUTOMATIONS_PATH, CM_TASKS_PATH
from codemonkeys.base_entitiies.command_class import Command
from codemonkeys.utils.monk.theme_functions import print_tree


class List(Command):

    named_arg_keys = ['named_arg_one', 'named_arg_two']
    named_arg_one = 'default_named'

    def main(self):

        print(self.monk_args)
        print(self.command_args.get('named_arg_one'))

        print()
        print_tree(CM_COMMANDS_PATH, exclude_file_starts=['.', '_'],
                   title="📁  Commands - Run CLI commands", incl_prefix=False)

        print()
        print_tree(CM_AUTOMATIONS_PATH, exclude_file_starts=['.', '_'],
                   title="🤖  Automations - Run automations with monkey configs", incl_prefix=False)

        print()
        print_tree(CM_BARRELS_PATH, exclude_file_starts=['.', '_'],
                   title="🛢️   Barrels - Combine and orchestrate automations", incl_prefix=False)
