from typing import List

import tiktoken


class TokenCounter:
    def __init__(self, model: str):
        supported_model_args = ['3', '4']
        model_names = {
            '3': 'gpt-3.5-turbo',
            '4': 'gpt-4'
        }

        if model not in supported_model_args:
            raise ValueError(f"Unsupported model '{model}'. Supported models are {supported_model_args}.")

        self.model = model_names[model]
        self.encoding = tiktoken.encoding_for_model(model)

    def tokenize(self, text: str) -> List[int]:
        return self.encoding.encode(text)

    def detokenize(self, token_list: List[int]) -> str:
        if len(token_list) == 0:
            return ""
        elif len(token_list) == 1:
            raise ValueError(f"You're using detokenize() on a single token. Please use detokenize_single().")
        else:
            return self.encoding.decode(token_list)

    def detokenize_single(self, token: int) -> bytes:
        return self.encoding.decode_single_token_bytes(token)

    def count_tokens(self, text: str) -> int:
        token_list = self.tokenize(text)
        return len(token_list)

    def shorten_to_n_tokens(self, text: str, n: int) -> str:
        token_list = self.tokenize(text)
        if len(token_list) > n:
            token_list = token_list[:n]
            text = self.detokenize(token_list)
        return text

    def split_into_chunks(self, text: str, chunk_size: int) -> List[str]:
        token_list = self.tokenize(text)
        chunks = [self.detokenize(token_list[i:i + chunk_size]) for i in range(0, len(token_list), chunk_size)]
        return chunks

    def num_tokens_from_messages(self, messages: List[dict]) -> int:
        if self.model == "gpt-3.5-turbo":
            tokens_per_message = 4
            tokens_per_name = -1
        elif self.model == "gpt-4":
            tokens_per_message = 3
            tokens_per_name = 1
        else:
            raise NotImplementedError(
                f"num_tokens_from_messages() is not implemented for model {self.model}. See https://github.com/openai"
                f"/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.")

        num_tokens = 0
        for message in messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += self.count_tokens(value)
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 3  # every reply is primed with assistant
        return num_tokens
