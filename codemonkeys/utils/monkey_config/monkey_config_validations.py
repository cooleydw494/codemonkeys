import os
import re
from typing import List, Union

from codemonkeys.utils.gpt.model_info import get_gpt_model_names
from codemonkeys.utils.monk.theme_functions import input_t, print_t
from codemonkeys.defs import ROOT_PATH

try:
    gpt_model_names = get_gpt_model_names()
except Exception as e:
    gpt_model_names = ['gpt-3.5-turbo', 'gpt-4']

valid_values = {
    'temp': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
    'model': gpt_model_names,
}


def _has_word(key: str, word: str) -> bool:
    return re.search(rf'\b{word}\b', str(key).lower().replace('_', ' ')) is not None


def _is_path_key(key: str) -> bool:
    return _has_word(key, 'path')


def _is_model_key(key: str) -> bool:
    return _has_word(key, 'model')


def _is_temp_key(key: str) -> bool:
    return _has_word(key, 'temp')


def is_prompt_key(key: str) -> bool:
    return _has_word(key, 'prompt')


def get_user_config_value(key: str, validate_func, hint="") -> Union[str, None]:
    while True:
        user_provided_value = input_t(key, hint)
        # if user_value is an empty string, return None
        if user_provided_value == "":
            return None
        # if user_value is "null", return None
        elif user_provided_value.lower() == "null":
            return 'null'
        try:
            return validate_func(key, user_provided_value)
        except (TypeError, ValueError) as exception:
            print_t(str(exception), 'error')


def validate_path(key: str, path: str) -> Union[str, None]:
    if path is None:
        return None
    if path.startswith('ROOT_PATH/'):
        path = os.path.join(ROOT_PATH, path[10:])
    absolute_path = os.path.expanduser(path)
    if not os.path.exists(absolute_path):
        raise TypeError(f"{key} value {absolute_path} does not exist.")
    if not os.path.isfile(absolute_path) and not os.path.isdir(absolute_path):
        raise TypeError(f"{key} value {absolute_path} does not point to a correct path.")
    return str(absolute_path)


def validate_monkey_name(monkey_name: str = None) -> str:
    if not monkey_name.replace('-', '').isalpha():
        raise TypeError(f"Monkey name must contain only letters and hyphens")
    return monkey_name


def validate_bool(key: str, value: bool) -> Union[bool, None]:
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if str(value).lower() in ['true', '1', 'yes']:
        return True
    if str(value).lower() in ['false', '0', 'no']:
        return False
    raise TypeError(f"{key} must be a boolean, not {type(value).__name__}")


def validate_type(key: str, value, expected_type: type):
    if value is None:
        return None
    try:
        value = expected_type(value)
    except TypeError:
        raise TypeError(f"{key} must be a {expected_type.__name__}")

    valid_type_values = valid_values.get(key)
    if valid_type_values and value not in valid_type_values:
        raise TypeError(f"{key} value {value} is not in valid values {valid_type_values}")
    return value


def validate_int(key: str, value: str) -> int:
    if _is_model_key(key):
        return validate_type('model', value, int)
    return validate_type(key, value, int)


def validate_float(key: str, value: str) -> float:
    if _is_temp_key(key):
        return validate_type('temp', value, float)
    return validate_type(key, value, float)


def validate_str(key: str, value: str) -> str:
    if type(value) in [int, float, bool]:
        raise TypeError(f"{key} must be a string, not {type(value).__name__}")
    string_value = validate_type(key, value, str)
    if string_value == str and _is_path_key(key):
        return validate_path(key, value)
    return string_value


def validate_list_str(key: str, value: List[str]) -> Union[List[str], None]:
    value = validate_type(key, value, list)
    if not all(isinstance(item, str) for item in value):
        raise TypeError(f"{key} must be a list of strings")
    return value
