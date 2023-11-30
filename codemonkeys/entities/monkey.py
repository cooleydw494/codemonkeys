import re
from dataclasses import dataclass
from typing import Optional

from codemonkeys.types import OStr
from codemonkeys.utils.config.monkey_validations import is_path_key, validate_path, is_model_key, validate_model, \
    validate_temp, is_temp_key, is_prompt_key
from codemonkeys.utils.misc.defs_utils import load_class
from codemonkeys.utils.misc.file_ops import get_file_contents
from codemonkeys.utils.misc.handle_exception import handle_exception
from codemonkeys.utils.monk.find_entity import find_entity
from codemonkeys.utils.monk.theme_functions import print_t, verbose_logs_enabled, print_table
from codemonkeys.defs import STOR_PATH


@dataclass
class Monkey:
    """
    A configuration entity for defining monkey behavior in the CodeMonkeys framework.

    The Monkey class holds configuration that determines the file iteration behavior,
    prompt composition, model selections, and output settings for GPT-powered
    file operations within the CodeMonkeys automation tasks.

    Attributes:
        WORK_PATH: The directory path where file processing will take place.
        INCLUDE_EXTS: A tuple of file extensions to include during processing.
        FILEPATH_MATCH_INCLUDE: A tuple of file patterns to specifically include during iteration.
        FILEPATH_MATCH_EXCLUDE: A tuple of file patterns to exclude during iteration.
        FILTER_MAX_TOKENS: The maximum number of tokens each file must be below to be processed.
        FILE_SELECT_PROMPT: An optional string to define a specific prompt when selecting files for processing.
        MAIN_PROMPT: The primary prompt text provided to GPT models during processing.
        MAIN_PROMPT_ULTIMATUM: An additional prompt to limit GPT responses to appropriate content.
        OUTPUT_PROMPT: A prompt that instructs GPT to specifically format the output.
        CONTEXT_FILE_PATH: An optional path for providing additional context during GPT processing.
        CONTEXT_SUMMARY_PROMPT: An optional prompt that can provide summary information for context.
        OUTPUT_PATH: The directory path where processed outputs will be stored.
        OUTPUT_EXT: The file extension for output files.
        OUTPUT_FILENAME_APPEND: An optional string to append to output filenames.
        SKIP_EXISTING_OUTPUT_FILES: A boolean that indicates whether existing output files should be skipped.
        RELATIVE_OUTPUT_PATHS: A boolean to indicate if output paths should be relative to the WORK_PATH.
        GPT_GIT_COMMITS: A boolean indicating whether GPT should make git commits after processing.
        GIT_REPO_PATH: An optional path that directs where GPT should perform git operations.
        MAIN_MODEL: The GPT model used for the main processing.
        SUMMARY_MODEL: The GPT model used for generating summaries if needed.
        FILE_SELECT_MODEL: The model used when prompting for file selection.
        MAIN_TEMP: The temperature setting for the main model processing.
        SUMMARY_TEMP: The temperature setting for summary model processing.
        FILE_SELECT_TEMP: The temperature setting for the file selection model.
        MAIN_MAX_TOKENS: The maximum token count allowed for the main processing responses.
        SUMMARY_MAX_TOKENS: The maximum token count allowed for summary responses.
        FILE_SELECT_MAX_TOKENS: The maximum token count for file selection prompts.
    """

    _instance: Optional['Monkey'] = None
    _current_monkey: OStr = None
    _mixins: tuple = ()

    # File Iteration
    WORK_PATH: str = f"{STOR_PATH}/work_path"
    INCLUDE_EXTS: tuple = ('.py',)
    FILEPATH_MATCH_INCLUDE: tuple = ()
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', 'help', '__', 'defs.py')
    FILTER_MAX_TOKENS: int = 8000

    # GPT File Selection
    FILE_SELECT_PROMPT: OStr = None

    # Main Prompts
    MAIN_PROMPT: str = "Please generate code for the following task..."
    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the contents of a python script, and nothing else."
    OUTPUT_PROMPT: OStr = "Output should be nothing more than the updated file contents."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = None
    CONTEXT_SUMMARY_PROMPT: OStr = None

    # Output
    OUTPUT_PATH: str = f"{STOR_PATH}/output"
    OUTPUT_EXT: OStr = None
    OUTPUT_FILENAME_APPEND: OStr = None
    OUTPUT_FILENAME_PREPEND: OStr = None
    SKIP_EXISTING_OUTPUT_FILES: bool = False

    # Git
    GPT_GIT_COMMITS: bool = False
    GIT_REPO_PATH: OStr = None

    # Models
    MAIN_MODEL: str = 'gpt-4-1106-preview'
    SUMMARY_MODEL: str = 'gpt-4-1106-preview'
    FILE_SELECT_MODEL: str = 'gpt-3.5-turbo'

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0
    FILE_SELECT_TEMP: float = 0.8

    # Max Tokens
    MAIN_MAX_TOKENS: int = 8000
    SUMMARY_MAX_TOKENS: int = 8000
    FILE_SELECT_MAX_TOKENS: int = 4000

    def __post_init__(self):
        self._apply_mixins()
        self._dynamic_validate()
        self._cop_paths()
        self.print_monkey_details()

    @classmethod
    def load(cls, name: OStr = None) -> 'Monkey':

        if cls._instance is None or cls._current_monkey != name:
            name, abspath = find_entity(name or '', 'monkey')
            cls._current_monkey = name
            cls._instance = load_class(abspath, name)()

        return cls._instance

    def _apply_mixins(self):
        if hasattr(self, 'mixins'):
            self._mixins = getattr(self, 'mixins')
        final_subclass_attrs = self.attrs_defined_in_final_subclass()
        for mixin in self._mixins:
            for key, value in vars(mixin).items():
                if not key.startswith("__") and key not in final_subclass_attrs:
                    setattr(self, key, value)

    @classmethod
    def attrs_defined_in_final_subclass(cls):
        # Get the dictionary of attributes for the most specific subclass
        final_subclass_attrs = vars(cls.__mro__[0])
        # Prepare a set to collect attributes from base classes for comparison
        base_attrs = set()
        # Collect attributes from all base classes
        for base_class in cls.__mro__[1:]:
            base_attrs.update(vars(base_class))
        # Determine which attributes are defined in the final subclass but not in the base classes
        # Or if they are redefined in the final subclass
        unique_attrs = {attr for attr in final_subclass_attrs if attr not in base_attrs or final_subclass_attrs[attr] is not vars(base_class).get(attr, None)}
        return list(unique_attrs)

    def _dynamic_validate(self) -> None:
        for key, value in self.__dict__.items():

            if is_path_key(key):
                try:
                    setattr(self, key, validate_path(value, allow_none=True))
                except BaseException as e:
                    print_t(f"PATH validation failed for {key}={value}, {self.__class__.__name__}.", 'error')
                    handle_exception(e, always_exit=True)

            elif is_model_key(key):
                try:
                    setattr(self, key, validate_model(value, allow_none=True))
                except BaseException as e:
                    print_t(f"MODEL validation failed for {key}={value}, {self.__class__.__name__}.", 'error')
                    handle_exception(e, always_exit=True)

            elif is_temp_key(key):
                try:
                    setattr(self, key, validate_temp(value, allow_none=True))
                except BaseException as e:
                    print_t(f"TEMP validation failed for {key}={value}, {self.__class__.__name__}.", 'error')
                    handle_exception(e, always_exit=True)

    def _cop_paths(self) -> None:
        """Replaces {cop:<filepath>} syntax within PROMPTs with file contents."""

        for attr, value in vars(self).items():
            if is_prompt_key(attr) and value and re.search(r'{cop:.*?}', value):
                try:
                    for match in re.findall(r'{cop:(.*?)}', value):
                        value = value.replace(f'{{cop:{match}}}', get_file_contents(match))
                    setattr(self, attr, value)
                except FileNotFoundError as e:
                    print_t(f"PROMPT cop-file not found for {attr}", 'error')
                    handle_exception(e, always_exit=True)

    def print_monkey_details(self) -> None:
        print_t(f'Monkey Loaded: {self.__class__.__name__}', 'start')
        if verbose_logs_enabled():
            filtered_props = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
            rows = [[k, str(v)[:64] + '...' if len(str(v)) > 64 else str(v)] for k, v in filtered_props.items()]
            print()
            print_table({
                "headers": ["Prop", "Computed Value"],
                "show_headers": True,
                "rows": rows,
            })
            print()

    def before_run(self) -> None:
        """Called before an Automation's run() method."""
        pass

    def after_run(self) -> None:
        """Called after an Automation's run() method."""
        pass
