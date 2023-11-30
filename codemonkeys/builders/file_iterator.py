import os
import time
from typing import Optional

from codemonkeys.defs import nl, content_sep
from codemonkeys.funcs.extract_list import ExtractList
from codemonkeys.types import OFloat, OStr, OInt
from codemonkeys.utils.gpt.gpt_client import GptClient
from codemonkeys.utils.imports.theme import Theme
from codemonkeys.utils.monk.theme_functions import print_t


class FileIterator:

    def __init__(self):

        self._token_count_client: Optional[GptClient] = None
        self._token_count_model: OStr = None
        self._filter_max_tokens: OInt = None

        self._file_select_client: Optional[GptClient] = None
        self._file_select_prompt: OStr = None
        self._file_select_model: OStr = 'gpt-3.5-turbo'
        self._file_select_temp: OFloat = 0.8
        self._file_select_max_tokens: OInt = 3000

        self._work_path: OStr = None
        self._include_extensions: tuple = ()
        self._include_patterns: tuple = ()
        self._exclude_patterns: tuple = ()
        self._filtered_files = []

    def work_path(self, work_path: str) -> 'FileIterator':
        """Set the working path for the FileIterator.

        :param str work_path: The path as a string.
        :return: The FileIterator instance with the new work_path value.
        """
        self._work_path = work_path
        return self

    def include_exts(self, include_exts: tuple = ()) -> 'FileIterator':
        """Set the included file types for the FileIterator.

        :param tuple include_exts: The file types as a tuple of strings.
        :return: The FileIterator instance with the new _include_extensions value.
        """
        self._include_extensions = include_exts
        return self

    def filepath_match_include(self, filepath_match_include: tuple) -> 'FileIterator':
        """Set the filepaths to include in the FileIterator.

        :param tuple filepath_match_include: The include patterns as a tuple of strings.
        :return: The FileIterator instance with the new _include_patterns value.
        """
        self._include_patterns = filepath_match_include
        return self

    def filepath_match_exclude(self, filepath_match_exclude: tuple) -> 'FileIterator':
        """Set the filepaths to exclude from the FileIterator.

        :param tuple filepath_match_exclude: The exclude patterns as a tuple of strings.
        :return: The FileIterator instance with the new _exclude_patterns value.
        """
        self._exclude_patterns = filepath_match_exclude
        return self

    def file_select_prompt(self, file_select_prompt: OStr) -> 'FileIterator':
        """Set the file select prompt for the FileIterator.

        :param str file_select_prompt: The file select prompt as a string.
        :return: Self for method chaining.
        """
        self._file_select_prompt = file_select_prompt
        return self

    def token_count_model(self, model: str, filter_max_tokens: int) -> 'FileIterator':
        """Set the token count model for the FileIterator.

        :param str model: The name of the model.
        :param int filter_max_tokens: The maximum number of tokens per file (not a max for the client)
        :return: Self for method chaining.
        """
        self._token_count_model = model
        self._filter_max_tokens = filter_max_tokens
        self._token_count_client = GptClient(model)
        return self

    def file_select_model(self, model: str, temp: float, max_tokens: int) -> 'FileIterator':
        """Set the file select model for the FileIterator.

        :param str model: The name of the model.
        :param float temp: The temperature for the model.
        :param int max_tokens: The maximum number of tokens.
        :return: Self for method chaining.
        """
        self._file_select_model = model
        self._file_select_temp = temp
        self._file_select_max_tokens = max_tokens
        self._file_select_client = GptClient(model, temp, max_tokens)
        return self

    @staticmethod
    def resolve_path(path: str) -> str:
        """Resolve a given path by expanding variables and user information.

        :param str path: The path string to resolve.
        :return: The resolved path string.
        """
        return os.path.abspath(os.path.expandvars(os.path.expanduser(path)))

    def _should_include(self, file_path: str) -> bool:
        """Check if a given file path should be included in the iterator.

        :param str file_path: The file path string to check.
        :return: A boolean indicating if the file path should be included.
        """

        passes_include_patterns = (any(pattern.strip() in file_path for pattern in self._include_patterns) or
                                   len(self._include_patterns) == 0)

        passes_include_exts = (any(file_path.endswith(ext) for ext in self._include_extensions) or
                               len(self._include_extensions) == 0)

        passes_exclude_patterns = (not any(pattern.strip() in file_path for pattern in self._exclude_patterns) or
                                   len(self._exclude_patterns) == 0)

        return passes_include_exts and passes_include_patterns and passes_exclude_patterns

    def filter_files(self) -> 'FileIterator':
        """Filter the files in the working path based on include and exclude patterns.

        Optionally, if file_select_prompt is provided, GPT will be used to further filter the files.

        :return: Self for method chaining.
        """
        self._filtered_files = []
        print_t("Filtering files...", 'loading')

        for root, _, files in os.walk(self._work_path):
            for file in files:
                print(".", end='', flush=True)
                time.sleep(0.005)

                absolute_path = self.resolve_path(os.path.join(root, file))
                if self._should_include(absolute_path):
                    with open(absolute_path, 'r') as f:
                        num_tokens = self._token_count_client.count_tokens(f.read())

                    if num_tokens <= self._filter_max_tokens:
                        self._filtered_files.append(absolute_path)

        if self._file_select_prompt:
            print_t(f"Further filtering with FILE_SELECT_PROMPT: {self._file_select_prompt}", 'info')
            current_list = str(self._filtered_files)
            prompt = (f"Examine the following list of filepaths: {content_sep}{current_list}{content_sep}"
                      f"Return the list of filepaths filtered by this prompt: {self._file_select_prompt}.")
            self._filtered_files = \
                (GptClient(self._file_select_model, self._file_select_temp, self._file_select_max_tokens)
                 .generate(prompt, [ExtractList()], 'extract_list'))

        print()
        print_t(f"File filtering complete.{nl}", 'done')
        print_t(f'Selected Files:{nl}{self._filtered_files}', 'special')

        return self

    def pop_file(self) -> OStr:
        """Get the next file in the _filtered_files list and remove it from the list.

        :return: The next file string or None if the list is empty.
        """
        if len(self._filtered_files) == 0:
            return None
        selected_file = self._filtered_files.pop(0)

        # Skip files that are not readable
        if os.access(selected_file, os.R_OK) is not True:
            print_t(f"Unable to read file:{nl}{selected_file}{nl}Skipped.", 'warning')

        return selected_file

    def get_filtered_files(self) -> list[str]:
        """Get the _filtered_files list.

        :return: The _filtered_files list.
        """
        return self._filtered_files

    def print_files_remaining(self, incl_next_file: bool = False) -> None:
        print(nl)
        terminal_max = min(Theme.max_terminal_width, os.get_terminal_size().columns)
        num_of_spacers = int(terminal_max / 3)
        print_t(f"{'---' * num_of_spacers}", 'info', incl_prefix=False)
        count_remaining = len(self.get_filtered_files())
        print_t(f"Files remaining: {count_remaining}", 'info')
        if incl_next_file and count_remaining > 0:
            print_t(f"-> {self.get_filtered_files()[0]}{nl}")
