from typing import Optional

from codemonkeys.defs import nl, nl2
from codemonkeys.funcs.finalize_output import FinalizeOutput
from codemonkeys.types import OStr, OFloat, OInt
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t


class OutputFixer:
    """A composable class to manage output fixing for generated text using GPT models."""

    _model: OStr = None
    _temp: OFloat = None
    _max_tokens: OInt = None
    _gpt_client: Optional[GPTClient] = None
    _prompt: OStr = None

    def model(self, model: str, temp: float, max_tokens: int) -> 'OutputFixer':
        """
        Sets the GPT model to use for fixing output.

        :param str model: The model to set.
        :param float temp: The temperature to set.
        :param int max_tokens: The maximum amount of tokens to set.
        :return: Self for method chaining.
        """
        self._model = model
        self._temp = temp
        self._max_tokens = max_tokens
        self._gpt_client = GPTClient(model, temp, max_tokens)
        return self

    def prompt(self, prompt: str) -> 'OutputFixer':
        """
        Sets the _prompt to use for fixing output.

        :param str prompt: The _prompt to set.
        :return: Self for method chaining.
        """
        self._prompt = prompt
        return self

    def fix(self, content: str) -> OStr:

        fix_prompt = f"{self._prompt}{nl2}{content}"
        print_t(f"Fixing Output With Prompt:{nl}{self._prompt}", 'quiet')
        fix_result = self._gpt_client.generate(fix_prompt, [FinalizeOutput()], enforce_func='finalize_output')

        if fix_result is None:
            print_t(f"Failed to generate an Output Fixer response. Using original content.", 'warning')
            return content

        return fix_result
