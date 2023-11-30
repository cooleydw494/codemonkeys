from codemonkeys.entities.command import Command
from codemonkeys.types import OStr
from codemonkeys.utils.imports.monkey import Monkey
from codemonkeys.utils.monk.theme_functions import verbose_logs_enabled


class PrintMonkey(Command):
    """
    A debugging command for printing the final computed properties of a given Monkey.
    """
    required_arg_keys = ['monkey']
    unnamed_arg_keys = ['monkey']

    monkey: OStr = None

    def run(self) -> None:
        m = Monkey.load(self.monkey)

        # if verbose logs are on this will have logged the monkey info already
        if not verbose_logs_enabled():
            # otherwise print it now
            m.print_monkey_details()
