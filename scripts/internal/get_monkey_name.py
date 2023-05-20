import os
import pathlib

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_monkey_name(argv):
    monkey_name = None
    default_monkey = os.getenv("DEFAULT_MONKEY")

    # Get monkey name from command-line arg & load config
    if len(argv) < 2:
        if default_monkey:
            default_monkey_config_file = f"../monkeys/{default_monkey}"
            # If no monkey name provided, use default if it exists
            if pathlib.Path(default_monkey_config_file).exists():
                print(f"🐒 No monkey name provided. Loading default monkey configuration from {default_monkey}...")
                monkey_config_file = default_monkey_config_file
            else:
                print(
                    f"⚠️ No monkey name provided and default configuration {default_monkey} not found. Please specify a monkey name.")
                exit(1)
        else:
            print("⚠️ No monkey name provided and no default monkey configured. Please specify a monkey name.")
            exit(1)
    else:
        monkey_name = argv[1]
        monkey_config_file = f"../monkeys/{monkey_name}"
        print(f"🐒 Loading {monkey_name} monkey configuration...")

    return monkey_name, monkey_config_file
