from typing import List

import openai
import tiktoken

from codemonkeys.utils.gpt.model_info import get_gpt_model_names
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.defs import TOKEN_UNCERTAINTY_BUFFER

try:
    from config.framework.env_class import Env
except ImportError:
    print_t('Could not import user Env class from config.framework.env_class. Using default Env class.', 'warning')
    from codemonkeys.config.env_class import Env

# Set up OpenAI client with API key
env = Env.get()
openai.api_key = env.OPENAI_API_KEY


def check_api_key():
    if not openai.api_key:
        raise Exception("OPENAI_API_KEY not set in `.env` file.")


class GPTClient:

    _model_names = get_gpt_model_names()

    def __init__(self, model_name: str, temperature: float = 1.0, max_tokens: int = 8000):
        if model_name not in self._model_names:
            raise ValueError(f"Invalid GPT model name: {model_name}. Try `monk gpt-models-info --update`.")

        self.model = model_name
        self.hard_max_tokens = 16000  # TODO: use model-specific token limits
        self.max_tokens = min(max_tokens, self.hard_max_tokens)
        self.temperature = temperature
        self.encoding = tiktoken.encoding_for_model(self.model)

    def generate(self, prompt: str, temperature: float = None) -> str:
        check_api_key()
        temperature = temperature or self.temperature

        max_tokens = self.max_tokens - self.count_tokens(prompt) - TOKEN_UNCERTAINTY_BUFFER

        print_t(f"Generating with {max_tokens}/{self.max_tokens} tokens remaining for response", 'special')

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )

        return response.choices[0].message.content.strip()

    def tokenize(self, text: str) -> List[int]:
        return self.encoding.encode(text)

    def detokenize(self, tokens: List[int]) -> str:
        if not tokens:
            return ""
        elif isinstance(tokens, int):
            return self.encoding.decode_single_token_bytes(tokens).decode('utf-8')
        else:
            return self.encoding.decode(tokens)

    def count_tokens(self, text: str) -> int:
        return len(self.tokenize(text))

    def shorten_to_n_tokens(self, text: str, n: int, end: bool = False) -> str:
        tokens = self.tokenize(text)
        if len(tokens) <= n:
            return text
        return self.detokenize(tokens[:n] if not end else tokens[-n:])

    def split_into_chunks(self, text: str, chunk_size: int) -> List[str]:
        tokens = self.tokenize(text)
        return [self.detokenize(tokens[i:i + chunk_size]) for i in range(0, len(tokens), chunk_size)]
