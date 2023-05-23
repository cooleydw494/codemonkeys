import json
import os
import subprocess
import sys

import openai
from termcolor import colored

from code_monkeys.modules.internal.get_gpt_client import instantiate_gpt_models
from code_monkeys.modules.internal.get_monkey_name import get_monkey_name
from code_monkeys.modules.customizable.process_file import process_file
from code_monkeys.modules.customizable.summarize_special_file import summarize_special_file


def check_env_vars():
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if openai.api_key is None:
            raise ValueError("OPENAI_API_KEY is not set.")
        work_path = os.getenv("WORK_PATH")
        if work_path is None:
            raise ValueError("WORK_PATH is not set.")
    except ValueError as error:
        print(colored(f"⚠️ {error}", "red"))
        exit(1)
    return work_path


def load_monkey_config(argv):
    monkey_name, monkey_config_file = get_monkey_name(argv)
    script_path = "../../load-monkey-config.py"
    process = subprocess.run(["python", script_path, monkey_config_file], check=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    if process.returncode != 0:
        print(colored(process.stderr.decode(), 'red'))
        exit(1)
    return json.loads(process.stdout.decode())


def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        print(colored("⚠️ Please provide the name of the monkey as a command-line argument.", "yellow"))
        exit(1)

    print(colored(
        "🚀 Welcome to the Monkeyspace! Let's wreak the opposite of havoc on your [whatever] with Monkey Power! 🌟",
        "green"))

    # Check and load environment variables
    work_path = check_env_vars()

    # Load monkey config
    monkey = load_monkey_config(sys.argv)

    # Instantiate necessary GPT models
    gpt_models = instantiate_gpt_models(monkey['MAIN_MODEL'], monkey['SUMMARY_MODEL'], monkey['USAGE_MODEL'])

    def gpt_client(model_name):
        return gpt_models.get(model_name)

    # Check if the special file exists
    if not os.path.isfile(monkey['SPECIAL_FILE']):
        print(colored(f"⚠️ Special file '{monkey['SPECIAL_FILE']}' not found.", "yellow"))
        exit(1)

    # Summarize the special file
    special_file_summary = summarize_special_file(monkey['SPECIAL_FILE'], monkey['SUMMARY_MODEL'],
                                                  monkey['SUMMARY_PROMPT'], gpt_client)
    print(colored("📋 Special file summarized successfully! 📝", 'green'))
    print(colored(f"📝 Summary: {special_file_summary}\n", 'cyan'))

    # Iterate over each file in the work_path
    for root, dirs, files in os.walk(work_path):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(file_path, monkey['USAGE_PROMPT'], special_file_summary, monkey['USAGE_MODEL'],
                         monkey['MAIN_PROMPT'], monkey['MAIN_MODEL'], gpt_client)


if __name__ == '__main__':
    main()
