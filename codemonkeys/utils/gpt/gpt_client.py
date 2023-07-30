from typing import List

import openai
import tiktoken

from codemonkeys.defs import TOKEN_UNCERTAINTY_BUFFER
from codemonkeys.utils.gpt.model_info import get_gpt_model_names
from codemonkeys.utils.monk.theme_functions import print_t

try:
    from config.framework.env_class import Env
except ImportError:
    print_t('Could not import user Env class from config.framework.env_class. Using default Env class.', 'warning')
    from codemonkeys.config.env_class import Env

# Set up OpenAI client with API key
env = Env.get()
openai.api_key = env.OPENAI_API_KEY


def check_api_key():
    """Check if OpenAI API key has been properly set, else raise an Exception."""
    if not openai.api_key:
        raise Exception("OPENAI_API_KEY not set in `.env` file.")


class GPTClient:
    """A helper class to interact with GPT based models."""

    _model_names = get_gpt_model_names()

    def __init__(self, model_name: str, temperature: float = 1.0, max_tokens: int = 8000):
        """
        Initialize a GPTClient instance for a specific model.
        
        :param str model_name: The model's name.
        :param float temperature: The generation temperature. Defaults to 1.0.
        :param int max_tokens: Maximum tokens limit. Defaults to 8000.
        """
        if model_name not in self._model_names:
            raise ValueError(f"Invalid GPT model name: {model_name}. Try `monk gpt-models-info --update`.")

        self.model = model_name
        self.hard_max_tokens = 16000  # TODO: use model-specific token limits
        self.max_tokens = min(max_tokens, self.hard_max_tokens)
        self.temperature = temperature
        self.encoding = tiktoken.encoding_for_model(self.model)

    def generate(self, prompt: str, temperature: float = None, rate_limit_delay: int = 60) -> str | None:
        """
        Generate a GPT model response from a given prompt.
        
        :param str prompt: The text input for the model.
        :param float temperature: The generation temperature. Defaults to None.
        :param int rate_limit_delay: The delay in seconds to wait before rate limit retry. Defaults to 60.
        :return: The generated response.
        """
        check_api_key()
        temperature = temperature or self.temperature

        max_tokens = self.max_tokens - self.count_tokens(prompt) - TOKEN_UNCERTAINTY_BUFFER

        print_t(f"Generating with {max_tokens}/{self.max_tokens} tokens remaining for response", 'special')

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{'role': 'user', 'content': prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
        except openai.error.RateLimitError as e:
            print_t(f"Rate limit error, trying again in {rate_limit_delay}s: {e}", 'warning')
            import time
            time.sleep(rate_limit_delay)
            return self.generate(prompt, temperature, rate_limit_delay*2)
        # except openai.error.Timeout as e:
        #     print_t(f"Timeout error, trying again in {rate_limit_delay}s: {e}", 'warning')
        #     import time
        #     time.sleep(rate_limit_delay)
        #     return self.generate(prompt, temperature, rate_limit_delay*2)
        except openai.error.OpenAIError as e:
            print_t(f"OpenAI error: {e}", 'error')
            return None

        return response.choices[0].message.content.strip()

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
