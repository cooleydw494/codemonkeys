import argparse
from typing import Dict, Any, List, Optional

from codemonkeys.base_entities.cli_runnable_class import CliRunnable
from codemonkeys.utils.monk.find_entity import find_entity
from codemonkeys.utils.monk.run_entities import run_automation
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.utils.monkey_config.load_monkey_config import load_monkey_config

try:
    from config.framework.monkey_config_class import MonkeyConfig
except ImportError:
    print_t('Could not import user MonkeyConfig class from config.framework.monkey_config_class. Using default '
            'MonkeyConfig class. automation_class', 'warning')
    from codemonkeys.config.monkey_config_class import MonkeyConfig


class Barrel(CliRunnable):
    """A Barrel class that initializes and runs multiple automations."""

    monkey_config: Optional[MonkeyConfig] = None

    def __init__(self, monk_args: argparse.Namespace, named_args: Dict[str, Any], unnamed_args: List[str]):
        """
        Initializes the `Barrel` class.

        :param argparse.Namespace monk_args: Monk arguments.
        :param Dict[str, Any] named_args: Named arguments.
        :param List[str] unnamed_args: Unnamed arguments.
        """
        super().__init__(monk_args, named_args, unnamed_args)
        print_t("Barrel initialized.", "start")

    def with_monkey(self, monkey_name: str | None = None) -> 'Barrel':
        """
        Set the MonkeyConfig that will be loaded and used to run Automations. Prompts user if None.

        :param str | None monkey_name: Name of the monkey configuration.
        :return: The current Barrel instance.
        """
        self.monkey_config = load_monkey_config(monkey_name)
        return self

    def run_automation(self, automation_name: str) -> 'Barrel':
        """
        Finds and runs the specified Automation, using the current MonkeyConfig.

        :param str automation_name: Name of the automation to run.
        :return: The current Barrel instance.
        """
        automation_path = find_entity(automation_name, 'automation', exact_match_only=True)
        run_automation(
            automation_path,
            automation_name,
            self.monk_args,
            self.named_args,
            self.unnamed_args,
            self.monkey_config
        )
        return self

    def run(self):
        """
        Defines the abstract method to be implemented in a subclass of Barrel.

        :raises NotImplementedError: The run() method must be implemented in a subclass of Barrel.
        """
        raise NotImplementedError("The run() method must be implemented in a subclass of Barrel.")
