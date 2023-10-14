from typing import Optional

from codemonkeys.defs import nl, content_sep
from codemonkeys.types import OStr, OFloat, OInt
from codemonkeys.utils.misc.file_ops import get_file_contents
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t


class Summarizer:
    """A class to summarize given text using GPT."""

    _model: OStr = None
    _temp: OFloat = None
    _max_tokens: OInt = None
    _gpt_client: Optional[GPTClient] = None
    _prompt: OStr = None
    _context: OStr = None

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
        self._gpt_client = GPTClient(self._model, self._temp, self._max_tokens)
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
        :raises RuntimeError: When no context is provided for summary.
        """
        if not self._context:
            raise RuntimeError("No context provided to summarize.")

        context_tokens = self._gpt_client.count_tokens(self._context)

        if context_tokens > self._max_tokens:
            summary = self._summarize_chunked()
        else:
            full_prompt = f"{self._prompt}: {content_sep}{self._context}{content_sep}"
            summary = self._gpt_client.generate(full_prompt)

        if summary is None:
            raise RuntimeError(f"Failed to generate a summary for the context.")

        print_t("Context summarized.", 'info')
        print_t(f"Summary:{nl}{summary}", 'quiet')

        return summary

    def _summarize_chunked(self) -> str:
        """
        Summarize the given text context in chunks using GPT.

        :return: The summarized text.
        """
        chunked_context = self._gpt_client.split_into_chunks(self._context, self._max_tokens)
        print_t(f"Split context into {len(chunked_context)} chunks.", 'info')
        print_t('Summarizing each chunk... is not implemented [see TODO in summarizer.py]', 'loading')
        # TODO: implement summarization of chunked context
        exit()
