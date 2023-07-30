from codemonkeys.defs import nl, nl2
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t


class OutputChecker:
    """A composable class to manage output checking for generated text using GPT models."""

    def __init__(self):
        self.gpt_client = None
        self.prompt = ''
        self.model = ''
        self.temp = ''
        self.max_tokens = None
        self.tries = 1
        self.current_try = 0

    def set_model(self, model: str, temp: float, max_tokens: int) -> 'OutputChecker':
        """
        Sets the GPT model to use for checking output.

        :param str model: The model to set.
        :param float temp: The temperature to set.
        :param int max_tokens: The maximum amount of tokens to set.
        :return: Self for method chaining.
        """
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        self.gpt_client = GPTClient(model, temp, max_tokens)
        return self

    def set_prompt(self, prompt: str) -> 'OutputChecker':
        """
        Sets the prompt to use for checking output.

        :param str prompt: The prompt to set.
        :return: Self for method chaining.
        """
        self.prompt = prompt
        return self

    def set_tries(self, tries: int) -> 'OutputChecker':
        """
        Sets the number of tries allowed for output checking.

        :param int tries: The number of tries to set.
        :return: Self for method chaining.
        """
        self.tries = tries
        return self

    def set_current_try(self, current_try: int) -> 'OutputChecker':
        """
        Sets the current try number for output checking.

        :param int current_try: The number current tries.
        :return: Self for method chaining.
        """
        self.current_try = current_try
        return self

    def has_tries(self) -> bool:
        """
        Checks if there are any tries remaining.

        :return: True if there are tries remaining, otherwise False.
        """
        return self.current_try <= self.tries

    def check_output(self, output: str) -> bool:
        """
        Checks the given output using the output check prompt.

        :param str output: The output to check.
        :return: True if the output passes the check, otherwise False.
        """
        check_prompt = f"{self.prompt}{nl2}{output}"
        print_t(f"Checking Output With Prompt:{nl}{self.prompt}", 'quiet')
        check_result = self.gpt_client.generate(check_prompt)

        if check_result is None:
            print_t(f"Output Check Failed because output check response could not be generated.", 'warning')
            return False

        if check_result.lower() == 'true':
            print_t(f"Output Check Passed. {check_result}", 'special')
            output_valid = True
        else:
            print_t(f"Output Check Failed. Result: {check_result}", 'warning')
            output_valid = False

        self.current_try += 1
        return output_valid
