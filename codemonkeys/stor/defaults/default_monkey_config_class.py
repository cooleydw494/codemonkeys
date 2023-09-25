from dataclasses import dataclass

from codemonkeys.utils.monk.theme_functions import print_t, verbose_logs_enabled
from codemonkeys.config.monkey_config import MonkeyConfig as CMMonkeyConfig

try:
    from config.framework.env import Env
except ImportError:
    print_t('Could not import user Env class from config.framework.env. Using default Env class.', 'warning')
    from codemonkeys.config.env import Env


@dataclass
class MonkeyConfig(CMMonkeyConfig):
    _instance = None

    """ MONKEY_CONFIG_PROPS - DO NOT MODIFY
        Definitions of MonkeyConfig props, generated from monkey-config-defaults. """
    # [MONKEY_CONFIG_PROPS_START]
    from types import NoneType
    from typing import Optional

    from ruamel.yaml.scalarfloat import ScalarFloat
    from dataclasses import field
    WORK_PATH: Optional[str] = field(default=None)
    FILE_TYPES_INCLUDED: Optional[str] = field(default=None)
    FILEPATH_MATCH_INCLUDE: Optional[NoneType] = field(default=None)
    FILEPATH_MATCH_EXCLUDE: Optional[str] = field(default=None)
    FILE_SELECT_MAX_TOKENS: Optional[int] = field(default=None)
    MAIN_PROMPT: Optional[str] = field(default=None)
    MAIN_PROMPT_ULTIMATUM: Optional[str] = field(default=None)
    OUTPUT_EXAMPLE_PROMPT: Optional[str] = field(default=None)
    CONTEXT_FILE_PATH: Optional[NoneType] = field(default=None)
    CONTEXT_SUMMARY_PROMPT: Optional[NoneType] = field(default=None)
    OUTPUT_CHECK_PROMPT: Optional[NoneType] = field(default=None)
    OUTPUT_TRIES: Optional[int] = field(default=None)
    OUTPUT_PATH: Optional[str] = field(default=None)
    OUTPUT_EXT: Optional[str] = field(default=None)
    OUTPUT_FILENAME_APPEND: Optional[str] = field(default=None)
    OUTPUT_REMOVE_STRINGS: Optional[str] = field(default=None)
    SKIP_EXISTING_OUTPUT_FILES: Optional[bool] = field(default=None)
    EDITOR_PROMPT: Optional[NoneType] = field(default=None)
    EDITOR_PROMPT_ULTIMATUM: Optional[NoneType] = field(default=None)
    OUTPUT_SPLIT_PATH: Optional[NoneType] = field(default=None)
    OUTPUT_SPLIT_TAG: Optional[str] = field(default=None)
    COMMIT_STYLE: Optional[NoneType] = field(default=None)
    STATIC_COMMIT_MESSAGE: Optional[str] = field(default=None)
    MAIN_MODEL: Optional[str] = field(default=None)
    SUMMARY_MODEL: Optional[str] = field(default=None)
    OUTPUT_CHECK_MODEL: Optional[str] = field(default=None)
    MAIN_TEMP: Optional[ScalarFloat] = field(default=None)
    SUMMARY_TEMP: Optional[ScalarFloat] = field(default=None)
    OUTPUT_CHECK_TEMP: Optional[ScalarFloat] = field(default=None)
    MAIN_MAX_TOKENS: Optional[int] = field(default=None)
    SUMMARY_MAX_TOKENS: Optional[int] = field(default=None)
    OUTPUT_CHECK_MAX_TOKENS: Optional[int] = field(default=None)
    # [MONKEY_CONFIG_PROPS_END]

    env: Optional[Env] = field(default=None)

    def __post_init__(self):

        if verbose_logs_enabled():
            print_t(f"Loaded MonkeyConfig: {self.__dict__}", 'info')

        """ MONKEY_CONFIG_VALIDATIONS - DO NOT MODIFY
        Set MonkeyConfig props with validations, generated from monkey-config-defaults & monkey_config_validations. """
        # [MONKEY_CONFIG_VALIDATIONS_START]
        from codemonkeys.utils.monkey_config.monkey_config_validations import validate_str, validate_bool, validate_int, validate_float, validate_path, validate_list_str
        self.WORK_PATH = validate_path('WORK_PATH', self.WORK_PATH)
        self.FILE_TYPES_INCLUDED = validate_str('FILE_TYPES_INCLUDED', self.FILE_TYPES_INCLUDED)
        self.FILEPATH_MATCH_EXCLUDE = validate_str('FILEPATH_MATCH_EXCLUDE', self.FILEPATH_MATCH_EXCLUDE)
        self.FILE_SELECT_MAX_TOKENS = validate_int('FILE_SELECT_MAX_TOKENS', self.FILE_SELECT_MAX_TOKENS)
        self.MAIN_PROMPT = validate_str('MAIN_PROMPT', self.MAIN_PROMPT)
        self.MAIN_PROMPT_ULTIMATUM = validate_str('MAIN_PROMPT_ULTIMATUM', self.MAIN_PROMPT_ULTIMATUM)
        self.OUTPUT_EXAMPLE_PROMPT = validate_str('OUTPUT_EXAMPLE_PROMPT', self.OUTPUT_EXAMPLE_PROMPT)
        self.CONTEXT_FILE_PATH = validate_path('CONTEXT_FILE_PATH', self.CONTEXT_FILE_PATH)
        self.OUTPUT_TRIES = validate_int('OUTPUT_TRIES', self.OUTPUT_TRIES)
        self.OUTPUT_PATH = validate_path('OUTPUT_PATH', self.OUTPUT_PATH)
        self.OUTPUT_EXT = validate_str('OUTPUT_EXT', self.OUTPUT_EXT)
        self.OUTPUT_FILENAME_APPEND = validate_str('OUTPUT_FILENAME_APPEND', self.OUTPUT_FILENAME_APPEND)
        self.OUTPUT_REMOVE_STRINGS = validate_str('OUTPUT_REMOVE_STRINGS', self.OUTPUT_REMOVE_STRINGS)
        self.SKIP_EXISTING_OUTPUT_FILES = validate_bool('SKIP_EXISTING_OUTPUT_FILES', self.SKIP_EXISTING_OUTPUT_FILES)
        self.OUTPUT_SPLIT_PATH = validate_path('OUTPUT_SPLIT_PATH', self.OUTPUT_SPLIT_PATH)
        self.OUTPUT_SPLIT_TAG = validate_str('OUTPUT_SPLIT_TAG', self.OUTPUT_SPLIT_TAG)
        self.STATIC_COMMIT_MESSAGE = validate_str('STATIC_COMMIT_MESSAGE', self.STATIC_COMMIT_MESSAGE)
        self.MAIN_MODEL = validate_str('MAIN_MODEL', self.MAIN_MODEL)
        self.SUMMARY_MODEL = validate_str('SUMMARY_MODEL', self.SUMMARY_MODEL)
        self.OUTPUT_CHECK_MODEL = validate_str('OUTPUT_CHECK_MODEL', self.OUTPUT_CHECK_MODEL)
        self.MAIN_TEMP = validate_float('MAIN_TEMP', self.MAIN_TEMP)
        self.SUMMARY_TEMP = validate_float('SUMMARY_TEMP', self.SUMMARY_TEMP)
        self.OUTPUT_CHECK_TEMP = validate_float('OUTPUT_CHECK_TEMP', self.OUTPUT_CHECK_TEMP)
        self.MAIN_MAX_TOKENS = validate_int('MAIN_MAX_TOKENS', self.MAIN_MAX_TOKENS)
        self.SUMMARY_MAX_TOKENS = validate_int('SUMMARY_MAX_TOKENS', self.SUMMARY_MAX_TOKENS)
        self.OUTPUT_CHECK_MAX_TOKENS = validate_int('OUTPUT_CHECK_MAX_TOKENS', self.OUTPUT_CHECK_MAX_TOKENS)
        # [MONKEY_CONFIG_VALIDATIONS_END]

        self.env = Env.get()
