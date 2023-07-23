from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.file_ops import get_file_contents
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.defs import nl


class Summarizer:

    def __init__(self):
        self.context = None
        self.allow_summarized = False
        self.max_tokens = None
        self.model = None
        self.temp = None
        self.prompt = None

    def set_model(self, model, temp, max_tokens):
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        return self

    def set_prompt(self, prompt):
        self.prompt = prompt
        return self

    def set_context(self, context_string):
        self.context = context_string
        return self

    def set_context_via_file(self, path):
        self.context = get_file_contents(path)
        return self

    def summarize(self) -> str:

        if not self.context:
            raise RuntimeError("No context provided to summarize.")

        client = GPTClient(self.model, self.temp, self.max_tokens)
        context_tokens = client.count_tokens(self.context)

        if context_tokens > self.max_tokens:
            summary = self._summarize_chunked(client)
        else:
            full_prompt = f'{self.prompt}: ```{self.context}```'
            summary = client.generate(full_prompt)

        if not summary:
            raise RuntimeError(f"Failed to generate a summary for the context.")

        print_t("Context summarized.", 'info')
        print_t(f"Summary:{nl}{summary}", 'quiet')

        return summary

    def _summarize_chunked(self, client: GPTClient) -> str:

        chunked_context = client.split_into_chunks(self.context, self.max_tokens)
        print_t(f"Split context into {len(chunked_context)} chunks.", 'info')
        print_t('Summarizing each chunk... is not implemented [see TODO in summarizer.py]', 'loading')
        # TODO: implement summarization of chunked context
        exit()
