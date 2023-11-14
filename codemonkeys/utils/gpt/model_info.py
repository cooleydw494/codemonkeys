import json
import os
from typing import Optional

import openai

from codemonkeys.defs import TEMP_PATH
from codemonkeys.utils.imports.env import Env
from codemonkeys.utils.misc.handle_exception import handle_exception
from codemonkeys.utils.monk.theme_functions import print_t


def get_gpt_model_info() -> Optional[dict]:
    """
    Retrieves cached info on GPT models.

    Attempts to read a JSON file containing cached GPT model information.
    It ensures that this data is readily available without querying the openai API repeatedly.

    :return: Dictionary containing GPT model information if successful, None otherwise.
    :rtype: Optional[dict]
    """
    try:
        with open(os.path.join(TEMP_PATH, 'model_info_cache.json'), 'r') as f:
            return json.load(f)

    except Exception as e:
        print_t("An error occurred reading cached gpt model info.", 'warning')
        handle_exception(e, always_continue=True)
        return None


def get_gpt_model_names() -> Optional[list[str]]:
    """
    Retrieves the names of all GPT models from the cached model info.

    :return: List of model names if model info is available, None otherwise.
    :rtype: Optional[list[str]]
    """
    model_info = get_gpt_model_info()
    if model_info is None:
        return None
    return [model_name for model_name in model_info.keys()]


def update_gpt_model_cache() -> None:
    """
    Updates the GPT model info cache.

    Contacts the OpenAI API to fetch the latest list of models and updates the
    model info cache file.

    :return: None
    """

    try:
        model_info = _query_model_info()
        if model_info is not None:
            with open(os.path.join(TEMP_PATH, 'model_info_cache.json'), 'w') as f:
                json.dump(model_info, f)

    except Exception as e:
        print_t("An error occurred updating GPT model info cache.", 'error')
        handle_exception(e)


def _query_model_info() -> Optional[dict]:
    """
    Queries the OpenAI API for the list of models.

    Private method that makes an API call to OpenAI to fetch a list of current models.
    The response is then shaped into a dictionary mapping model IDs to their respective details.

    :return: A dictionary mapping model ids to their details if successful, None otherwise.
    :rtype: Optional[dict]

    :raises Exception: If the OPENAI_API_KEY is not set in the environment variables.
    """

    env = Env.get()
    openai.api_key = env.OPENAI_API_KEY

    if openai.api_key is None:
        raise Exception("OPENAI_API_KEY not set in environment variables")

    model_list = openai.Model.list()

    # We're creating a new dictionary where the key is the model's ID and the value is the model's data
    model_info = {model.id: model for model in model_list.data}

    return model_info
