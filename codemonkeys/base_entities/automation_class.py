import argparse
from typing import Dict, Any, List

from codemonkeys.base_entities.utils.cli_runnable_class import CliRunnable
from codemonkeys.utils.env.environment_checks import automation_env_checks
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.utils.monkey_config.load_monkey_config import load_monkey_config

try:
    from config.framework.monkey_config_class import MonkeyConfig
except ImportError:
    print_t('Could not import user MonkeyConfig class from config.framework.monkey_config_class. Using default '
            'MonkeyConfig class. automation_class', 'warning')
    from codemonkeys.config.monkey_config_class import MonkeyConfig


class Automation(CliRunnable):
    named_arg_keys = ['monkey']
    monkey: str = None
    monkey_config: MonkeyConfig | None = None

    required_config_keys = []

    def __init__(self, monk_args: argparse.Namespace, named_args: Dict[str, Any], unnamed_args: List[str], monkey_config: MonkeyConfig | None = None):

        super().__init__(monk_args, named_args, unnamed_args)

        automation_env_checks()

        if monkey_config is None:
            self.monkey_config: MonkeyConfig = self.load_config()
        else:
            self.monkey_config = monkey_config

        self._check_required_config_keys()

        print_t("Automation initialized.", "start")

    def load_config(self) -> MonkeyConfig:
        return load_monkey_config(self.monkey)

    def _check_required_config_keys(self):
        missing_keys = [key for key in self.required_config_keys if key not in vars(self.monkey_config)]
        if missing_keys:
            raise ValueError(f"Missing required config keys: {', '.join(missing_keys)}")

    def run(self):
        raise NotImplementedError("The run() method must be implemented in a subclass of Automation.")
