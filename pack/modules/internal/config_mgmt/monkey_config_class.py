import os
from dataclasses import dataclass, field
from typing import Optional

from ruamel.yaml import YAML

from definitions import MONKEYS_PATH
from pack.modules.internal.config_mgmt.env_class import ENV
from pack.modules.internal.config_mgmt.monkey_config_validations import validate_str, \
    validate_bool, validate_int, validate_float


@dataclass
class MonkeyConfig:
    _instance = None

    # [MONKEY_CONFIG_PROPS_START]
    SPECIAL_FILE: Optional[str] = field(default=None)
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
    MAIN_MODEL: Optional[int] = field(default=None)
    SUMMARY_MODEL: Optional[int] = field(default=None)
    OUTPUT_CHECK_MODEL: Optional[int] = field(default=None)
    MAIN_TEMP: Optional[int] = field(default=None)
    SUMMARY_TEMP: Optional[int] = field(default=None)
    OUTPUT_CHECK_TEMP: Optional[float] = field(default=None)
    # [MONKEY_CONFIG_PROPS_END]

    ENV: Optional[ENV] = field(default=None)

    def __post_init__(self):
        env = ENV()
        for attribute in env.__annotations__:
            if getattr(self, attribute, None) is None and getattr(env, attribute, None) is not None:
                setattr(self, attribute, getattr(env, attribute))

        # [MONKEY_CONFIG_VALIDATIONS_START]
        self.SPECIAL_FILE = validate_str('SPECIAL_FILE', self.SPECIAL_FILE)
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
        self.MAIN_MODEL = validate_int('MAIN_MODEL', self.MAIN_MODEL)
        self.SUMMARY_MODEL = validate_int('SUMMARY_MODEL', self.SUMMARY_MODEL)
        self.OUTPUT_CHECK_MODEL = validate_int('OUTPUT_CHECK_MODEL', self.OUTPUT_CHECK_MODEL)
        self.MAIN_TEMP = validate_int('MAIN_TEMP', self.MAIN_TEMP)
        self.SUMMARY_TEMP = validate_int('SUMMARY_TEMP', self.SUMMARY_TEMP)
        self.OUTPUT_CHECK_TEMP = validate_float('OUTPUT_CHECK_TEMP', self.OUTPUT_CHECK_TEMP)
        # [MONKEY_CONFIG_VALIDATIONS_END]

        self.ENV = env

    @classmethod
    def load(cls, monkey_name: str) -> 'MonkeyConfig':
        if cls._instance is None:
            yaml = YAML(typ='safe')
            monkey_path = os.path.join(MONKEYS_PATH, f"{monkey_name}.yaml")
            if not os.path.exists(monkey_path):
                raise FileNotFoundError(f"Monkey configuration file {monkey_path} not found.")
            with open(monkey_path) as file:
                monkey_dict = yaml.load(file)
            cls._instance = MonkeyConfig(**monkey_dict)
            cls._instance.__post_init__()
        return cls._instance
