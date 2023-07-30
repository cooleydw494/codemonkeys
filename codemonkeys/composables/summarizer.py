from codemonkeys.defs import nl, content_sep
from codemonkeys.utils.file_ops import get_file_contents
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t


class Summarizer:
    """A class to summarize given text using GPT."""

    def __init__(self):
        """
        Summarizer constructor.
        """
        self.context = None
        self.allow_summarized = False
        self.max_tokens = None
        self.model = None
        self.temp = None
        self.prompt = None

    def set_model(self, model: str, temp: float, max_tokens: int) -> 'Summarizer':
        """
        Set the GPT model, temperature, and max tokens for the summarizer.

        :param str model: The GPT model to be used.
        :param float temp: The temperature to be used.
        :param int max_tokens: The maximum number of tokens.
        :return: Self for method chaining.
        """
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        return self

    def set_prompt(self, prompt: str) -> 'Summarizer':
        """
        Set the GPT prompt for the summarizer.

        :param str prompt: The prompt to be used.
        :return: Self for method chaining.
        """
        self.prompt = prompt
        return self

    def set_context(self, context_string: str) -> 'Summarizer':
        """
        Set the text context for the summarizer.

        :param str context_string: The context string to be used.
        :return: Self for method chaining.
        """
        self.context = context_string
        return self

    def set_context_via_file(self, path: str) -> 'Summarizer':
        """
        Set the text context for the summarizer by reading from a file.

        :param str path: The file path to read the context from.
        :return: Self for method chaining.
        """
        self.context = get_file_contents(path)
        return self

    def summarize(self) -> str:
        """
        Summarize the given text context using GPT.

        :return: The summarized text.
        :raises RuntimeError: When no context is provided for summary.
        """
        if not self.context:
            raise RuntimeError("No context provided to summarize.")

        client = GPTClient(self.model, self.temp, self.max_tokens)
        context_tokens = client.count_tokens(self.context)

        if context_tokens > self.max_tokens:
            summary = self._summarize_chunked(client)
        else:
            full_prompt = f"{self.prompt}: {content_sep}{self.context}{content_sep}"
            summary = client.generate(full_prompt)

        if summary is None:
            raise RuntimeError(f"Failed to generate a summary for the context.")

        print_t("Context summarized.", 'info')
        print_t(f"Summary:{nl}{summary}", 'quiet')

        return summary

    def _summarize_chunked(self, client: GPTClient) -> str:
        """
        Summarize the given text context in chunks using GPT.

        :param GPTClient client: The client used for generating summary.
        :return: The summarized text.
        """
        chunked_context = client.split_into_chunks(self.context, self.max_tokens)
        print_t(f"Split context into {len(chunked_context)} chunks.", 'info')
        print_t('Summarizing each chunk... is not implemented [see TODO in summarizer.py]', 'loading')
        # TODO: implement summarization of chunked context
        exit()
