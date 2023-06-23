from typing import List

import openai
import tiktoken

from defs import import_env_class
from defs import TOKEN_UNCERTAINTY_BUFFER
from codemonkeys.utils.monk.theme_functions import print_t

ENV = import_env_class()

# Set up OpenAI client with API key
ENV = ENV()
openai.api_key = ENV.OPENAI_API_KEY


def check_api_key():
    if not openai.api_key:
        raise Exception("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")


class GPTClient:
    model_map = {
        '3': ("gpt-3.5-turbo", 4000),
        '4': ("gpt-4", 8000),
    }

    def __init__(self, model_name, temperature=1.0, max_tokens=1000000):
        model_info = self.model_map.get(str(model_name))
        if model_info is None:
            raise ValueError(f"Unsupported GPT version: {model_name}")

        self.model, self.hard_max_tokens = model_info
        self.max_tokens = min(max_tokens, self.hard_max_tokens)
        self.temperature = temperature
        self.encoding = tiktoken.encoding_for_model(self.model)

    def generate(self, prompt, temperature=None):
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

    def detokenize(self, tokens) -> str:
        if not tokens:
            return ""
        elif isinstance(tokens, int):
            return self.encoding.decode_single_token_bytes(tokens).decode('utf-8')
        else:
            return self.encoding.decode(tokens)

    def count_tokens(self, text: str) -> int:
        return len(self.tokenize(text))

    def shorten_to_n_tokens(self, text: str, n: int, end=False) -> str:
        tokens = self.tokenize(text)
        if len(tokens) <= n:
            return text
        return self.detokenize(tokens[:n] if not end else tokens[-n:])

    def split_into_chunks(self, text: str, chunk_size: int) -> List[str]:
        tokens = self.tokenize(text)
        return [self.detokenize(tokens[i:i + chunk_size]) for i in range(0, len(tokens), chunk_size)]

    def num_tokens_from_messages(self, messages: List[dict]) -> int:
        tokens_per_message = 4 if self.model == "gpt-3.5-turbo" else 3
        tokens_per_name = -1 if self.model == "gpt-3.5-turbo" else 1

        return sum(tokens_per_message + sum(self.count_tokens(val) for key, val in msg.items()) + (
            tokens_per_name if 'name' in msg else 0)
                   for msg in messages) + 3
