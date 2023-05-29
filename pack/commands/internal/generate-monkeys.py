import os
import shutil
import time

import yaml
from definitions import MONKEYS_PATH
from pack.modules.custom.theme.theme_functions import print_t


def main():
    print_t("Generating monkey configs...", 'start')
    monkey_manifest = os.path.join(MONKEYS_PATH, "monkey-manifest.yaml")
    try:
        with open(monkey_manifest, "r") as f:
            monkeys = yaml.safe_load(f)
        print_t("monkey-manifest.yaml located", 'info')
    except FileNotFoundError:
        print_t(f"Could not find monkey-manifest.yaml file. File expected to exist at {monkey_manifest}", 'error')
        return

    # Create the directories and configuration files
    for monkey, config in monkeys.items():
        print_t(f"Checking {monkey}", 'special')
        # Create the directory for the monkey if it doesn't exist
        monkey_dir = os.path.join(MONKEYS_PATH, monkey)
        os.makedirs(monkey_dir, exist_ok=True)

        # Generate new config content
        new_config_content = "\n".join(f"{key}='{value}'" for key, value in config.items()) + '\n'

        config_file_path = os.path.join(monkey_dir, 'config')
        # Check if new config content is different from the existing one
        if os.path.exists(config_file_path):
            with open(config_file_path, "r") as f:
                existing_config_content = f.read()
            if existing_config_content == new_config_content:
                print_t(f"Skipping {monkey} (no changes).", 'quiet')
                continue
            else:
                print_t(f"Changes detected for {monkey}. Backing up existing config.", 'info')
                os.makedirs(os.path.join(monkey_dir, 'history'), exist_ok=True)
                timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
                shutil.move(config_file_path, os.path.join(monkey_dir, 'history', f'{timestamp}.config'))

        # Write the config file
        with open(os.path.join(monkey_dir, 'config'), "w") as f:
            f.write(new_config_content)
        print_t(f"Updated config for {monkey}.", 'info')

    print_t("All monkeys processed successfully. Exiting.", 'done')


if __name__ == "__main__":
    main()
