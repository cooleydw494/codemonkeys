import argparse
import os
import shutil
import time

from dotenv import dotenv_values

from definitions import MONKEYS_PATH, ROOT_PATH, MONKEY_MANIFEST_PATH
from pack.modules.core.config.monkey_config.monkey_config_class import MonkeyConfig
from pack.modules.core.config.yaml_helpers import get_monkey_config_defaults, read_yaml_file, write_yaml_file
from pack.modules.core.theme.theme_functions import print_t


def main(monk_args: argparse.Namespace = None):
    print_t("Generating monkey configs...", 'config')

    try:
        manifest_monkeys = read_yaml_file(MONKEY_MANIFEST_PATH)
        print_t("monkey-manifest.yaml located", 'file')
    except FileNotFoundError:
        print_t(f"Could not find monkey-manifest.yaml file. File expected to exist at {MONKEY_MANIFEST_PATH}", 'error')
        return

    # Create the directories and config files
    for monkey_name, manifest_config in manifest_monkeys.items():
        print_t(f"Checking {monkey_name}", 'special')

        merged_config = MonkeyConfig.apply_default_and_validate(manifest_config)

        # Check if new config content is different from the existing one
        generated_config_path = os.path.join(MONKEYS_PATH, f'{monkey_name}.yaml')
        if os.path.exists(generated_config_path):
            existing_config = read_yaml_file(generated_config_path)
            if existing_config == merged_config:
                print_t(f"Skipping {monkey_name} (no changes).", 'quiet')
                continue
            else:
                print_t(f"Changes detected for {monkey_name}. Backing up existing config.", 'info')
                os.makedirs(os.path.join(MONKEYS_PATH, '.history', monkey_name), exist_ok=True)
                timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
                shutil.move(generated_config_path, os.path.join(MONKEYS_PATH, '.history', monkey_name, f'{timestamp}.yaml'))
                # Write to the file
                write_yaml_file(generated_config_path, merged_config, ruamel=True)
                print_t(f"Updated config for {monkey_name}.", 'info')

    print_t("All monkeys processed successfully. Exiting.", 'done')
