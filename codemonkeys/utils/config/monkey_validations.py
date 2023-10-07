import os
import re
from typing import Optional

from codemonkeys.types import OStr, OFloat
from codemonkeys.utils.gpt.model_info import get_gpt_model_names, update_gpt_model_cache


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


def is_model_key(key: str) -> bool:
    """
    Checks if the given key is a MODEL key.

    :param str key: The config key to check.
    :return True if key is a MODEL key, else False.
    """
    return _has_word(key, 'model')


def is_temp_key(key: str) -> bool:
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


def validate_path(path: OStr, allow_none: bool = False) -> OStr:
    """
    Validate PATH by checking its existence and whether it is file or directory.

    :param allow_none: Whether to allow None as a valid value.
    :param str path: The PATH value to validate.
    :return: Validated PATH str or None.
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
    Validates that the given model name is a valid GPT model name.
    Checks against local cached models associated with the users' OpenAI API key.
    If the model name is not found, attempts to update the cache and check again before throwing an error.

    :param allow_none: Whether to allow None as a valid value.
    :param model_name: The model name to validate.
    :return: The validated model name.
    """
    if model_name is None:
        if allow_none:
            return None
        raise TypeError("Model name value cannot be None.")
    valid_models = get_gpt_model_names()
    if model_name not in valid_models:
        try:
            update_gpt_model_cache()
            valid_models = get_gpt_model_names()
            if model_name not in valid_models:
                raise ValueError(f"Invalid GPT model name: {model_name}.")
        except Exception:
            raise ValueError(f"Invalid GPT model name: {model_name}.")
    return model_name


def validate_temp(value: OFloat, allow_none: bool = False) -> OFloat:
    """
    Validates that the given value is a valid temperature value.

    :param allow_none: Whether to allow None as a valid value.
    :param value: The temperature value to validate.
    :return: The validated temperature value.
    """
    if value is None and allow_none:
        return None
    if value not in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
        raise ValueError(f"Invalid temperature value: {value}.")
    return value
