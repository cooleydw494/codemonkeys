import argparse
from typing import Dict, Any, List

from codemonkeys.base_entitiies.utils.cli_runnable_class import CliRunnable
from codemonkeys.utils.env.environment_checks import automation_env_checks
from codemonkeys.utils.monkey_config.load_monkey_config import load_monkey_config
from defs import import_monkey_config_class
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.abilities.file_list_manager import FileListManager

MonkeyConfig = import_monkey_config_class()


class Automation(CliRunnable):
    named_arg_keys = ['monkey']
    monkey: str = None

    required_config_keys = []

    def __init__(self, monk_args: argparse.Namespace, named_args: Dict[str, Any], unnamed_args: List[str]):

        super().__init__(monk_args, named_args, unnamed_args)

        automation_env_checks()

        self.monkey_config: MonkeyConfig = self.load_config()
        self.validate_config()

        self.flm: FileListManager = FileListManager(self.monkey_config)

        print_t("Automation initialized. Monkey Time!", "start")

    def load_config(self):
        return load_monkey_config(self.monkey)

    def validate_config(self):
        missing_keys = [key for key in self.required_config_keys if key not in vars(self.monkey_config)]
        if missing_keys:
            raise ValueError(f"Missing required config keys: {', '.join(missing_keys)}")

    def run(self):
        raise NotImplementedError("The main() method must be implemented in a subclass of Automation.")
