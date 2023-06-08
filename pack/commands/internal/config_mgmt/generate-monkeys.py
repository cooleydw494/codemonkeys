import argparse
import os
import shutil
import time

from dotenv import dotenv_values

from definitions import MONKEYS_PATH, ROOT_PATH
from pack.modules.internal.config_mgmt.yaml_helpers import get_monkey_config_defaults, read_yaml_file, write_yaml_file
from pack.modules.internal.theme.theme_functions import print_t


def main(monk_args: argparse.Namespace = None):
    print_t("Generating monkey configs...", 'config')
    monkey_manifest = os.path.join(ROOT_PATH, "monkey-manifest.yaml")

    try:
        monkeys = read_yaml_file(monkey_manifest)
        print_t("monkey-manifest.yaml located", 'file')
    except FileNotFoundError:
        print_t(f"Could not find monkey-manifest.yaml file. File expected to exist at {monkey_manifest}", 'error')
        return

    default_config = get_monkey_config_defaults()

    # Load .env values
    env_config = dotenv_values(".env")
    # Filter only those keys present in default_config
    env_config = {k: env_config[k] for k in env_config if k in default_config}

    # Create the directories and config files
    for monkey_name, config in monkeys.items():
        print_t(f"Checking {monkey_name}", 'special')

        # Merge the default config with the monkey's own config
        merged_config = default_config.copy()  # Start with the defaults
        merged_config.update(env_config)  # Overwrite with the .env's specific config
        merged_config.update(config)  # Overwrite with the monkey's specific config

        config_file_path = os.path.join(MONKEYS_PATH, f'{monkey_name}.yaml')
        # Check if new config content is different from the existing one
        if os.path.exists(config_file_path):
            existing_config = read_yaml_file(config_file_path)
            if existing_config == merged_config:
                print_t(f"Skipping {monkey_name} (no changes).", 'quiet')
                continue
            else:
                print_t(f"Changes detected for {monkey_name}. Backing up existing config.", 'info')
                os.makedirs(os.path.join(MONKEYS_PATH, '.history', monkey_name), exist_ok=True)
                timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
                shutil.move(config_file_path, os.path.join(MONKEYS_PATH, '.history', monkey_name, f'{timestamp}.yaml'))

        # Write the config file
        write_yaml_file(config_file_path, merged_config, ruamel=True)
        print_t(f"Updated config for {monkey_name}.", 'info')

    print_t("All monkeys processed successfully. Exiting.", 'done')