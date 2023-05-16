import os
import yaml

# Define the directory for the configuration files
directory = "monkeys"

# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)

# Load the monkey configurations from the YAML file
with open("monkey-manifest.yaml", "r") as f:
    monkeys = yaml.safe_load(f)

# Create the configuration files
for monkey, config in monkeys.items():
    with open(f"{directory}/{monkey}", "w") as f:
        for key, value in config.items():
            f.write(f"{key}='{value}'\n")

