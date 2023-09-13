import os
import re
from typing import List, Union, Any

from codemonkeys.defs import ROOT_PATH
from codemonkeys.utils.gpt.model_info import get_gpt_model_names


def get_valid_values(key: str) -> List[Any]:
    """
    Gets the valid values for the given key.

    :param str key: The config key to check.
    :return: List of valid values for the given key.
    """
    try:
        gpt_model_names = get_gpt_model_names()
    except Exception as e:
        gpt_model_names = ['gpt-3.5-turbo', 'gpt-4']

    valid_values = {
        'temp': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
        'model': gpt_model_names,
    }
    if key in valid_values:
        return valid_values[key]
    return []


def _has_word(key: str, word: str) -> bool:
    """
    Checks if a word is present in the given string (using word boundaries).

    :param str key: The config key to check.
    :param str word: The word to search for.
    :return: True if key contains word, else False.
    """
    return re.search(rf'\b{word}\b', str(key).lower().replace('_', ' ')) is not None


def is_path_key(key: str) -> bool:
    """
    Checks if the given key is a PATH key.

    :param str key: The config key to check.
    :return True if key is a PATH key, else False.
    """
    return _has_word(key, 'path')


def _is_model_key(key: str) -> bool:
    """
    Checks if the given key is a MODEL key.

    :param str key: The config key to check.
    :return True if key is a MODEL key, else False.
    """
    return _has_word(key, 'model')


def _is_temp_key(key: str) -> bool:
    """
    Checks if the given key is a TEMP key.

    :param str key: The config key to check.
    :return True if key is a TEMP key, else False.
    """
    return _has_word(key, 'temp')


def is_prompt_key(key: str) -> bool:
    """
    Checks if the given key is a PROMPT key.

    :param str key: The config key to check.
    :return True if key is a PROMPT key, else False.
    """
    return _has_word(key, 'prompt')


def validate_path(key: str, path: str | None) -> Union[str, None]:
    """
    Validate PATH by checking its existence and whether it is file or directory.

    :param str key: The config key to validate.
    :param str path: The PATH value to validate.
    :return: Validated PATH str or None.
    """
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


def validate_bool(key: str, value: bool) -> Union[bool, None]:
    """
    Validate a boolean value. Accepts 'true', 'false', '1', '0', 'yes', and 'no'. Case insensitive.

    :param str key: The config key to validate.
    :param bool value: Value to be validated.
    :return: True, False, or None.
    """
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if str(value).lower() in ['true', '1', 'yes']:
        return True
    if str(value).lower() in ['false', '0', 'no']:
        return False
    raise TypeError(f"{key} must be a boolean, not {type(value).__name__}")


def validate_type(key: str, value: Any, expected_type: type) -> Any:
    """
    Validate the type of a value, optionally checking against a list of valid values.

    :param str key: The config key to validate.
    :param Any value: The value to validate.
    :param type expected_type: The expected type of the value.
    :return: Validated value or None.
    """
    if value is None:
        return None
    try:
        value = expected_type(value)
    except TypeError:
        raise TypeError(f"{key} must be a {expected_type.__name__}")

    valid_type_values = get_valid_values(str(expected_type))
    if valid_type_values and value not in valid_type_values:
        raise TypeError(f"{key} value {value} is not in valid values {valid_type_values}")
    return value


def validate_int(key: str, value: Any) -> int | None:
    """
    Validate an integer value.

    :param str key: The config key to validate.
    :param Any value: Value to be validated.
    :return: Validated int or None.
    """
    if _is_model_key(key):
        return validate_type('model', value, int)
    return validate_type(key, value, int)


def validate_float(key: str, value: Any) -> float | None:
    """
    Validate a float value.

    :param str key: The config key to validate.
    :param Any value: Value to be validated.
    :return: Validated float or None.
    """
    if _is_temp_key(key):
        return validate_type('temp', value, float)
    return validate_type(key, value, float)


def validate_str(key: str, value: Any) -> str | None:
    """
    Validate a string value.

    :param str key: Key associated to the configured value.
    :param Any value: Value to be validated.
    :return: Validated string or None.
    """
    if type(value) in [int, float, bool]:
        raise TypeError(f"{key} must be a string, not {type(value).__name__}")
    string_value = validate_type(key, value, str)
    if string_value == str and is_path_key(key):
        return validate_path(key, value)
    return string_value


def validate_list_str(key: str, value: List[str]) -> List[str] | None:
    """
    Validate a List of strings

    :param str key: The config key to validate.
    :param List[str] value: The List of string values to validate.
    :return: Validated List or None.
    """
    value = validate_type(key, value, list)
    if not all(isinstance(item, str) for item in value):
        raise TypeError(f"{key} must be a list of strings")
    return value
