import os

from codemonkeys.abilities.gpt_client import GPTClient
from codemonkeys.utils.file_ops import get_file_contents
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.defs import nl, nl2, _or, import_env_class

Env = import_env_class()
env = Env.get()


class FilePrompter:

    def __init__(self):
        self.gpt_client = None
        self.model = ''
        self.temp = ''
        self.max_tokens = None
        self.file_path = None
        self.file_name = None
        self.main_prompt = ''
        self.context = ''
        self.output_example_prompt = ''
        self.ultimatum_prompt = ''
        self.skip_existing_output_files = False
        self.output_remove_strings = []

    def set_path(self, file_path: str) -> 'FilePrompter':
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        return self

    def set_context(self, context: str) -> 'FilePrompter':
        self.context = context
        return self

    def set_main_prompt(self, main_prompt: str) -> 'FilePrompter':
        self.main_prompt = main_prompt
        return self

    def set_ultimatum_prompt(self, ultimatum_prompt: str) -> 'FilePrompter':
        self.ultimatum_prompt = ultimatum_prompt
        return self

    def set_output_example_prompt(self, output_example_prompt: str) -> 'FilePrompter':
        self.output_example_prompt = output_example_prompt
        return self

    def set_model(self, model: str, temp: float, max_tokens: int) -> 'FilePrompter':
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        self.gpt_client = GPTClient(model, temp, max_tokens)
        return self

    def set_output_remove_strings(self, output_remove_strings: str) -> 'FilePrompter':
        self.output_remove_strings = output_remove_strings.split(',')
        return self

    def get_output(self):
        full_prompt, stubbed_prompt = self.get_full_prompt()
        if env.verbose_logs_enabled:
            print_t(f'Prompt: {full_prompt}', 'quiet')
        else:
            print_t(f"Prompt: {stubbed_prompt}", 'quiet')

        print_t("Generating output...", 'loading')
        output = self.gpt_client.generate(full_prompt)

        if self.output_remove_strings is not None:
            for remove_str in self.output_remove_strings:
                output = output.replace(remove_str, '')

        print_t("Output returned.", 'info')
        print_t(f"{output}", 'quiet')
        return output

    def get_full_prompt(self) -> (str, str):
        main_prompt = _or(self.main_prompt)
        ultimatum = _or(self.ultimatum_prompt)
        output_example = _or(self.output_example_prompt)
        file_contents = get_file_contents(self.file_path)

        full_prompt = f"{main_prompt}{nl}{self.context}{nl}{self.file_name}:{nl}" \
                      f"```{file_contents}```{nl}{ultimatum}{nl}{output_example}"

        stubbed_prompt = f"{main_prompt}{nl2}<context>{nl2}{self.file_name}:{nl}" \
                         f"```<file contents>```{nl2}<ultimatum>{nl2}<output example>"

        return full_prompt, stubbed_prompt
