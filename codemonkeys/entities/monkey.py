import re
from dataclasses import dataclass
from typing import Optional

from codemonkeys.defs import STOR_PATH
from codemonkeys.types import OStr
from codemonkeys.utils.config.monkey_validations import is_path_key, validate_path, is_model_key, validate_model, \
    validate_temp, is_temp_key, is_prompt_key
from codemonkeys.utils.defs_utils import load_class
from codemonkeys.utils.file_ops import get_file_contents
from codemonkeys.utils.monk.find_entity import find_entity
from codemonkeys.utils.monk.theme_functions import print_t, verbose_logs_enabled


@dataclass
class Monkey:
    _instance: Optional['Monkey'] = None
    _current_monkey: OStr = None

    # File Iteration
    WORK_PATH: str = f'{STOR_PATH}/work_path'
    INCLUDE_EXTS: tuple = ('.py', '.js')
    FILEPATH_MATCH_INCLUDE: tuple = ()
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', '__init__.py')
    FILTER_MAX_TOKENS: int = 3500

    # Main Prompts
    MAIN_PROMPT: str = "Please generate code for the following task..."
    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the contents of a python script, and nothing else."
    OUTPUT_EXAMPLE_PROMPT: OStr = "Limit your output to file contents, like: ```<new file contents>```."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = None
    CONTEXT_SUMMARY_PROMPT: OStr = None

    # Output Fixing
    FIX_OUTPUT_PROMPT: OStr = None

    # Output
    OUTPUT_PATH: str = f"{STOR_PATH}/output"
    OUTPUT_EXT: OStr = ".py"
    OUTPUT_FILENAME_APPEND: OStr = None
    SKIP_EXISTING_OUTPUT_FILES: bool = True
    RELATIVE_OUTPUT_PATHS: bool = True

    # Git
    GPT_GIT_COMMITS: bool = False
    GIT_REPO_PATH: OStr = None

    # Models
    MAIN_MODEL: str = 'gpt-4'
    SUMMARY_MODEL: str = 'gpt-4'
    FIX_OUTPUT_MODEL: str = 'gpt-3.5-turbo'

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0
    FIX_OUTPUT_TEMP: float = 0.5

    # Max Tokens
    MAIN_MAX_TOKENS: int = 8000
    SUMMARY_MAX_TOKENS: int = 8000
    FIX_OUTPUT_MAX_TOKENS: int = 8000

    def __post_init__(self):
        self._dynamic_validate()
        self._cop_paths()
        if verbose_logs_enabled():
            print_t(f"Loaded Monkey: {self.__dict__}", 'info')

    @classmethod
    def load(cls, name: OStr = None) -> 'Monkey':

        if cls._instance is None or cls._current_monkey != name:

            name, abspath = find_entity(name, 'monkey')
            cls._current_monkey = name
            cls._instance = load_class(abspath, name)()

        return cls._instance

    def _dynamic_validate(self) -> None:
        for key, value in self.__dict__.items():
            if is_path_key(key):
                setattr(self, key, validate_path(value, allow_none=True))
            elif is_model_key(key):
                setattr(self, key, validate_model(value, allow_none=True))
            elif is_temp_key(key):
                setattr(self, key, validate_temp(value, allow_none=True))

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
