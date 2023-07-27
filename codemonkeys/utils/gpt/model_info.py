import json

import openai

from codemonkeys.defs import TEMP_PATH
from codemonkeys.utils.monk.theme_functions import print_t

try:
    from config.framework.env_class import Env
except ImportError:
    print_t('Could not import user Env class from config.framework.env_class. Using default Env class.', 'warning')
    from codemonkeys.config.env_class import Env

_model_cache_file_path = TEMP_PATH + '/model_info_cache.json'


def get_gpt_model_info() -> dict | None:
    try:
        with open(_model_cache_file_path, 'r') as f:
            return json.load(f)

    except Exception as e:
        print_t(f"An error occurred reading cached gpt model info: {e}", 'warning')
        return None


def get_gpt_model_names() -> list[str] | None:
    model_info = get_gpt_model_info()
    if model_info is None:
        return None
    return [model_name for model_name in model_info.keys()]


def update_gpt_model_cache() -> None:
    model_info = _query_model_info()

    if model_info is not None:
        try:
            with open(_model_cache_file_path, 'w') as f:
                json.dump(model_info, f)

        except Exception as e:
            print(f"An error occurred updating gpt model info cache: {e}")


def _query_model_info() -> dict | None:
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
