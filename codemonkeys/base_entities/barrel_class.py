import argparse
from typing import Dict, Any, List

from codemonkeys.base_entities.utils.cli_runnable_class import CliRunnable
from codemonkeys.utils.monk.find_entity import find_entity
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.utils.monkey_config.load_monkey_config import load_monkey_config

try:
    from config.framework.monkey_config_class import MonkeyConfig
except ImportError:
    print_t('Could not import user MonkeyConfig class from config.framework.monkey_config_class. Using default '
            'MonkeyConfig class. automation_class', 'warning')
    from codemonkeys.config.monkey_config_class import MonkeyConfig


class Barrel(CliRunnable):

    monkey_config: MonkeyConfig | None = None

    def __init__(self, monk_args: argparse.Namespace, named_args: Dict[str, Any], unnamed_args: List[str]):
        super().__init__(monk_args, named_args, unnamed_args)

        print_t("Barrel initialized.", "start")

    def with_monkey(self, monkey_name: str | None = None):
        self.monkey_config = load_monkey_config(monkey_name)

    def run_automation(self, automation_name: str):
        automation = find_entity(automation_name)

    def run(self):
        raise NotImplementedError("The run() method must be implemented in a subclass of Barrel.")
