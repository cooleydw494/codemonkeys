import os
from dataclasses import dataclass, field
from typing import Union, Any, Optional

from ruamel.yaml import YAML

from definitions import MONKEYS_PATH
from pack.modules.internal.cm_config_mgmt.env_class import ENV


@dataclass
class MonkeyConfig:
    _instance = None

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
    MAIN_TEMP: Optional[float] = field(default=None)
    SUMMARY_TEMP: Optional[float] = field(default=None)
    OUTPUT_CHECK_TEMP: Optional[float] = field(default=None)
    ENV: Optional[ENV] = field(default=None)

    def __post_init__(self):
        env = ENV()
        for attribute in env.__annotations__:
            if getattr(self, attribute, None) is None and getattr(env, attribute, None) is not None:
                setattr(self, attribute, getattr(env, attribute))

        self.SPECIAL_FILE = self._validate_path('SPECIAL_FILE', self.SPECIAL_FILE)
        self.WORK_PATH = self._validate_path('WORK_PATH', self.WORK_PATH)
        self.MAIN_MODEL = self._validate_range('MAIN_MODEL', self.MAIN_MODEL, min_value=3, max_value=4)
        self.SUMMARY_MODEL = self._validate_range('SUMMARY_MODEL', self.SUMMARY_MODEL, min_value=3, max_value=4)
        self.OUTPUT_CHECK_MODEL = self._validate_range('OUTPUT_CHECK_MODEL', self.OUTPUT_CHECK_MODEL, min_value=3, max_value=4)
        self.MAIN_TEMP = self._validate_range('MAIN_TEMP', self.MAIN_TEMP, min_value=0, max_value=1)
        self.SUMMARY_TEMP = self._validate_range('SUMMARY_TEMP', self.SUMMARY_TEMP, min_value=0, max_value=1)
        self.OUTPUT_CHECK_TEMP = self._validate_range('OUTPUT_CHECK_TEMP', self.OUTPUT_CHECK_TEMP, min_value=0, max_value=1)
        self.ENV = env

    @staticmethod
    def _validate_path(key, path: str) -> str:
        absolute_path = os.path.expanduser(path)
        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"{key} value {absolute_path} does not exist. Make sure it is a valid absolute path.")
        return str(absolute_path)

    @staticmethod
    def _validate_range(key, value: Union[int, float], min_value: Any = None, max_value: Any = None) -> Union[int, float]:
        if min_value is not None and value < min_value:
            raise ValueError(f"{key} value {value} is less than the minimum value {min_value}")
        if max_value is not None and value > max_value:
            raise ValueError(f"{key} value {value} is greater than the maximum value {max_value}")
        return value

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
