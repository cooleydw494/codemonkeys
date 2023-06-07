import os
import re
from typing import Union, List

from definitions import ROOT_PATH
from pack.modules.internal.theme.theme_functions import input_t, print_t

valid_values = {
    'temperature': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
    'model': [3, 4]
}


def get_user_config_value(key: str, validate_func, hint=""):
    while True:
        user_provided_value = input_t(key, hint)
        try:
            return validate_func(key, user_provided_value)
        except ValueError as e:
            print_t(str(e), 'error')


def validate_path(key, path: str) -> str:
    if path.startswith('ROOT_PATH/'):
        path = os.path.join(ROOT_PATH, path[10:])
    absolute_path = os.path.expanduser(path)
    if not os.path.exists(absolute_path):
        raise ValueError(f"{key} value {absolute_path} does not exist.")
    if not os.path.isfile(absolute_path) and not os.path.isdir(absolute_path):
        raise ValueError(f"{key} value {absolute_path} does not point to a correct path.")
    return str(absolute_path)


def validate_monkey_name(key: str = 'Monkey Name', monkey_name: str = None) -> str:
    if not monkey_name.replace('-', '').isalpha():
        raise ValueError(f"Monkey name must contain only letters and hyphens")
    return monkey_name


def validate_bool(key, value: bool) -> bool:
    if isinstance(value, bool):
        return value
    if str(value).lower() in ['true', '1', 'yes']:
        return True
    if str(value).lower() in ['false', '0', 'no']:
        return False
    raise ValueError(f"{key} must be a boolean, not {type(value).__name__}")


def validate_type(key, value, expected_type: type):
    try:
        value = expected_type(value)
    except ValueError:
        raise ValueError(f"{key} must be a {expected_type.__name__}")

    valid_type_values = valid_values.get(key)
    if valid_type_values and value not in valid_type_values:
        raise ValueError(f"{key} value {value} is not in valid values {valid_type_values}")
    return value


def validate_int(key, value):
    if re.search(r'\bmodel\b', str(key).lower()):
        return validate_type('model', value, int)
    return validate_type(key, value, int)


def validate_float(key, value):
    if re.search(r'\btemperature\b', str(key).lower()):
        return validate_type('temperature', value, float)
    return validate_type(key, value, float)


def validate_str(key, value):
    string_value = validate_type(key, value, str)
    if re.search(r'\bpath\b', str(key).lower()):
        return validate_path(key, value)
    return string_value


def validate_list_str(key, value: List[str]) -> List[str]:
    value = validate_type(key, value, list)
    if not all(isinstance(item, str) for item in value):
        raise ValueError(f"{key} must be a list of strings")
    return value
