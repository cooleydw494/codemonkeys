import dataclasses
import os
import re
from dataclasses import dataclass

from codemonkeys.config.yaml_helpers import get_monkey_config_defaults
from codemonkeys.defs import MONKEYS_PATH
from codemonkeys.utils.monk.get_monkey_name import get_monkey_name
from codemonkeys.utils.monk.theme_functions import print_t, verbose_logs_enabled
from codemonkeys.utils.monkey_config.monkey_config_validations import is_prompt_key, is_path_key


@dataclass
class MonkeyConfig:

    _instance = None
    _current_monkey = None

    # DO NOT MODIFY - generated from monkey-config-defaults.
    # [MONKEY_CONFIG_PROPS_START]
    from types import NoneType
    from typing import Optional

    from dataclasses import field
    WORK_PATH: Optional[str] = field(default=None)
    FILE_TYPES_INCLUDED: Optional[str] = field(default=None)
    FILEPATH_MATCH_INCLUDE: Optional[NoneType] = field(default=None)
    FILEPATH_MATCH_EXCLUDE: Optional[str] = field(default=None)
    FILE_SELECT_MAX_TOKENS: Optional[int] = field(default=None)
    MAX_TOKENS: Optional[int] = field(default=None)
    MAIN_PROMPT: Optional[str] = field(default=None)
    MAIN_PROMPT_ULTIMATUM: Optional[str] = field(default=None)
    OUTPUT_EXAMPLE_PROMPT: Optional[str] = field(default=None)
    CONTEXT_FILE_PATH: Optional[str] = field(default=None)
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
    MAIN_TEMP: Optional[float] = field(default=None)
    SUMMARY_TEMP: Optional[float] = field(default=None)
    OUTPUT_CHECK_TEMP: Optional[float] = field(default=None)
    MAIN_MAX_TOKENS: Optional[int] = field(default=None)
    SUMMARY_MAX_TOKENS: Optional[int] = field(default=None)
    OUTPUT_CHECK_MAX_TOKENS: Optional[int] = field(default=None)
    # [MONKEY_CONFIG_PROPS_END]

    def __post_init__(self):
        self._dynamic_validate()
        self._cop_paths()
        if verbose_logs_enabled():
            print_t(f"Loaded MonkeyConfig: {self.__dict__}", 'info')

    @classmethod
    def load(cls, monkey_name: str | None = None) -> 'MonkeyConfig':
        from codemonkeys.config.yaml_helpers import read_yaml_file

        if cls._instance is None or cls._current_monkey != monkey_name:
            monkey_name = get_monkey_name(monkey_name)  # Find or _prompt user to select
            cls._current_monkey = monkey_name
            monkey_path = os.path.join(MONKEYS_PATH, f"{monkey_name}.yaml")

            if not os.path.exists(monkey_path):
                raise FileNotFoundError(f"Monkey configuration file {monkey_path} not found.")

            monkey_dict = read_yaml_file(monkey_path)
            monkey_dict = cls._filter_config_values(monkey_dict)
            monkey_dict = cls._apply_defaults(monkey_dict)

            cls._instance = MonkeyConfig(**monkey_dict)

        return cls._instance

    @classmethod
    def _filter_config_values(cls, config_values: dict) -> dict:
        # Get dictionary of MonkeyConfig properties
        config_properties = {f.name for f in dataclasses.fields(cls)}

        # Remove any keys from data that aren't properties of the MonkeyConfig class
        config_values = {k: v for k, v in config_values.items() if k in config_properties}

        return config_values

    @classmethod
    def _apply_defaults(cls, config_values: dict) -> dict:
        """
        Apply default values to the provided dictionary with MonkeyConfig and return it.
        If a value is set to None, it will be maintained as None.
        If a value isn't present, it will be set to the default value.
        :param config_values: dict
        :return: dict
        """

        monkey_config_defaults = get_monkey_config_defaults()
        for attribute in monkey_config_defaults:
            if config_values.get(attribute, '**unset') == '**unset' and monkey_config_defaults[attribute] is not None:
                config_values[attribute] = monkey_config_defaults[attribute]

        return config_values

    def _dynamic_validate(self) -> None:
        from codemonkeys.utils.monkey_config.monkey_config_validations import \
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

    def replace_prompt_str(self, to_replace, replace_with) -> 'MonkeyConfig':
        """
        Replaces any {prompt:<prompt_key>} placeholders with the provided value and returns a copy of the MonkeyConfig.

        :param to_replace: The placeholder to replace.
        :param replace_with: The value to replace the placeholder with.
        :return: A copy of the MonkeyConfig instance with the placeholders replaced.
        """
        copy = MonkeyConfig(**self.__dict__)
        for attr in vars(copy):
            value = getattr(copy, attr)
            if is_prompt_key(attr) and value is not None:
                setattr(copy, attr, value.replace(to_replace, replace_with))
        return copy

    def _cop_paths(self) -> None:
        """
        Replaces any {cop:<filepath>} placeholders with the contents of the file at <filepath>.
        """
        for attr in vars(self):
            value = getattr(self, attr)
            if is_prompt_key(attr) and value is not None and re.search(r'{cop:.*?}', value):
                try:
                    new_value = self.insert_cop_file_contents(value)
                except FileNotFoundError as e:
                    print_t(f"{e}", 'error')
                    exit()
                setattr(self, attr, new_value)

    @classmethod
    def insert_cop_file_contents(cls, value: str) -> str:
        """
        Replaces any {cop:<filepath>} placeholders with the contents of the file at <filepath>.

        :param str value: The value to check for {cop:<filepath>} placeholders.
        :return: The value with the placeholders replaced with the file contents.
        """
        matches = re.findall(r'{cop:(.*?)}', value)
        for match in matches:
            file_path = os.path.expanduser(match)
            if os.path.isfile(file_path):
                with open(file_path, "r") as file:
                    file_content = file.read()
                value = value.replace(f'{{cop:{match}}}', file_content)
            else:
                raise FileNotFoundError(f"Could not find the file specified in the 'cop' placeholder: {file_path}")
        return value
