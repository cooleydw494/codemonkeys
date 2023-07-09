import os

from codemonkeys.abilities.gpt_client import GPTClient
from codemonkeys.tasks.output_checker import OutputChecker
from codemonkeys.tasks.output_path_resolver import OutputPathResolver
from codemonkeys.utils.monk.theme_functions import print_t
from codemonkeys.defs import nl, nl2, _or


class FileHandler:

    def __init__(self):
        self.output_path_resolver = None
        self.gpt_client = None
        self.model = ''
        self.temp = ''
        self.max_tokens = None
        self.file_path = None
        self.main_prompt = ''
        self.context = ''
        self.output_example_prompt = ''
        self.ultimatum_prompt = ''
        self.output_filename_append = ''
        self.output_ext = ''
        self.skip_existing_output_files = False
        self.output_remove_strings = []
        self.output_checker: OutputChecker | None = None
        self.output_path = ''

    def set_path(self, file_path: str) -> 'FileHandler':
        self.file_path = file_path
        return self

    def set_context(self, context: str) -> 'FileHandler':
        self.context = context
        return self

    def set_output_filename_append(self, output_filename_append: str) -> 'FileHandler':
        self.output_filename_append = output_filename_append
        return self

    def set_output_ext(self, output_ext: str) -> 'FileHandler':
        self.output_ext = output_ext
        return self

    def set_skip_existing(self, skip_existing_output_files: bool) -> 'FileHandler':
        self.skip_existing_output_files = skip_existing_output_files
        return self

    def set_main_prompt(self, main_prompt: str) -> 'FileHandler':
        self.main_prompt = main_prompt
        return self

    def set_ultimatum_prompt(self, ultimatum_prompt: str) -> 'FileHandler':
        self.ultimatum_prompt = ultimatum_prompt
        return self

    def set_output_example_prompt(self, output_example_prompt: str) -> 'FileHandler':
        self.output_example_prompt = output_example_prompt
        return self

    def set_model(self, model: str, temp: float, max_tokens: int) -> 'FileHandler':
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        return self

    def set_output_remove_strings(self, output_remove_strings: str) -> 'FileHandler':
        self.output_remove_strings = output_remove_strings.split(',')
        return self

    def set_output_path(self, output_path: str) -> 'FileHandler':
        self.output_path = output_path
        return self

    def set_output_checker(self, output_checker: OutputChecker) -> 'FileHandler':
        self.output_checker = output_checker
        return self

    def set_output_path_resolver(self, output_path_resolver: OutputPathResolver) -> 'FileHandler':
        self.output_path_resolver = output_path_resolver
        return self

    def get_output(self, full_prompt):

        output = self.gpt_client.generate(full_prompt)

        if self.output_remove_strings is not None:
            for remove_str in self.output_remove_strings:
                output = output.replace(remove_str, '')

        print_t("Output returned.", 'quiet')
        print_t(f"{output}", 'file')
        return output

    def handle(self):
        print(f"Processing file: {self.file_path}")

        if self.skip_existing_output_files and self.output_path_resolver.output_file_exists(self.file_path):
            print_t(f"{self.file_path} exists and was skipped.", 'quiet')
            return

        the_file_name = os.path.basename(self.file_path)
        output_file_path = self.output_path_resolver.get_output_path(self.file_path)

        with open(self.file_path, "r") as f:
            file_contents = f.read()

        main_prompt = _or(self.main_prompt)
        ultimatum = _or(self.ultimatum_prompt)
        output_example = _or(self.output_example_prompt)

        full_prompt = f"{main_prompt}{nl}{self.context}{nl}{the_file_name}:{nl}" \
                      f"```{file_contents}```{nl}{ultimatum}{nl}{output_example}"

        # Print full prompt with placeholders
        print_t(f"{main_prompt}{nl2}<context>{nl2}{the_file_name}:{nl}"
                f"```<file contents>```{nl2}{ultimatum}{nl2}<output example>",
                'info')

        # Prepare GPT client for Main Prompt
        self.gpt_client = GPTClient(self.model, self.temp, self.max_tokens)

        # Prepare output directory
        output_dir = os.path.join(self.output_path)
        os.makedirs(output_dir, exist_ok=True)

        output = None

        oc = self.output_checker
        if oc is not None:
            oc.set_current_try(0)

            while oc.has_tries() and output is None:
                print_t(f"Attempt {oc.current_try}/{oc.tries} for {the_file_name}...", 'loading')

                unchecked_output = self.get_output(full_prompt)
                if oc.check_output(unchecked_output):
                    output = unchecked_output

        else:
            output = self.get_output(full_prompt)

        with open(output_file_path, "w") as f:
            f.write(output)
        print(f"Output saved to: {output_file_path}", 'success')
