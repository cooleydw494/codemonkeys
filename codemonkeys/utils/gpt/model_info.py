import json
import os
from typing import Optional

import openai

from codemonkeys.config.imports.env import Env
from codemonkeys.defs import TEMP_PATH
from codemonkeys.utils.monk.theme_functions import print_t


def get_gpt_model_info() -> Optional[dict]:
    """
    Retrieves cached info on GPT models.

    :return: A dictionary containing GPT model information, or None if the information could not be retrieved.
    :rtype: Optional[dict]
    """
    try:
        with open(os.path.join(TEMP_PATH, 'model_info_cache.json'), 'r') as f:
            return json.load(f)

    except Exception as e:
        print_t(f"An error occurred reading cached gpt model info: {e}", 'warning')
        return None


def get_gpt_model_names() -> Optional[list[str]]:
    """
    Retrieves the names of all GPT models from the cached model info.

    :return: A list of model names, or None if the model info could not be retrieved.
    :rtype: Optional[list[str]]
    """
    model_info = get_gpt_model_info()
    if model_info is None:
        return None
    return [model_name for model_name in model_info.keys()]


def update_gpt_model_cache() -> None:
    """
    Updates the GPT model info cache by querying the openai API.

    :return: None
    """
    model_info = _query_model_info()

    if model_info is not None:
        try:
            with open(os.path.join(TEMP_PATH, 'model_info_cache.json'), 'w') as f:
                json.dump(model_info, f)

        except Exception as e:
            print(f"An error occurred updating gpt model info cache: {e}")


def _query_model_info() -> Optional[dict]:
    """
    Queries the OpenAI API for a list of models.

    :return: A dictionary mapping model ids to models, or None if the API call failed.
    :rtype: Optional[dict]
    """
    try:
        env = Env.get()
        openai.api_key = env.OPENAI_API_KEY

        if openai.api_key is None:
            raise Exception("OPENAI_API_KEY not set in environment variables")

        model_list = openai.Model.list()

        # We're creating a new dictionary where the key is the model's ID and the value is the model's data
        model_info = {model.id: model for model in model_list.data}

        return model_info

    except Exception as e:
        print(f"An error occurred while retrieving the model information: {e}")
        return None
