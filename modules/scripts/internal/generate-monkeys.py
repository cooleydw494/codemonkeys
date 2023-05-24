import os
import yaml
from modules.definitions import MONKEYS_PATH

# Create the directory if it doesn't exist
os.makedirs(MONKEYS_PATH, exist_ok=True)

# Load the monkey configurations from the YAML file
monkey_manifest = os.path.join(MONKEYS_PATH, "monkey-manifest.yaml")
with open(monkey_manifest, "r") as f:
    monkeys = yaml.safe_load(f)

# Create the configuration files
for monkey, config in monkeys.items():
    with open(f"{MONKEYS_PATH}/{monkey}", "w") as f:
        for key, value in config.items():
            f.write(f"{key}='{value}'\n")
