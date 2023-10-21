import json
import sys
import time
import traceback
from typing import List, Optional, Any

import openai
import tiktoken
from json_repair import repair_json
from tiktoken import Encoding

from codemonkeys.defs import TOKEN_UNCERTAINTY_BUFFER, nl2, nl
from codemonkeys.entities.func import Func
from codemonkeys.types import OStr, OInt, OFloat
from codemonkeys.utils.config.monkey_validations import validate_model, validate_temp
from codemonkeys.utils.imports.env import Env
from codemonkeys.utils.misc.handle_exception import handle_exception
from codemonkeys.utils.misc.log import Log
from codemonkeys.utils.monk.theme_functions import print_t, verbose_logs_enabled


class GPTClient:
    """A helper class to interact with GPT based models."""

    model: OStr = None
    hard_max_tokens: OInt = None
    max_tokens: OInt = None
    temperature: OFloat = None
    encoding: Optional[Encoding] = None

    def __init__(self, model_name: str, temperature: float = 1.0, max_tokens: int = 8000):
        """
        Initialize a GPTClient instance for a specific model.
        
        :param str model_name: The model's name.
        :param float temperature: The generation temperature. Defaults to 1.0.
        :param int max_tokens: Maximum tokens limit. Defaults to 8000.
        """

        env = Env.get()
        openai.api_key = env.OPENAI_API_KEY

        self.model = validate_model(model_name)
        self.hard_max_tokens = 16000  # TODO: use model-specific token limits
        self.max_tokens = min(max_tokens, self.hard_max_tokens) - TOKEN_UNCERTAINTY_BUFFER
        self.temperature = validate_temp(temperature)
        self.encoding = tiktoken.encoding_for_model(self.model)

    def generate(self, prompt: str, funcs: Optional[List[Func]] = None, enforce_func: OStr = None,
                 retry_delay: int = 60) -> Any:
        """
        Generate a GPT model response from a given prompt.

        :param enforce_func: The name of the function to enforce. Defaults to None.
        :param funcs: list of Func classes to use for function calling.
        :param str prompt: The text input for the model.
        :param int retry_delay: The delay in seconds to wait before rate limit retry. Defaults to 60.
        :return: The generated response.
        """

        try:
            if funcs:
                return self._generate_with_funcs(prompt, funcs, enforce_func)
            else:
                return self._generate(prompt)
        except openai.error.RateLimitError as e:
            print_t(f"Rate limit error, trying again in {retry_delay}s", 'warning')
            handle_exception(e, always_continue=True)
            time.sleep(retry_delay)
            return self.generate(prompt, funcs, enforce_func, retry_delay * 2)

        # Commented out because timeouts sometimes recur many times but only for specific prompts (best to skip)
        #
        # except openai.error.Timeout as e:
        #     print_t(f"Timeout error, trying again in {rate_limit_delay}s: {e}", 'warning')
        #     import time
        #     time.sleep(rate_limit_delay)
        #     return self.generate(_prompt, rate_limit_delay*2)

        except openai.error.OpenAIError as e:
            print_t(f"OpenAIError generating GPT response.", 'error')
            handle_exception(e, always_continue=True)
        except BaseException as e:
            print_t(f"GPT call failed.", 'error')
            handle_exception(e, always_continue=True)
        return None

    def _generate(self, prompt: str) -> str:
        """
        Generate a GPT response from a given prompt.
        :param prompt: The text input for the model.
        :return: The generated response.
        """

        max_tokens = self.max_tokens - self.count_tokens(prompt)
        print()
        print_t(f"Generating with {max_tokens}/{self.max_tokens} tokens remaining for response", 'loading')

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=max_tokens,
            temperature=self.temperature
        )

        return response.choices[0].message.content.strip()

    def _generate_with_funcs(self, prompt: str, funcs: Optional[List[Func]] = None, enforce_func: OStr = None) -> Any:
        """
        Generate a GPT model response from a given prompt, using the given Funcs (function calling)
        :param prompt: The text input for the model.
        :param funcs: list of Func classes to use for function calling.
        :param enforce_func: The name of the function to enforce. Defaults to None / "auto".
        :return: The result of the Func call (can be anything).
        """

        functions_data = [func.data() for func in funcs]
        function_call = {'name': enforce_func} if enforce_func else 'auto'

        max_tokens = self.max_tokens - self.count_tokens(prompt) - self.count_tokens(json.dumps(functions_data))
        print()
        print_t(f"Generating with {max_tokens}/{self.max_tokens} tokens remaining for response", 'loading')

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=max_tokens,
            temperature=self.temperature,
            functions=functions_data,
            function_call=function_call
        )

        fc_response = response['choices'][0]['message'].get('function_call')
        (name, args) = (fc_response['name'], fc_response['arguments'])
        available_funcs = {func.name: func for func in funcs}
        try:
            args = json.loads(args)
        except json.JSONDecodeError:
            print_t(f'sanitizing args due to decoding error', 'special', verbose=True)
            Log.warning(f'function call ({name}) produced invalid raw JSON args:{nl}{repr(args)}')
            args = json.loads(repair_json(args))
            Log.warning(f'function call ({name}) sanitized JSON args:{nl}{repr(args)}')

        func = available_funcs[name]

        return func.call(args)

    def tokenize(self, text: str) -> List[int]:
        """
        Tokenize a given text into a list of tokens.
        
        :param str text: The input text.
        :return: The list of tokens.
        """
        return self.encoding.encode(text)

    def count_tokens(self, text: str) -> int:
        """
        Count the number of tokens in a given text.

        :param str text: The input text.
        :return: The number of tokens in the text.
        """
        return len(self.tokenize(text))
