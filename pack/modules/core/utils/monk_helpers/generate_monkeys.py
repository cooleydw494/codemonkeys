import os
import os
import shutil
import time

from defs import MONKEYS_PATH, MONKEY_MANIFEST_PATH
from pack.modules.core.config.monkey_config.monkey_config_class import MonkeyConfig
from pack.modules.core.config.yaml_helpers import read_yaml_file, write_yaml_file
from pack.modules.core.theme.theme_functions import print_t


def generate_monkeys():

    try:
        manifest_monkeys = read_yaml_file(MONKEY_MANIFEST_PATH)
    except FileNotFoundError:
        print_t(f"Could not find monkey-manifest.yaml file. File expected to exist at {MONKEY_MANIFEST_PATH}", 'error')
        return

    # Create the directories and config files
    for monkey_name, manifest_config in manifest_monkeys.items():
        merged_config = MonkeyConfig.apply_default_and_validate(manifest_config)

        # Check if new config content is different from the existing one
        generated_config_path = os.path.join(MONKEYS_PATH, f'{monkey_name}.yaml')
        if os.path.exists(generated_config_path):
            existing_config = read_yaml_file(generated_config_path)
            if existing_config == merged_config:
                continue
            else:
                os.makedirs(os.path.join(MONKEYS_PATH, '.history', monkey_name), exist_ok=True)
                timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
                shutil.move(generated_config_path, os.path.join(MONKEYS_PATH, '.history', monkey_name, f'{timestamp}.yaml'))
                # Write to the file
                write_yaml_file(generated_config_path, merged_config, ruamel=True)
