from codemonkeys.base_entitiies.command_class import Command
from codemonkeys.utils.monk.theme_functions import print_t
from cmdefs import VERSION


class Version(Command):

    def main(self):
        print_t(f"CodeMonkeys v{VERSION}", 'monkey')
