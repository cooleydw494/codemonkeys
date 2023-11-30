import os
from typing import Optional

from codemonkeys.defs import nl, nl2, _or, content_sep
from codemonkeys.funcs.finalize_output import FinalizeOutput
from codemonkeys.types import OStr, OFloat, OInt
from codemonkeys.utils.gpt.gpt_client import GptClient
from codemonkeys.utils.imports.env import Env
from codemonkeys.utils.misc.file_ops import get_file_contents
from codemonkeys.utils.monk.theme_functions import print_t, verbose_logs_enabled

env = Env.get()


class FilePrompter:
    """
    Builder for generating output based on files' content using configured PROMPTs.

    This builder class orchestrates the construction and execution of GPT-based file content editing tasks,
    providing a fluid interface for setting up inputs and generating outputs using specific GPT model configurations.
    It serves as a bridge between the file contents and the GPT client, translating file data into contextual information
    that the GPT model can use to generate desired outputs.

    Attributes:
        _model (OStr): GPT model to be used.
        _temp (OFloat): Temperature setting for GPT model.
        _max_tokens (OInt): Maximum tokens for response generation.
        _gpt_client (Optional[GptClient]): GPT client instance for interaction with the API.
        _finalize_output (bool): Flag indicating whether the FinalizeOutput function should be used.
        _file_path (OStr): Path of the file being processed.
        _file_name (OStr): Name of the file extracted from the file path.
        _main_prompt (OStr): Main GPT prompt to frame the task.
        _context (OStr): Additional context provided to the GPT model.
        _output_prompt (OStr): Example prompt to guide the expected output format.
        _ultimatum_prompt (OStr): Ultimatum prompt to coerce GPT towards desired output.
        _skip_existing_output_files (bool): Flag indicating whether existing output files should be skipped.
    """

    def __init__(self):
        self._model: OStr = None
        self._temp: OFloat = None
        self._max_tokens: OInt = None
        self._gpt_client: Optional[GptClient] = None
        self._finalize_output: bool = False
        self._file_path: OStr = None
        self._file_name: OStr = None
        self._main_prompt: OStr = None
        self._context: OStr = None
        self._output_prompt: OStr = None
        self._ultimatum_prompt: OStr = None
        self._skip_existing_output_files: bool = False

    def file_path(self, file_path: str) -> 'FilePrompter':
        """Sets the file path and the file name to be used in the prompts.

        :param str file_path: The file path to set
        :return: FilePrompter: returns the updated instance
        """
        self._file_path = file_path
        self._file_name = os.path.basename(file_path)
        return self

    def context(self, context: OStr = None) -> 'FilePrompter':
        """Sets the context to be used in the prompts.

        :param str context: The context string to set
        :return: FilePrompter: returns the updated instance
        """
        self._context = context
        return self

    def main_prompt(self, main_prompt: str) -> 'FilePrompter':
        """Sets the main prompt to be used in the prompts.

        :param str main_prompt: The main prompt string to set
        :return: FilePrompter: returns the updated instance
        """
        self._main_prompt = main_prompt
        return self

    def ultimatum_prompt(self, ultimatum_prompt: str) -> 'FilePrompter':
        """Sets the ultimatum prompt to be used in the prompts.

        :param str ultimatum_prompt: The ultimatum prompt string to set
        :return: FilePrompter: returns the updated instance
        """
        self._ultimatum_prompt = ultimatum_prompt
        return self

    def output_prompt(self, output_prompt: str) -> 'FilePrompter':
        """Sets the output example prompt to be used in the prompts.

        :param str output_prompt: The output example prompt string to set
        :return: FilePrompter: returns the updated instance
        """
        self._output_prompt = output_prompt
        return self

    def model(self, model: str, temp: float, max_tokens: int) -> 'FilePrompter':
        """Sets the GPT model, temperature, and max tokens to use for generating outputs.

        :param str model: The GPT model to set
        :param float temp: The temperature to set
        :param int max_tokens: The maximum tokens to generate
        :return: FilePrompter: returns the updated instance
        """
        self._model = model
        self._temp = temp
        self._max_tokens = max_tokens
        self._gpt_client = GptClient(model, temp, max_tokens)
        return self

    def finalize_output(self, finalize_output: bool = True) -> 'FilePrompter':
        """Sets whether or not to use the FinalizeOutput Func to finalize the output.

        :param bool finalize_output: Whether or not to finalize the output
        :return: FilePrompter: returns the updated instance
        """
        self._finalize_output = finalize_output
        return self

    def generate_output(self) -> OStr:
        """Gets the generated output from the GPT model using the configured prompts.

        :return: str: The output generated by the model
        """
        full_prompt = self._get_full_prompt(print_prompt=True)

        if self._finalize_output:
            output = self._gpt_client.generate(full_prompt, [FinalizeOutput()], 'finalize_output')
        else:
            output = self._gpt_client.generate(full_prompt)

        if output is None:
            print_t(f"Valid output could not be generated for: {self._file_path}", 'error')
            return None

        print_t("Output returned.", 'info')
        print_t(f"{output}", 'quiet')
        return output

    def _get_full_prompt(self, print_prompt: bool = False) -> str:
        """Creates the full prompt using the configured input options.

        :param bool print_prompt: Whether or not to print the prompt to the console
        :return: str: The full prompt
        """
        main_prompt = _or(self._main_prompt.replace('{the-file}', self._file_name))
        ultimatum = _or(self._ultimatum_prompt.replace('{the-file}', self._file_name))
        output_prompt = _or(self._output_prompt.replace('{the-file}', self._file_name))
        file_contents = get_file_contents(self._file_path)

        full_prompt = f"{main_prompt}{nl}{self._context or ''}{nl}{self._file_name}:{nl}" \
                      f"{content_sep}{nl}{file_contents}{content_sep}{nl}{ultimatum}{nl}{output_prompt}"

        print_t('File Prompt:', 'important')
        if print_prompt and verbose_logs_enabled():
            print_t(full_prompt, 'quiet')
        elif print_prompt:
            stubbed_context = f'<context>{nl2}' if self._context else ''
            stubbed_ultimatum = f'<ultimatum>{nl2}' if self._ultimatum_prompt else ''
            stubbed_output_prompt = f'<output example>{nl2}' if self._output_prompt else ''
            stubbed_prompt = f"{main_prompt}{nl2}{stubbed_context}{self._file_name}:{nl}" \
                             f"{content_sep}<file contents>{content_sep}{nl2}{stubbed_ultimatum}{stubbed_output_prompt}"
            print_t(stubbed_prompt, 'quiet')

        return full_prompt
