from typing import Dict, Any, List, Optional

from codemonkeys.config.imports.monkey_config import MonkeyConfig
from codemonkeys.entities.cli_runnable import CliRunnable
from codemonkeys.utils.monk.theme_functions import print_t


class Automation(CliRunnable):
    """
    A base class for framework and user-created Automations.
    Automation is a subclass of CLIRunnable and therefor supports named and unnamed args (required or optional).
    It adds the `--monkey` named arg, to specify the MonkeyConfig to use for the Automation.
    When instantiated directly, a MonkeyConfig instance can be passed in the constructor.
    """

    named_arg_keys = ['monkey']
    monkey: str | None = None
    monkey_config: Optional[MonkeyConfig] = None

    def __init__(self, named_args: Dict[str, Any], unnamed_args: List[str], monkey_config: Optional[MonkeyConfig] = None):
        """
        Initializes the `Automation` class.

        :param Dict[str, Any] named_args: Dict of named args and values (e.g. `--key value`)
        :param List[str] unnamed_args: List of unnamed args (e.g. `value`)
        :param MonkeyConfig | None monkey_config: Optional MonkeyConfig for Automation; otherwise, user is prompted.
        """
        super().__init__(named_args, unnamed_args)

        if monkey_config is None:
            self.monkey_config: MonkeyConfig = self.load_config()
        else:
            self.monkey_config = monkey_config

        print_t("Automation initialized.", "start")

    def load_config(self) -> MonkeyConfig:
        """
        Loads the MonkeyConfig instance for the specified monkey (or prompts user if None)

        :return: Instantiated MonkeyConfig.
        """
        return MonkeyConfig.load(self.monkey)

    def run(self):
        """
        The main execution method is implemented in this class and should be overwritten in subclasses.

        :raises NotImplementedError: If not implemented in a subclass.
        """
        raise NotImplementedError("The run() method must be implemented in a subclass of Automation.")
