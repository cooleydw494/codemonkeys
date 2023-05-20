import os

import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the directory for the configuration files
monkeys_directory = os.path.join(os.getenv("BASE_DIR_ABS_PATH"), "monkeys")

# Create the directory if it doesn't exist
os.makedirs(monkeys_directory, exist_ok=True)

# Load the monkey configurations from the YAML file
monkey_manifest = os.path.join(monkeys_directory, "monkey-manifest.yaml")
with open(monkey_manifest, "r") as f:
    monkeys = yaml.safe_load(f)

# Create the configuration files
for monkey, config in monkeys.items():
    with open(f"{monkeys_directory}/{monkey}", "w") as f:
        for key, value in config.items():
            f.write(f"{key}='{value}'\n")
