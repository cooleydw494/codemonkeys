import dataclasses
import os
from dataclasses import dataclass, field
from typing import Optional

from ruamel.yaml.scalarfloat import ScalarFloat

from definitions import MONKEYS_PATH
from pack.modules.internal.config_mgmt.env.env_class import ENV
from pack.modules.internal.config_mgmt.monkey_config.monkey_config_validations import validate_str, \
    validate_bool, validate_int, validate_float
from pack.modules.internal.config_mgmt.yaml_helpers import get_monkey_config_defaults, write_yaml_file


@dataclass
class MonkeyConfig:
    _instance = None

    # [MONKEY_CONFIG_PROPS_START]
    FILE_TYPES_INCLUDED: Optional[str] = field(default=None)
    FILEPATH_MATCH_EXCLUDED: Optional[str] = field(default=None)
    FILE_SELECT_MAX_TOKENS: Optional[int] = field(default=None)
    SPECIAL_FILE_PATH: Optional[str] = field(default=None)
    WORK_PATH: Optional[str] = field(default=None)
    MAIN_PROMPT: Optional[str] = field(default=None)
    SUMMARY_PROMPT: Optional[str] = field(default=None)
    MAIN_PROMPT_ULTIMATUM: Optional[str] = field(default=None)
    OUTPUT_EXAMPLE: Optional[str] = field(default=None)
    CHECK_OUTPUT: Optional[bool] = field(default=None)
    OUTPUT_CHECK_PROMPT: Optional[str] = field(default=None)
    OUTPUT_PATH: Optional[str] = field(default=None)
    OUTPUT_EXT: Optional[str] = field(default=None)
    OUTPUT_FILENAME_APPEND: Optional[str] = field(default=None)
    OUTPUT_TRIES_LIMIT: Optional[int] = field(default=None)
    MAIN_MODEL: Optional[int] = field(default=None)
    SUMMARY_MODEL: Optional[int] = field(default=None)
    OUTPUT_CHECK_MODEL: Optional[int] = field(default=None)
    MAIN_TEMP: Optional[ScalarFloat] = field(default=None)
    SUMMARY_TEMP: Optional[ScalarFloat] = field(default=None)
    OUTPUT_CHECK_TEMP: Optional[ScalarFloat] = field(default=None)
    # [MONKEY_CONFIG_PROPS_END]

    ENV: Optional[ENV] = field(default=None)

    def __post_init__(self):
        env = ENV()
        for attribute in env.__annotations__:
            if getattr(self, attribute, None) is None and getattr(env, attribute, None) is not None:
                setattr(self, attribute, getattr(env, attribute))

        monkey_config_defaults = get_monkey_config_defaults()
        for attribute in monkey_config_defaults:
            if getattr(self, attribute, None) is None and monkey_config_defaults[attribute] is not None:
                setattr(self, attribute, monkey_config_defaults[attribute])

        # [MONKEY_CONFIG_VALIDATIONS_START]
        self.FILE_TYPES_INCLUDED = validate_str('FILE_TYPES_INCLUDED', self.FILE_TYPES_INCLUDED)
        self.FILEPATH_MATCH_EXCLUDED = validate_str('FILEPATH_MATCH_EXCLUDED', self.FILEPATH_MATCH_EXCLUDED)
        self.FILE_SELECT_MAX_TOKENS = validate_int('FILE_SELECT_MAX_TOKENS', self.FILE_SELECT_MAX_TOKENS)
        self.SPECIAL_FILE_PATH = validate_str('SPECIAL_FILE_PATH', self.SPECIAL_FILE_PATH)
        self.WORK_PATH = validate_str('WORK_PATH', self.WORK_PATH)
        self.MAIN_PROMPT = validate_str('MAIN_PROMPT', self.MAIN_PROMPT)
        self.SUMMARY_PROMPT = validate_str('SUMMARY_PROMPT', self.SUMMARY_PROMPT)
        self.MAIN_PROMPT_ULTIMATUM = validate_str('MAIN_PROMPT_ULTIMATUM', self.MAIN_PROMPT_ULTIMATUM)
        self.OUTPUT_EXAMPLE = validate_str('OUTPUT_EXAMPLE', self.OUTPUT_EXAMPLE)
        self.CHECK_OUTPUT = validate_bool('CHECK_OUTPUT', self.CHECK_OUTPUT)
        self.OUTPUT_CHECK_PROMPT = validate_str('OUTPUT_CHECK_PROMPT', self.OUTPUT_CHECK_PROMPT)
        self.OUTPUT_PATH = validate_str('OUTPUT_PATH', self.OUTPUT_PATH)
        self.OUTPUT_EXT = validate_str('OUTPUT_EXT', self.OUTPUT_EXT)
        self.OUTPUT_FILENAME_APPEND = validate_str('OUTPUT_FILENAME_APPEND', self.OUTPUT_FILENAME_APPEND)
        self.OUTPUT_TRIES_LIMIT = validate_int('OUTPUT_TRIES_LIMIT', self.OUTPUT_TRIES_LIMIT)
        self.MAIN_MODEL = validate_int('MAIN_MODEL', self.MAIN_MODEL)
        self.SUMMARY_MODEL = validate_int('SUMMARY_MODEL', self.SUMMARY_MODEL)
        self.OUTPUT_CHECK_MODEL = validate_int('OUTPUT_CHECK_MODEL', self.OUTPUT_CHECK_MODEL)
        self.MAIN_TEMP = validate_float('MAIN_TEMP', self.MAIN_TEMP)
        self.SUMMARY_TEMP = validate_float('SUMMARY_TEMP', self.SUMMARY_TEMP)
        self.OUTPUT_CHECK_TEMP = validate_float('OUTPUT_CHECK_TEMP', self.OUTPUT_CHECK_TEMP)
        # [MONKEY_CONFIG_VALIDATIONS_END]

        self.ENV = env

    @classmethod
    def load(cls, monkey_name: str) -> 'MonkeyConfig':
        from pack.modules.internal.config_mgmt.yaml_helpers import read_yaml_file

        if cls._instance is None:
            monkey_path = os.path.join(MONKEYS_PATH, f"{monkey_name}.yaml")

            if not os.path.exists(monkey_path):
                raise FileNotFoundError(f"Monkey configuration file {monkey_path} not found.")

            monkey_dict = read_yaml_file(monkey_path, ruamel=True)

            # Get the properties defined in MonkeyConfig
            config_properties = {f.name for f in dataclasses.fields(cls)}

            # Filter out any keys in monkey_dict that are not properties of MonkeyConfig
            monkey_dict = {k: v for k, v in monkey_dict.items() if k in config_properties}

            cls._instance = MonkeyConfig(**monkey_dict)
            cls._instance.__post_init__()

        return cls._instance

    @classmethod
    def validate_and_write_yaml(cls, data: dict, file_path: str):
        """
        Validate the provided dictionary with MonkeyConfig and write it to a YAML file, skipping 'ENV' field.

        Args:
            data (dict): The dictionary to validate and write to a YAML file.
            file_path (str): The path of the YAML file to write to.
        """

        # Get dictionary of MonkeyConfig properties
        config_properties = {f.name for f in dataclasses.fields(cls)}

        # Remove any keys from data that aren't properties of the MonkeyConfig class
        data = {k: v for k, v in data.items() if k in config_properties}

        # Create an instance of MonkeyConfig to perform validation
        validated_config = cls(**data)

        data = validated_config.__dict__
        data.pop('ENV', None)  # Use dict.pop with default to avoid KeyError if ENV doesn't exist

        # Write to the file
        write_yaml_file(file_path, data, ruamel=True)
