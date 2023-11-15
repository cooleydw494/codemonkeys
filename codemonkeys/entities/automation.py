from typing import Dict, Any, List

from codemonkeys.entities.cli_runnable import CliRunnable
from codemonkeys.types import OStr
from codemonkeys.utils.imports.monkey import Monkey, OMonkey
from codemonkeys.utils.monk.theme_functions import print_t


class Automation(CliRunnable):
    """
    A base class for framework and user-created Automations.

    An Automation is a specific type of CliRunnable that focuses on automating tasks,
    often with the help of Monkeys. It introduces the concept of a Monkey which allows
    for specification of the behavior of the Automation. Subclasses implement specific
    automation logic within the run method.

    Attributes:
        named_arg_keys: A list of named arguments that the CLI command expects.
        monkey: The name of the Monkey to use for the Automation, passed as a CLI argument.
        _monkey: The actual Monkey instance used by the Automation.

    :param named_arg_keys: A list of named arguments that the CLI command expects.
    :type named_arg_keys: list
    :param _monkey: The current Monkey instance used by this Automation.
    :type _monkey: OMonkey
    """

    named_arg_keys: list = ['monkey']
    monkey: OStr = None
    _monkey: OMonkey = None

    def __init__(self, named_args: Dict[str, Any], unnamed_args: List[str], monkey: OMonkey = None):
        """
        Initializes the `Automation` class with potential CLI arguments and an optional Monkey.

        :param named_args: Named arguments passed via the CLI.
        :type named_args: Dict[str, Any]
        :param unnamed_args: Unnamed arguments passed via the CLI.
        :type unnamed_args: List[str]
        :param monkey: An optional Monkey instance to use for this Automation. If None,
                      the Automation will attempt to load a Monkey based on CLI input or default configuration.
        :type monkey: OMonkey
        """
        super().__init__(named_args, unnamed_args)

        if monkey is None:
            self._monkey: Monkey = self.load_monkey()
        else:
            self._monkey = monkey

        print_t(f"Automation initialized: {self.__class__.__name__}", 'start')

    def load_monkey(self) -> Monkey:
        """
        Loads and returns the specified Monkey instance for this Automation.

        If a specific Monkey is not named, the user may be prompted to choose one.

        :return: The Monkey instance.
        :rtype: Monkey
        """
        return Monkey.load(self.monkey)

    def get_monkey(self) -> OMonkey:
        """
        Returns the current Monkey instance used by this Automation.

        :return: The instantiated Monkey, or None if not set.
        :rtype: OMonkey
        """
        return self._monkey

    def trigger(self):
        """
        Triggers the full Automation lifecycle which includes pre-run, main run, and post-run stages.

        It sequentially invokes the before_run method of the Monkey, the run method of the Automation,
        and finally the after_run method of the Monkey.

        :return: None
        """
        self._monkey.before_run()
        self.run()
        self._monkey.after_run()

    def run(self):
        """
        The main execution method for Automations, which must be implemented by subclasses.

        This method should contain the core logic for the automation task and is called during the trigger sequence.

        :raises NotImplementedError: Indicates that a subclass has not implemented this method as required.
        """
        raise NotImplementedError("The run() method must be implemented in a subclass of Automation.")
