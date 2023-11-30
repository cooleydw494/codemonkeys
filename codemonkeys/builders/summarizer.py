from typing import Optional

from codemonkeys.defs import nl, content_sep
from codemonkeys.types import OStr, OFloat, OInt
from codemonkeys.utils.gpt.gpt_client import GptClient
from codemonkeys.utils.misc.file_ops import get_file_contents
from codemonkeys.utils.monk.theme_functions import print_t


class Summarizer:
    """
    A builder class to summarize given text using GPT.

    This class provides functionality to set up and run text summarization using the GPT model.
    It allows for setting the model, temperature, max tokens, GPT prompt, and the text context.
    It also offers a method to read a text context directly from a file. The summarization
    process executes with the given context and generates a summarized version of the text.

    Attributes:
        _model (OStr): The GPT model identifier.
        _temp (OFloat): The temperature setting for the GPT model.
        _max_tokens (OInt): The maximum number of tokens allowed in the GPT output.
        _gpt_client (Optional[GptClient]): The GPT client instance for API interactions.
        _prompt (OStr): The prompt to direct GPT's text summarization task.
        _context (OStr): The text content to be summarized by GPT.
    """

    def __init__(self):
        self._model: OStr = None
        self._temp: OFloat = None
        self._max_tokens: OInt = None
        self._gpt_client: Optional[GptClient] = None
        self._prompt: OStr = None
        self._context: OStr = None

    def model(self, model: str, temp: float, max_tokens: int) -> 'Summarizer':
        """
        Set the GPT model, temperature, and max tokens for the summarizer.

        :param str model: The GPT model to be used.
        :param float temp: The temperature to be used.
        :param int max_tokens: The maximum number of tokens.
        :return: Self for method chaining.
        """
        self._model = model
        self._temp = temp
        self._max_tokens = max_tokens
        self._gpt_client = GptClient(self._model, self._temp, self._max_tokens)
        return self

    def prompt(self, prompt: str) -> 'Summarizer':
        """
        Set the GPT prompt for the summarizer.

        :param str prompt: The prompt to be used.
        :return: Self for method chaining.
        """
        self._prompt = prompt
        return self

    def context(self, context_string: str) -> 'Summarizer':
        """
        Set the text context for the summarizer.

        :param str context_string: The context string to be used.
        :return: Self for method chaining.
        """
        self._context = context_string
        return self

    def context_from_file(self, path: str) -> 'Summarizer':
        """
        Set the text context for the summarizer by reading from a file.

        :param str path: The file path to read the context from.
        :return: Self for method chaining.
        """
        self._context = get_file_contents(path)
        return self

    def summarize(self) -> str:
        """
        Summarize the given text context using GPT.

        :return: The summarized text.
        :raises RuntimeError: When no context is provided for summary, or when context exceeds max tokens.
        """
        if not self._context:
            raise RuntimeError("No context provided to summarize.")

        context_tokens = self._gpt_client.count_tokens(self._context)

        if context_tokens > self._max_tokens:
            raise RuntimeError(f"Context ({context_tokens} tokens) longer than max tokens ({self._max_tokens}).")
        else:
            full_prompt = f"{self._prompt}: {content_sep}{self._context}{content_sep}"
            summary = self._gpt_client.generate(full_prompt)

        if summary is None:
            raise RuntimeError(f"Failed to generate a summary for the context.")

        print_t("Context summarized.", 'info')
        print_t(f"Summary:{nl}{summary}", 'quiet')

        return summary
