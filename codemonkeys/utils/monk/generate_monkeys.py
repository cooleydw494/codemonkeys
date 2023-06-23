import os
import shutil
import time

from defs import import_monkey_config_class
from defs import MONKEYS_PATH, MONKEY_MANIFEST_PATH
from codemonkeys.config.yaml_helpers import read_yaml_file, write_yaml_file
from codemonkeys.utils.monk.theme_functions import print_t

MonkeyConfig = import_monkey_config_class()


def generate_monkeys():

    os.makedirs(os.path.join(MONKEYS_PATH), exist_ok=True)

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
        else:
            write_yaml_file(generated_config_path, merged_config, ruamel=True)

    # Remove any monkeys that are no longer in the manifest
    for monkey_name in os.listdir(MONKEYS_PATH):
        if monkey_name.endswith('.yaml'):
            monkey_name = monkey_name[:-5]
            if monkey_name not in manifest_monkeys:
                os.makedirs(os.path.join(MONKEYS_PATH, '.history', monkey_name), exist_ok=True)
                timestamp = time.strftime("%Y-%m-%d_%H:%M:%S")
                removed_monkey_path = os.path.join(MONKEYS_PATH, f'{monkey_name}.yaml')
                shutil.move(removed_monkey_path,
                            os.path.join(MONKEYS_PATH, '.history', monkey_name, f'{timestamp}.yaml'))
                os.remove(os.path.join(MONKEYS_PATH, f'{monkey_name}.yaml'))
