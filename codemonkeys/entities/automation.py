from typing import Dict, Any, List, Optional

from codemonkeys.config.imports.monkey import Monkey
from codemonkeys.entities.cli_runnable import CliRunnable
from codemonkeys.utils.monk.theme_functions import print_t


class Automation(CliRunnable):
    """
    A base class for framework and user-created Automations.
    Automation is a subclass of CLIRunnable and therefor supports named and unnamed args (required or optional).
    It adds the `--monkey` named arg, to specify the Monkey to use for the Automation.
    When instantiated directly, a Monkey instance can be passed in the constructor.
    """

    named_arg_keys = ['monkey']
    monkey: str | None = None
    _monkey: Optional[Monkey] = None

    def __init__(self, named_args: Dict[str, Any], unnamed_args: List[str], monkey: Optional[Monkey] = None):
        """
        Initializes the `Automation` class.

        :param Dict[str, Any] named_args: Dict of named args and values (e.g. `--key value`)
        :param List[str] unnamed_args: List of unnamed args (e.g. `value`)
        :param Monkey | None monkey: Optional Monkey for Automation; otherwise, user is prompted.
        """
        super().__init__(named_args, unnamed_args)

        if monkey is None:
            self._monkey: Monkey = self.load_monkey()
        else:
            self._monkey = monkey

        print_t("Automation initialized.", "start")

    def load_monkey(self) -> Monkey:
        """
        Loads the Monkey instance for the specified Monkey (or prompts user if None)

        :return: Instantiated Monkey.
        """
        return Monkey.load(self.monkey)

    def get_monkey(self) -> Optional[Monkey]:
        """
        Returns the Monkey instance for the specified Monkey (or None)

        :return: Instantiated Monkey.
        """
        return self._monkey

    def run(self):
        """
        The main execution method is implemented in this class and should be overwritten in subclasses.

        :raises NotImplementedError: If not implemented in a subclass.
        """
        raise NotImplementedError("The run() method must be implemented in a subclass of Automation.")
