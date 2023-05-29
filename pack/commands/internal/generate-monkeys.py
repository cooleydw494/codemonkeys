import os
import shutil
import time

import yaml
from definitions import MONKEYS_PATH


def main():
    # Load the monkey configurations from the YAML file
    monkey_manifest = os.path.join(MONKEYS_PATH, "monkey-manifest.yaml")
    with open(monkey_manifest, "r") as f:
        monkeys = yaml.safe_load(f)

    # Create the directories and configuration files
    for monkey, config in monkeys.items():
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
                continue
            else:
                os.makedirs(os.path.join(monkey_dir, 'history'), exist_ok=True)
                timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
                shutil.move(config_file_path, os.path.join(monkey_dir, 'history', f'{timestamp}.config'))

        # Write the config file
        with open(os.path.join(monkey_dir, 'config'), "w") as f:
            f.write(new_config_content)


if __name__ == "__main__":
    main()
