import os

from codemonkeys.abilities.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.defs import nl


class ContextHandler:

    def __init__(self):
        self.context_file_path = None
        self.context_summary_prompt = None
        self.summary_model = None
        self.summary_temp = None
        self.max_tokens = None
        self.allow_summarized = False

    def model(self, model, temp, max_tokens):
        self.summary_model = model
        self.summary_temp = temp
        self.max_tokens = max_tokens
        return self

    def prompt(self, prompt):
        self.context_summary_prompt = prompt
        return self

    def context_file(self, file_path):
        self.context_file_path = os.path.expanduser(file_path)
        return self

    def get_unsummarized_context(self) -> str:
        if not os.path.isfile(self.context_file_path):
            raise FileNotFoundError(f"The context file {self.context_file_path} does not exist.")

        with open(self.context_file_path, "r") as f:
            context_file_contents = f.read()

        return context_file_contents

    def summarize(self) -> str:

        context_file_contents = self.get_unsummarized_context()

        summary_client = GPTClient(self.summary_model, self.summary_temp, self.max_tokens)

        context_file_contents = summary_client.split_into_chunks(context_file_contents, self.max_tokens)

        context_file_contents = '' if context_file_contents == '' else context_file_contents

        if len(context_file_contents) > 1:
            print_t(f"Split the context file {self.context_file_path} into {len(context_file_contents)} chunks.", 'info')
            print_t('Summarizing each chunk... [see TODO in context_summarizer.py]', 'loading')
            # TODO: implement summarization of chunked context files
            exit()

        # If not chunked (length 1), summarize the context file
        summary_prompt = f'{self.context_summary_prompt}: ```{context_file_contents[0]}```'
        context_file_summary = summary_client.generate(summary_prompt)

        # Check if a summary was successfully generated
        if not context_file_summary:
            raise RuntimeError(f"Failed to generate a summary for the context file {self.context_file_path}.")

        print_t("Special file summarized!", 'success')
        print_t(f"Summary:{nl}{context_file_summary}", 'file')

        return context_file_summary
