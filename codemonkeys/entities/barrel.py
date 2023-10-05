from typing import Dict, Any, List, Optional

from codemonkeys.config.imports.monkey import Monkey
from codemonkeys.entities.cli_runnable import CliRunnable
from codemonkeys.utils.monk.find_entity import find_entity
from codemonkeys.utils.monk.run_entities import run_automation
from codemonkeys.utils.monk.theme_functions import print_t


class Barrel(CliRunnable):
    """A base class that initializes and runs multiple automations."""

    monkey: Optional[Monkey] = None

    def __init__(self, named_args: Dict[str, Any], unnamed_args: List[str]):
        """
        Initializes the `Barrel` class.

        :param Dict[str, Any] named_args: Named arguments.
        :param List[str] unnamed_args: Unnamed arguments.
        """
        super().__init__( named_args, unnamed_args)
        print_t("Barrel initialized.", "start")

    def with_monkey(self, monkey_name: str | None = None) -> 'Barrel':
        """
        Set the Monkey that will be loaded and used to run Automations. Prompts user if None.

        :param str | None monkey_name: Name of the Monkey configuration.
        :return: The current Barrel instance.
        """
        self.monkey = Monkey.load(monkey_name)
        return self

    def run_automation(self, automation_name: str) -> 'Barrel':
        """
        Finds and runs the specified Automation, using the current Monkey.

        :param str automation_name: Name of the automation to run.
        :return: The current Barrel instance.
        """
        automation_path = find_entity(automation_name, 'automation', exact_match_only=True)
        run_automation(
            automation_path,
            automation_name,
            self.named_args,
            self.unnamed_args,
            self.monkey
        )
        return self

    def run(self):
        """
        Defines the abstract method to be implemented in a subclass of Barrel.

        :raises NotImplementedError: The run() method must be implemented in a subclass of Barrel.
        """
        raise NotImplementedError("The run() method must be implemented in a subclass of Barrel.")
