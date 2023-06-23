import dataclasses
import os
import re
from dataclasses import dataclass

from defs import MONKEYS_PATH
from codemonkeys.utils.monkey_config.monkey_config_validations import is_prompt_key
from codemonkeys.config.yaml_helpers import get_monkey_config_defaults
from codemonkeys.utils.monk.theme_functions import print_t
from defs import import_env_class

ENV = import_env_class()


def insert_cop_file_contents(value: str) -> str:
    matches = re.findall(r'{cop:(.*?)}', value)
    for match in matches:
        expanded_path = os.path.expanduser(match)
        if os.path.isfile(expanded_path):
            with open(expanded_path, "r") as file:
                file_content = file.read()
            value = value.replace(f'{{cop:{match}}}', file_content)
        else:
            raise FileNotFoundError(f"Could not find the file specified in the 'cop' placeholder: {expanded_path}")
    return value


@dataclass
class MonkeyConfig:
    _instance = None

    """ MONKEY_CONFIG_PROPS - DO NOT MODIFY
        Definitions of MonkeyConfig props, generated from monkey-config-defaults. """
    # [MONKEY_CONFIG_PROPS_START]
    from typing import Optional

    from ruamel.yaml.scalarfloat import ScalarFloat
    from dataclasses import field
    WORK_PATH: Optional[str] = field(default=None)
    FILE_TYPES_INCLUDED: Optional[str] = field(default=None)
    FILEPATH_MATCH_EXCLUDED: Optional[str] = field(default=None)
    FILE_SELECT_MAX_TOKENS: Optional[int] = field(default=None)
    MAX_TOKENS: Optional[int] = field(default=None)
    MAIN_PROMPT: Optional[str] = field(default=None)
    MAIN_PROMPT_ULTIMATUM: Optional[str] = field(default=None)
    OUTPUT_EXAMPLE_PROMPT: Optional[str] = field(default=None)
    CONTEXT_FILE_PATH: Optional[str] = field(default=None)
    CONTEXT_SUMMARY_PROMPT: Optional[str] = field(default=None)
    CHECK_OUTPUT: Optional[bool] = field(default=None)
    OUTPUT_TRIES_LIMIT: Optional[int] = field(default=None)
    OUTPUT_CHECK_PROMPT: Optional[str] = field(default=None)
    OUTPUT_PATH: Optional[str] = field(default=None)
    OUTPUT_EXT: Optional[str] = field(default=None)
    OUTPUT_FILENAME_APPEND: Optional[str] = field(default=None)
    OUTPUT_REMOVE_STRINGS: Optional[str] = field(default=None)
    SKIP_EXISTING_OUTPUT_FILES: Optional[bool] = field(default=None)
    MAIN_MODEL: Optional[int] = field(default=None)
    SUMMARY_MODEL: Optional[int] = field(default=None)
    OUTPUT_CHECK_MODEL: Optional[int] = field(default=None)
    MAIN_TEMP: Optional[ScalarFloat] = field(default=None)
    SUMMARY_TEMP: Optional[ScalarFloat] = field(default=None)
    OUTPUT_CHECK_TEMP: Optional[ScalarFloat] = field(default=None)
    # [MONKEY_CONFIG_PROPS_END]

    ENV: Optional[ENV] = field(default=None)

    def __post_init__(self):
        # print_t(f"Loaded MonkeyConfig: {self.__dict__}", 'info')

        """ MONKEY_CONFIG_VALIDATIONS - DO NOT MODIFY
        Set MonkeyConfig props with validations, generated from monkey-config-defaults & monkey_config_validations. """
        # [MONKEY_CONFIG_VALIDATIONS_START]
        from codemonkeys.utils.monkey_config.monkey_config_validations import validate_str, validate_bool, validate_int, validate_float, validate_path
        self.WORK_PATH = validate_path('WORK_PATH', self.WORK_PATH)
        self.FILE_TYPES_INCLUDED = validate_str('FILE_TYPES_INCLUDED', self.FILE_TYPES_INCLUDED)
        self.FILEPATH_MATCH_EXCLUDED = validate_str('FILEPATH_MATCH_EXCLUDED', self.FILEPATH_MATCH_EXCLUDED)
        self.FILE_SELECT_MAX_TOKENS = validate_int('FILE_SELECT_MAX_TOKENS', self.FILE_SELECT_MAX_TOKENS)
        self.MAX_TOKENS = validate_int('MAX_TOKENS', self.MAX_TOKENS)
        self.MAIN_PROMPT = validate_str('MAIN_PROMPT', self.MAIN_PROMPT)
        self.MAIN_PROMPT_ULTIMATUM = validate_str('MAIN_PROMPT_ULTIMATUM', self.MAIN_PROMPT_ULTIMATUM)
        self.OUTPUT_EXAMPLE_PROMPT = validate_str('OUTPUT_EXAMPLE_PROMPT', self.OUTPUT_EXAMPLE_PROMPT)
        self.CONTEXT_FILE_PATH = validate_path('CONTEXT_FILE_PATH', self.CONTEXT_FILE_PATH)
        self.CONTEXT_SUMMARY_PROMPT = validate_str('CONTEXT_SUMMARY_PROMPT', self.CONTEXT_SUMMARY_PROMPT)
        self.CHECK_OUTPUT = validate_bool('CHECK_OUTPUT', self.CHECK_OUTPUT)
        self.OUTPUT_TRIES_LIMIT = validate_int('OUTPUT_TRIES_LIMIT', self.OUTPUT_TRIES_LIMIT)
        self.OUTPUT_CHECK_PROMPT = validate_str('OUTPUT_CHECK_PROMPT', self.OUTPUT_CHECK_PROMPT)
        self.OUTPUT_PATH = validate_path('OUTPUT_PATH', self.OUTPUT_PATH)
        self.OUTPUT_EXT = validate_str('OUTPUT_EXT', self.OUTPUT_EXT)
        self.OUTPUT_FILENAME_APPEND = validate_str('OUTPUT_FILENAME_APPEND', self.OUTPUT_FILENAME_APPEND)
        self.OUTPUT_REMOVE_STRINGS = validate_str('OUTPUT_REMOVE_STRINGS', self.OUTPUT_REMOVE_STRINGS)
        self.SKIP_EXISTING_OUTPUT_FILES = validate_bool('SKIP_EXISTING_OUTPUT_FILES', self.SKIP_EXISTING_OUTPUT_FILES)
        self.MAIN_MODEL = validate_int('MAIN_MODEL', self.MAIN_MODEL)
        self.SUMMARY_MODEL = validate_int('SUMMARY_MODEL', self.SUMMARY_MODEL)
        self.OUTPUT_CHECK_MODEL = validate_int('OUTPUT_CHECK_MODEL', self.OUTPUT_CHECK_MODEL)
        self.MAIN_TEMP = validate_float('MAIN_TEMP', self.MAIN_TEMP)
        self.SUMMARY_TEMP = validate_float('SUMMARY_TEMP', self.SUMMARY_TEMP)
        self.OUTPUT_CHECK_TEMP = validate_float('OUTPUT_CHECK_TEMP', self.OUTPUT_CHECK_TEMP)
        # [MONKEY_CONFIG_VALIDATIONS_END]

        self.ENV = ENV()

        self.cop_paths()

    @classmethod
    def load(cls, monkey_name: str) -> 'MonkeyConfig':
        from codemonkeys.config.yaml_helpers import read_yaml_file

        if cls._instance is None:
            monkey_path = os.path.join(MONKEYS_PATH, f"{monkey_name}.yaml")

            if not os.path.exists(monkey_path):
                raise FileNotFoundError(f"Monkey configuration file {monkey_path} not found.")

            monkey_dict = read_yaml_file(monkey_path, ruamel=True)
            monkey_dict = cls.filter_config_values(monkey_dict)
            monkey_dict = cls.apply_defaults(monkey_dict)

            cls._instance = MonkeyConfig(**monkey_dict)

        return cls._instance

    @classmethod
    def apply_default_and_validate(cls, data: dict):
        """
        Validate the provided dictionary with MonkeyConfig and return it.
        """

        data = cls.filter_config_values(data)
        data = cls.apply_defaults(data)

        # Create an instance of MonkeyConfig to perform validation
        try:
            validated_config = cls(**data)
        except (TypeError, ValueError) as e:
            print_t(f"MonkeyConfig Validation - {e}", 'error')
            exit()

        data = validated_config.__dict__
        data.pop('ENV', None)

        return data

    @classmethod
    def filter_config_values(cls, config_values: dict) -> dict:
        # Get dictionary of MonkeyConfig properties
        config_properties = {f.name for f in dataclasses.fields(cls)}
        config_properties.remove('ENV')

        # Remove any keys from data that aren't properties of the MonkeyConfig class
        config_values = {k: v for k, v in config_values.items() if k in config_properties}

        return config_values

    @classmethod
    def apply_defaults(cls, config_values: dict) -> dict:
        """
        Apply default values to the provided dictionary with MonkeyConfig and return it.
        If a value is set to None, it will be maintained as None.
        If a value isn't present, it will be set to the default value.
        :param config_values: dict
        :return: dict
        """

        # Get dictionary of MonkeyConfig properties so we don't default to env vars that aren't properties
        config_properties = {f.name for f in dataclasses.fields(cls)}
        config_properties.remove('ENV')

        monkey_config_defaults = get_monkey_config_defaults()
        for attribute in monkey_config_defaults:
            if config_values.get(attribute, '**unset') == '**unset' and monkey_config_defaults[attribute] is not None:
                config_values[attribute] = monkey_config_defaults[attribute]

        return config_values

    def replace_prompt_str(self, to_replace, replace_with):
        copy = MonkeyConfig(**self.__dict__)
        for attr in vars(copy):
            value = getattr(copy, attr)
            if is_prompt_key(attr) and value is not None:
                setattr(copy, attr, value.replace(to_replace, replace_with))
        return copy

    def cop_paths(self):
        # for each property containing 'PATH' word-bound (replace _ with ' '), do a replace on any string matching "{
        # cop:<a-file-path>}" with the read content of the file at <a-file-path>. Throw a clear error if the file
        # doesn't exist.
        for attr in vars(self):
            value = getattr(self, attr)
            if is_prompt_key(attr) and value is not None and re.search(r'{cop:.*?}', value):
                try:
                    new_value = insert_cop_file_contents(value)
                except FileNotFoundError as e:
                    print_t(f"{e}", 'error')
                    exit()
                setattr(self, attr, new_value)
