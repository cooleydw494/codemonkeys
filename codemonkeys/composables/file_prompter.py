import os

from codemonkeys.defs import nl, nl2, _or, content_sep
from codemonkeys.utils.file_ops import get_file_contents
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t, verbose_logs_enabled
from codemonkeys.config.imports.env import Env

env = Env.get()


class FilePrompter:
    """Creates and configures a file prompter instance for generating model outputs
    based on the given file content and the provided prompts.
    """

    def __init__(self):
        self.gpt_client: GPTClient | None = None
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
        """Sets the file path and the file name to be used in the prompts.

        :param str file_path: The file path to set
        :return: FilePrompter: returns the updated instance
        """
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        return self

    def set_context(self, context: str) -> 'FilePrompter':
        """Sets the context to be used in the prompts.

        :param str context: The context string to set
        :return: FilePrompter: returns the updated instance
        """
        self.context = context
        return self

    def set_main_prompt(self, main_prompt: str) -> 'FilePrompter':
        """Sets the main prompt to be used in the prompts.

        :param str main_prompt: The main prompt string to set
        :return: FilePrompter: returns the updated instance
        """
        self.main_prompt = main_prompt
        return self

    def set_ultimatum_prompt(self, ultimatum_prompt: str) -> 'FilePrompter':
        """Sets the ultimatum prompt to be used in the prompts.

        :param str ultimatum_prompt: The ultimatum prompt string to set
        :return: FilePrompter: returns the updated instance
        """
        self.ultimatum_prompt = ultimatum_prompt
        return self

    def set_output_example_prompt(self, output_example_prompt: str) -> 'FilePrompter':
        """Sets the output example prompt to be used in the prompts.

        :param str output_example_prompt: The output example prompt string to set
        :return: FilePrompter: returns the updated instance
        """
        self.output_example_prompt = output_example_prompt
        return self

    def set_model(self, model: str, temp: float, max_tokens: int) -> 'FilePrompter':
        """Sets the GPT model, temperature, and max tokens to use for generating outputs.

        :param str model: The GPT model to set
        :param float temp: The temperature to set
        :param int max_tokens: The maximum tokens to generate
        :return: FilePrompter: returns the updated instance
        """
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        self.gpt_client = GPTClient(model, temp, max_tokens)
        return self

    def set_output_remove_strings(self, output_remove_strings: str) -> 'FilePrompter':
        """Sets the output remove strings to automatically remove them from the generated output.

        :param str output_remove_strings: The comma-separated remove strings to set
        :return: FilePrompter: returns the updated instance
        """
        self.output_remove_strings = output_remove_strings.split(',')
        return self

    def get_output(self) -> str | None:
        """Gets the generated output from the GPT model using the configured prompts.

        :return: str: The output generated by the model
        """
        full_prompt, stubbed_prompt = self._get_full_prompt()
        if verbose_logs_enabled():
            print_t(f'Prompt: {full_prompt}', 'quiet')
        else:
            print_t(f"Prompt: {stubbed_prompt}", 'quiet')

        print_t("Generating output...", 'loading')
        output = self.gpt_client.generate(full_prompt)

        if output is None:
            return None

        if self.output_remove_strings is not None:
            for remove_str in self.output_remove_strings:
                output = output.replace(remove_str, '')

        print_t("Output returned.", 'info')
        print_t(f"{output}", 'quiet')
        return output

    def _get_full_prompt(self) -> (str, str):
        """Creates the full prompt using the configured input options.

        :return: tuple of (str, str): Tuple of strings (full_prompt, stubbed_prompt)
        """
        main_prompt = _or(self.main_prompt)
        ultimatum = _or(self.ultimatum_prompt)
        output_example = _or(self.output_example_prompt)
        file_contents = get_file_contents(self.file_path)

        full_prompt = f"{main_prompt}{nl}{self.context}{nl}{self.file_name}:{nl}" \
                      f"{content_sep}{nl}{file_contents}{content_sep}{nl}{ultimatum}{nl}{output_example}"

        stubbed_prompt = f"{main_prompt}{nl2}<context>{nl2}{self.file_name}:{nl}" \
                         f"{content_sep}<file contents>{content_sep}{nl2}<ultimatum>{nl2}<output example>"

        return full_prompt, stubbed_prompt
