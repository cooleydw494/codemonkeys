from codemonkeys.defs import nl, nl2
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t


class OutputChecker:

    def __init__(self):
        self.gpt_client = None
        self.prompt = ''
        self.model = ''
        self.temp = ''
        self.max_tokens = None
        self.tries = 1
        self.current_try = 0

    def set_model(self, model: str, temp: float, max_tokens: int) -> 'OutputChecker':
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        self.gpt_client = GPTClient(model, temp, max_tokens)
        return self

    def set_prompt(self, prompt: str) -> 'OutputChecker':
        self.prompt = prompt
        return self

    def set_tries(self, tries: int) -> 'OutputChecker':
        self.tries = tries
        return self

    def set_current_try(self, current_try: int) -> 'OutputChecker':
        self.current_try = current_try
        return self

    def has_tries(self) -> bool:
        return self.current_try <= self.tries

    def check_output(self, output: str) -> bool:

        check_prompt = f"{self.prompt}{nl2}{output}"
        print_t(f"Checking Output With Prompt:{nl}{self.prompt}", 'quiet')
        check_result = self.gpt_client.generate(check_prompt)

        if check_result.lower() == 'true':
            print_t(f"Output Check Passed. {check_result}", 'special')
            output_valid = True
        else:
            print_t(f"Output Check Failed. Result: {check_result}", 'warning')
            output_valid = False

        self.current_try += 1
        return output_valid
