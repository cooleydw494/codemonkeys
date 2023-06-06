import os
from typing import Union, Any, List

from pack.modules.internal.theme.theme_functions import input_t, print_t


# Interactive validations for the terminal
def is_valid_path():
    while True:
        path = input_t("Please enter the path: ", "(absolute path or you can use ~ on Mac/Linux)")
        absolute_path = os.path.expanduser(path)
        if os.path.exists(absolute_path):
            return absolute_path
        else:
            print_t("Invalid path. Please try again.", 'error')


def is_valid_model():
    while True:
        model = int(input_t("Please enter the model: ", "(choose 3 (gpt-3.5-turbo) or 4 (gpt-4))"))
        if model in [3, 4]:
            return model
        else:
            print_t("Invalid model. Please try again.", 'error')


def is_valid_temp():
    while True:
        temp = float(input_t("Please enter the temperature: ", "(a value between 0 and 1)"))
        if 0 <= temp <= 1:
            return temp
        else:
            print_t("Invalid temperature. Please try again.", 'error')


def validate_path(key, path: str, is_file: bool = False) -> str:
    if not isinstance(path, str):
        raise ValueError(f"{key} must be a string, not {type(path).__name__}")

    absolute_path = os.path.expanduser(path)
    if not os.path.exists(absolute_path):
        raise FileNotFoundError(
            f"{key} value {absolute_path} does not exist. Make sure it is a valid absolute path.")

    if is_file and not os.path.isfile(absolute_path):
        raise FileNotFoundError(
            f"{key} value {absolute_path} does not point to a file.")

    if not is_file and not os.path.isdir(absolute_path):
        raise FileNotFoundError(
            f"{key} value {absolute_path} does not point to a directory.")
    return str(absolute_path)


def validate_range(key, value: Union[int, float], min_value: Any = None, max_value: Any = None) -> Union[int, float]:
    if not isinstance(value, (int, float)):
        raise ValueError(f"{key} must be an integer or a float, not {type(value).__name__}")

    if min_value is not None:
        if not isinstance(min_value, (int, float)):
            raise ValueError(f"Minimum value for {key} must be an integer or a float, not {type(min_value).__name__}")
        if value < min_value:
            raise ValueError(f"{key} value {value} is less than the minimum value {min_value}")

    if max_value is not None:
        if not isinstance(max_value, (int, float)):
            raise ValueError(f"Maximum value for {key} must be an integer or a float, not {type(max_value).__name__}")
        if value > max_value:
            raise ValueError(f"{key} value {value} is greater than the maximum value {max_value}")
    return value


def validate_bool(key, value: bool) -> bool:
    if str(value) in ['True', 'true', '1', 'Yes', 'yes', 'False', 'false', '0', 'No', 'no']:
        return str(value) in ['True', 'true', '1', 'Yes', 'yes']
    if not isinstance(value, bool):
        raise ValueError(f"{key} must be a boolean, not {type(value).__name__}")
    return value


def validate_int(key, value: int) -> int:
    if not isinstance(value, int):
        raise ValueError(f"{key} must be an integer, not {type(value).__name__}")
    return value


def validate_float(key, value: float) -> float:
    if not isinstance(value, float):
        raise ValueError(f"{key} must be a float, not {type(value).__name__}")
    return value


def validate_str(key, value: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{key} must be a string, not {type(value).__name__}")
    return value


def validate_list_str(key, value: List[str]) -> List[str]:
    if not isinstance(value, list):
        raise ValueError(f"{key} must be a list, not {type(value).__name__}")
    if not all(isinstance(item, str) for item in value):
        raise ValueError(f"{key} must be a list of strings")
    return value
