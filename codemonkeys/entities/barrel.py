from typing import Dict, Any, List

from codemonkeys.entities.cli_runnable import CliRunnable
from codemonkeys.types import OStr
from codemonkeys.utils.imports.monkey import Monkey, OMonkey
from codemonkeys.utils.monk.find_entity import find_entity
from codemonkeys.utils.monk.run_entities import run_automation
from codemonkeys.utils.monk.theme_functions import print_t


class Barrel(CliRunnable):
    """A base class for orchestrating multiple automations as a single cli-runnable entity.

    A Barrel allows for sequentially running multiple Automations with specific Monkey configurations,
    encapsulating this logic in a clean and repeatable way. It is utilized when automations need to be
    performed in a specific order or with interdependent settings.

    Attributes:
        monkey (OMonkey): The Monkey instance used to configure automations. Can be set with `with_monkey`.
    """

    monkey: OMonkey = None

    def __init__(self, named_args: Dict[str, Any], unnamed_args: List[str]):
        """
        Initializes the `Barrel` class.

        :param named_args: Named arguments passed via the CLI.
        :type named_args: Dict[str, Any]
        :param unnamed_args: Unnamed arguments passed via the CLI.
        :type unnamed_args: List[str]
        """
        super().__init__(named_args, unnamed_args)
        print_t(f"Barrel initialized: {self.__class__.__name__}", 'start')

    def with_monkey(self, monkey_name: OStr = None) -> 'Barrel':
        """
        Set the Monkey that will be loaded and used to run Automations. Prompts user if None.

        :param monkey_name: Name of the Monkey configuration. If None, the user will be prompted.
        :type monkey_name: OStr, optional
        :return: The current Barrel instance.
        :rtype: Barrel
        """
        self.monkey = Monkey.load(monkey_name)
        return self

    def run_automation(self, name: str) -> 'Barrel':
        """
        Finds and runs the specified Automation, using the current Monkey.

        :param name: Name of the automation to run.
        :type name: str
        :return: The current Barrel instance.
        :rtype: Barrel
        """
        name, abspath = find_entity(name, 'automation', exact_match_only=True)
        run_automation(
            abspath,
            name,
            self.named_args,
            self.unnamed_args,
            self.monkey
        )
        return self

    def run(self):
        """
        Defines the abstract method to be implemented in a subclass of Barrel.

        This method should contain the concrete logic for running multiple automations that are sequenced
        and configured according to the needs of the specific Barrel implementation.

        :raises NotImplementedError: The run() method must be implemented in a subclass of Barrel.
        """
        raise NotImplementedError("The run() method must be implemented in a subclass of Barrel.")
