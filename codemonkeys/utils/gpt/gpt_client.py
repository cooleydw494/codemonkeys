import json
from typing import List, Optional, Any

import openai
import tiktoken
from tiktoken import Encoding

from codemonkeys.utils.imports.env import Env
from codemonkeys.defs import TOKEN_UNCERTAINTY_BUFFER
from codemonkeys.entities.func import Func
from codemonkeys.types import OStr, OInt, OFloat
from codemonkeys.utils.config.monkey_validations import validate_model, validate_temp
from codemonkeys.utils.monk.theme_functions import print_t


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
        self.max_tokens = min(max_tokens, self.hard_max_tokens)
        self.temperature = validate_temp(temperature)
        self.encoding = tiktoken.encoding_for_model(self.model)

    def generate(self, prompt: str, funcs: Optional[List[Func]] = None, enforce_func: OStr = None, retry_delay: int = 60) -> Any:
        """
        Generate a GPT model response from a given prompt.
        
        :param enforce_func: The name of the function to enforce. Defaults to None.
        :param funcs: list of Func classes to use for function calling.
        :param str prompt: The text input for the model.
        :param int retry_delay: The delay in seconds to wait before rate limit retry. Defaults to 60.
        :return: The generated response.
        """
        max_tokens = self.max_tokens - self.count_tokens(prompt) - TOKEN_UNCERTAINTY_BUFFER

        try:

            if funcs is not None and len(funcs) > 0:
                functions_data = [func.data() for func in funcs]
                max_tokens -= self.count_tokens(json.dumps([func.data() for func in funcs]))
                print_t(f"Generating with {max_tokens}/{self.max_tokens} tokens remaining for response", 'special')
                function_call = {'name': enforce_func} if enforce_func is not None else 'auto'

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
                options = {func.name: func for func in funcs}
                return options[name].call(json.loads(args))

            else:
                print_t(f"Generating with {max_tokens}/{self.max_tokens} tokens remaining for response", 'special')
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[{'role': 'user', 'content': prompt}],
                    max_tokens=max_tokens,
                    temperature=self.temperature
                )

                return response.choices[0].message.content.strip()

        except openai.error.RateLimitError as e:
            print_t(f"Rate limit error, trying again in {retry_delay}s: {e}", 'warning')
            import time
            time.sleep(retry_delay)
            return self.generate(prompt, funcs, retry_delay * 2)

        # Commented out because timeouts sometimes recur many times but only for specific prompts (best to skip)
        #
        # except openai.error.Timeout as e:
        #     print_t(f"Timeout error, trying again in {rate_limit_delay}s: {e}", 'warning')
        #     import time
        #     time.sleep(rate_limit_delay)
        #     return self.generate(_prompt, rate_limit_delay*2)

        except openai.error.OpenAIError as e:
            print_t(f"OpenAI error:", 'error')
            import traceback
            traceback.print_exc()
        except Exception as e:
            print_t(f"Unknown error:", 'error')
            import traceback
            traceback.print_exc()
        return None

    def tokenize(self, text: str) -> List[int]:
        """
        Tokenize a given text into a list of tokens.
        
        :param str text: The input text.
        :return: The list of tokens.
        """
        return self.encoding.encode(text)

    def detokenize(self, tokens: List[int]) -> str:
        """
        Detokenize a given list of tokens back into text.
        
        :param list tokens: The list of tokens.
        :return: The decoded text.
        """
        if not tokens:
            return ""
        elif isinstance(tokens, int):
            return self.encoding.decode_single_token_bytes(tokens).decode('utf-8')
        else:
            return self.encoding.decode(tokens)

    def count_tokens(self, text: str) -> int:
        """
        Count the number of tokens in a given text.

        :param str text: The input text.
        :return: The number of tokens in the text.
        """
        return len(self.tokenize(text))

    def shorten_to_n_tokens(self, text: str, n: int, end: bool = False) -> str:
        """
        Shortens a given text to n number of tokens.

        :param str text: The input text.
        :param int n: The required number of tokens.
        :param bool end: Flag indicating whether to keep the ending tokens or the beginning ones. Defaults to False.
        :return: The shortened text.
        """
        tokens = self.tokenize(text)
        if len(tokens) <= n:
            return text
        return self.detokenize(tokens[:n] if not end else tokens[-n:])

    def split_into_chunks(self, text: str, chunk_size: int) -> List[str]:
        """
        Split a given text into chunks where each chunk has chunk_size number of tokens.

        :param str text: The input text.
        :param int chunk_size: The size of each chunk in tokens.
        :return: The list of text chunks.
        """
        tokens = self.tokenize(text)
        return [self.detokenize(tokens[i:i + chunk_size]) for i in range(0, len(tokens), chunk_size)]
