from codemonkeys.defs import nl, nl2
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t


class OutputChecker:
    """A composable class to manage output checking for generated text using GPT models."""

    _model = ''
    _temp = ''
    _max_tokens = None
    _gpt_client = None
    _prompt = ''
    _tries = 1
    _current_try = 0

    def model(self, model: str, temp: float, max_tokens: int) -> 'OutputChecker':
        """
        Sets the GPT model to use for checking output.

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

    def prompt(self, prompt: str) -> 'OutputChecker':
        """
        Sets the _prompt to use for checking output.

        :param str prompt: The _prompt to set.
        :return: Self for method chaining.
        """
        self._prompt = prompt
        return self

    def tries(self, tries: int) -> 'OutputChecker':
        """
        Sets the number of _tries allowed for output checking.

        :param int tries: The number of _tries to set.
        :return: Self for method chaining.
        """
        self._tries = tries
        return self

    def set_current_try(self, current_try: int) -> 'OutputChecker':
        """
        Sets the current try number for output checking.

        :param int current_try: The number current _tries.
        :return: Self for method chaining.
        """
        self._current_try = current_try
        return self

    def has_tries(self) -> bool:
        """
        Checks if there are any _tries remaining.

        :return: True if there are _tries remaining, otherwise False.
        """
        return self._current_try <= self._tries

    def check_output(self, output: str) -> bool:
        """
        Checks the given output using the output check _prompt.

        :param str output: The output to check.
        :return: True if the output passes the check, otherwise False.
        """
        check_prompt = f"{self._prompt}{nl2}{output}"
        print_t(f"Checking Output With Prompt:{nl}{self._prompt}", 'quiet')
        check_result = self._gpt_client.generate(check_prompt)

        if check_result is None:
            print_t(f"Output Check Failed because output check response could not be generated.", 'warning')
            return False

        if check_result.lower() == 'true':
            print_t(f"Output Check Passed. {check_result}", 'special')
            output_valid = True
        else:
            print_t(f"Output Check Failed. Result: {check_result}", 'warning')
            output_valid = False

        self._current_try += 1
        return output_valid
