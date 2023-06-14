import argparse

from core.config_mgmt.environment_checks import automation_env_checks
from core.config_mgmt.monkey_config.load_monkey_config import load_monkey_config
from core.config_mgmt.monkey_config.monkey_config_class import MonkeyConfig
from core.utils.monk.theme.theme_functions import print_t
from modules.abilities.file_list_manager import FileListManager


class Automation:
    required_config_keys = []

    def __init__(self, monk_args: argparse.Namespace):

        automation_env_checks()

        self.monk_args: argparse.Namespace = monk_args

        self.monkey_config: MonkeyConfig = self.load_config()
        self.validate_config()

        self.fpm: FileListManager = FileListManager(self.monkey_config)

        print_t("Automation initialized. Monkey Time!", "start")

    def load_config(self):
        return load_monkey_config(self.monk_args.monkey or None)

    def validate_config(self):
        missing_keys = [key for key in self.required_config_keys if key not in vars(self.monkey_config)]
        if missing_keys:
            raise ValueError(f"Missing required config keys: {', '.join(missing_keys)}")

    def main(self):
        raise NotImplementedError("The main() method must be implemented in a subclass of Automation.")
