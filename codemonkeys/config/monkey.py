import os
import re
from dataclasses import dataclass
from typing import Optional

from codemonkeys.defs import MONKEYS_PATH, ROOT_PATH
from codemonkeys.utils.config.monkey_validations import is_prompt_key, is_path_key
from codemonkeys.utils.file_ops import get_file_contents
from codemonkeys.utils.monk.get_monkey_name import get_monkey_name
from codemonkeys.utils.defs_utils import load_class
from codemonkeys.utils.monk.theme_functions import print_t, verbose_logs_enabled

(OStr, OBool, OInt, OFloat) = (Optional[str], Optional[bool], Optional[int], Optional[float])


@dataclass
class Monkey:
    _instance = None
    _current_monkey = None

    # General
    WORK_PATH: OStr = f'{ROOT_PATH}/stor/work_path'
    FILE_TYPES_INCLUDED: OStr = ".py"
    FILEPATH_MATCH_INCLUDE: OStr = None
    FILEPATH_MATCH_EXCLUDE: OStr = ".config,.md,.git,__init__.py"
    FILE_SELECT_MAX_TOKENS: OInt = 3000

    # Main Prompts
    MAIN_PROMPT: OStr = "Please generate code for the following task..."
    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the contents of a python script, and nothing else."
    OUTPUT_EXAMPLE_PROMPT: OStr = "Limit your output to file contents, like: ```<new file contents>```."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = f"{ROOT_PATH}/stor/context/context-file.txt"
    CONTEXT_SUMMARY_PROMPT: OStr = "Provide a summary of this file..."

    # Output Checks
    OUTPUT_CHECK_PROMPT: OStr = \
        'Examine the following output and determine if it contains the contents of a python script.' \
        ' Respond with only one word: "True" or "False".'
    OUTPUT_TRIES: OInt = 1

    # Output
    OUTPUT_PATH: OStr = f"{ROOT_PATH}/stor/output"
    OUTPUT_EXT: OStr = ".py"
    OUTPUT_FILENAME_APPEND: OStr = None
    OUTPUT_REMOVE_STRINGS: OStr = "```python\n,```python,```"
    SKIP_EXISTING_OUTPUT_FILES: OBool = True

    # Editor
    EDITOR_PROMPT: OStr = None
    EDITOR_PROMPT_ULTIMATUM: OStr = None

    # Output Splitting
    OUTPUT_SPLIT_PATH: OStr = None
    OUTPUT_SPLIT_TAG: OStr = '[SPLIT]'

    # Git
    COMMIT_STYLE: OStr = None
    STATIC_COMMIT_MESSAGE: OStr = 'File updated with CodeMonkeys.'

    # Models
    MAIN_MODEL: OStr = 'gpt-4'
    SUMMARY_MODEL: OStr = 'gpt-4'
    OUTPUT_CHECK_MODEL: OStr = 'gpt-3.5-turbo'

    # Temps
    MAIN_TEMP: OFloat = 1.0
    SUMMARY_TEMP: OFloat = 1.0
    OUTPUT_CHECK_TEMP: OFloat = 0.5

    # Max Tokens
    MAIN_MAX_TOKENS: OInt = 8000
    SUMMARY_MAX_TOKENS: OInt = 8000
    OUTPUT_CHECK_MAX_TOKENS: OInt = 8000

    def __post_init__(self):
        self._dynamic_validate()
        self._cop_paths()
        if verbose_logs_enabled():
            print_t(f"Loaded Monkey: {self.__dict__}", 'info')

    @classmethod
    def load(cls, name: str | None = None) -> 'Monkey':

        if cls._instance is None or cls._current_monkey != name:
            # Find or _prompt user to select
            name = get_monkey_name(name)
            cls._current_monkey = name
            file_path = os.path.join(MONKEYS_PATH, f"{name}.py")

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Monkey configuration file {file_path} not found.")

            cls._instance = load_class(file_path, name)()

        return cls._instance

    def _dynamic_validate(self) -> None:
        from codemonkeys.utils.config.monkey_validations import \
            validate_str, validate_bool, validate_int, validate_float, validate_path, validate_list_str

        for key, value in self.__dict__.items():
            if isinstance(value, bool):
                setattr(self, key, validate_bool(key, value))
            elif isinstance(value, int):
                setattr(self, key, validate_int(key, value))
            elif isinstance(value, float):
                setattr(self, key, validate_float(key, value))
            elif is_path_key(key):
                setattr(self, key, validate_path(key, value))
            elif isinstance(value, str):
                setattr(self, key, validate_str(key, value))
            elif isinstance(value, list):
                if all(isinstance(item, str) for item in value):
                    setattr(self, key, validate_list_str(key, value))

    def prompt_replace(self, to_replace, replace_with) -> 'Monkey':
        """
        Replaces any {prompt:<prompt_key>} placeholders with the provided value and returns a copy of the Monkey.

        :param to_replace: The placeholder to replace.
        :param replace_with: The value to replace the placeholder with.
        :return: A copy of the Monkey instance with the placeholders replaced.
        """
        copy = Monkey(**self.__dict__)
        for attr in vars(copy):
            value = getattr(copy, attr)
            if is_prompt_key(attr) and value is not None:
                setattr(copy, attr, value.replace(to_replace, replace_with))
        return copy

    def _cop_paths(self) -> None:
        """Replaces {cop:<filepath>} syntax within PROMPTs with file contents."""

        for attr, value in vars(self).items():
            if is_prompt_key(attr) and value and re.search(r'{cop:.*?}', value):
                try:
                    for match in re.findall(r'{cop:(.*?)}', value):
                        value = value.replace(f'{{cop:{match}}}', get_file_contents(match))
                    setattr(self, attr, value)
                except FileNotFoundError as e:
                    print_t(f"PROMPT cop file not found: {e}", 'error')

    def before_run(self) -> None:
        """Called before an Automation's run() method."""
        pass

    def after_run(self) -> None:
        """Called after an Automation's run() method."""
        pass
