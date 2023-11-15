import os
import re

from codemonkeys.types import OStr, OFloat
from codemonkeys.utils.gpt.model_info import get_gpt_model_names, update_gpt_model_cache


def _has_word(key: str, word: str) -> bool:
    """
    Checks if a word is present in the given string (using word boundaries).

    :param key: The string to be checked.
    :type key: str
    :param word: The word to be searched for within the string.
    :type word: str
    :return: True if the word is found in the string, False otherwise.
    :rtype: bool
    """
    return re.search(rf'\b{word}\b', str(key).lower().replace('_', ' ')) is not None


def is_path_key(key: str) -> bool:
    """
    Determines whether the given config key is related to a PATH.

    :param key: The config key to be checked.
    :type key: str
    :return: True if key is related to a PATH, False otherwise.
    :rtype: bool
    """
    return _has_word(key, 'path')


def is_model_key(key: str) -> bool:
    """
    Determines whether the given config key is related to a MODEL.

    :param key: The config key to be checked.
    :type key: str
    :return: True if key is related to a MODEL, False otherwise.
    :rtype: bool
    """
    return _has_word(key, 'model')


def is_temp_key(key: str) -> bool:
    """
    Determines whether the given config key is related to a TEMP(temperature setting).

    :param key: The config key to be checked.
    :type key: str
    :return: True if key is related to a TEMP, False otherwise.
    :rtype: bool
    """
    return _has_word(key, 'temp')


def is_prompt_key(key: str) -> bool:
    """
    Determines whether the given config key is related to a PROMPT.

    :param key: The config key to be checked.
    :type key: str
    :return: True if key is related to a PROMPT, False otherwise.
    :rtype: bool
    """
    return _has_word(key, 'prompt')


def validate_path(path: OStr, allow_none: bool = False) -> OStr:
    """
    Validates a PATH by checking its existence and ensuring it is a file or a directory.

    Given a path, this function checks if the path exists and whether it is a valid
    file or directory path. Optional parameter allow_none determines whether
    a None value is acceptable.

    :param path: The path to validate.
    :type path: OStr
    :param allow_none: Allows the value None as a valid PATH. Defaults to False.
    :type allow_none: bool
    :return: The validated path.
    :rtype: OStr
    :raises TypeError: If path is None when allow_none is False, or if the path does not exist or is not a valid file or directory.
    """
    if path is None:
        if allow_none:
            return None
        raise TypeError("Path value cannot be None.")
    absolute_path = os.path.expanduser(path)
    if not os.path.exists(absolute_path):
        raise TypeError(f"Path value {absolute_path} does not exist.")
    if not os.path.isfile(absolute_path) and not os.path.isdir(absolute_path):
        raise TypeError(f"Path value {absolute_path} is not a valid file or directory.")
    return str(absolute_path)


def validate_model(model_name: OStr, allow_none: bool = False) -> OStr:
    """
    Validates a GPT model name against a list of known model names.

    Checks if the provided model name is in the list of known GPT model names. Optional
    parameter allow_none determines whether a None value is acceptable.

    :param model_name: The model name to validate.
    :type model_name: OStr
    :param allow_none: Allows the value None as a valid model name. Defaults to False.
    :type allow_none: bool
    :return: The validated model name.
    :rtype: OStr
    :raises TypeError: If model_name is None when allow_none is False.
    :raises ValueError: If the model_name is not a recognized GPT model.
    """
    if model_name is None:
        if allow_none:
            return None
        raise TypeError("Model name value cannot be None.")
    valid_models = get_gpt_model_names()
    if model_name not in valid_models:
        update_gpt_model_cache()
        valid_models = get_gpt_model_names()
        if model_name not in valid_models:
            raise ValueError(f"Invalid GPT model name: {model_name}.")
    return model_name


def validate_temp(value: OFloat, allow_none: bool = False) -> OFloat:
    """
    Validates that a given value falls within the expected range of temperature settings.

    This function ensures that the provided temperature setting is within the valid
    range GPT can accept. The optional parameter allow_none indicates if a None value
    is permissible.

    :param value: The temperature setting to validate.
    :type value: OFloat
    :param allow_none: Allows the value None as a valid temperature setting. Defaults to False.
    :type allow_none: bool
    :return: The validated temperature setting.
    :rtype: OFloat
    :raises ValueError: If the value is not within the permitted temperature range.
    """
    if value is None and allow_none:
        return None
    if value not in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
        raise ValueError(f"Invalid temperature value: {value}.")
    return value
