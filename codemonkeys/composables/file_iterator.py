import os
import time

from codemonkeys.defs import nl
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t


class FileIterator:

    def __init__(self):
        self.temp = None
        self.model = None
        self.include_extensions = []
        self.exclude_patterns = []
        self.max_tokens = None
        self.gpt_client = None
        self.work_path = None
        self.filtered_files = []

    def set_work_path(self, work_path: str) -> 'FileIterator':
        self.work_path = work_path
        return self

    def set_file_types_included(self, file_types_included: str) -> 'FileIterator':
        self.include_extensions = file_types_included.split(',')
        return self

    def set_filepath_match_exclude(self, filepath_match_exclude: str) -> 'FileIterator':
        self.exclude_patterns = filepath_match_exclude.split(',') if filepath_match_exclude is not None else []
        return self

    def set_token_count_model(self, model: str, temp: float, max_tokens: int) -> 'FileIterator':
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        self.gpt_client = GPTClient(model)
        return self

    @staticmethod
    def resolve_path(path: str) -> str:
        return os.path.abspath(os.path.expandvars(os.path.expanduser(path)))

    def _should_include(self, file_path: str) -> bool:
        return (
                any(file_path.endswith(ext) for ext in self.include_extensions) and
                not any(pattern.strip() in file_path for pattern in self.exclude_patterns)
        )

    def filter_files(self) -> 'FileIterator':
        self.filtered_files = []
        print_t("Filtering files...", 'loading')
        print_t(f'WORK_PATH: {self.work_path}', 'info')

        for root, _, files in os.walk(self.work_path):
            for file in files:
                print(".", end='', flush=True)
                time.sleep(0.001)

                if self._should_include(file):
                    absolute_path = self.resolve_path(os.path.join(root, file))
                    with open(absolute_path, 'r') as f:
                        num_tokens = self.gpt_client.count_tokens(f.read())

                    if num_tokens <= self.max_tokens:
                        self.filtered_files.append(absolute_path)

        print_t("File filtering complete.", 'quiet')

        return self

    def pop_file(self) -> str | None:
        if len(self.filtered_files) == 0:
            return None
        selected_file = self.filtered_files.pop(0)

        # Skip files that are not readable
        if os.access(selected_file, os.R_OK) is not True:
            print_t(f"Unable to read file:{nl}{selected_file}{nl}Skipped.", 'warning')

        return selected_file
