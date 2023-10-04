import os
import time

from codemonkeys.defs import nl
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t


class FileIterator:

    _temp = None
    _model = None
    _max_tokens = None
    _gpt_client = None
    _work_path = None
    _include_extensions = []
    _include_patterns = []
    _exclude_patterns = []
    _filtered_files = []

    def work_path(self, work_path: str) -> 'FileIterator':
        """Set the working path for the FileIterator.

        :param str work_path: The path as a string.
        :return: The FileIterator instance with the new work_path value.
        """
        self._work_path = work_path
        return self

    def file_types_included(self, file_types_included: str) -> 'FileIterator':
        """Set the included file types for the FileIterator.

        :param str file_types_included: The file types as a comma-separated string.
        :return: The FileIterator instance with the new _include_extensions value.
        """
        self._include_extensions = file_types_included.split(',')
        return self

    def filepath_match_include(self, filepath_match_include: str) -> 'FileIterator':
        """Set the filepaths to include in the FileIterator.

        :param str filepath_match_include: The include patterns as a comma-separated string.
        :return: The FileIterator instance with the new _include_patterns value.
        """
        self._include_patterns = filepath_match_include.split(',') if filepath_match_include is not None else []
        return self

    def filepath_match_exclude(self, filepath_match_exclude: str) -> 'FileIterator':
        """Set the filepaths to exclude from the FileIterator.

        :param str filepath_match_exclude: The exclude patterns as a comma-separated string.
        :return: The FileIterator instance with the new _exclude_patterns value.
        """
        self._exclude_patterns = filepath_match_exclude.split(',') if filepath_match_exclude is not None else []
        return self

    def token_count_model(self, model: str, temp: float, max_tokens: int) -> 'FileIterator':
        """Set the token count model for the FileIterator.

        :param str model: The name of the model.
        :param float temp: The temperature for the model.
        :param int max_tokens: The maximum number of tokens.
        :return: Self for method chaining.
        """
        self._model = model
        self._temp = temp
        self._max_tokens = max_tokens
        self._gpt_client = GPTClient(model, temp, max_tokens)
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

        :return: Self for method chaining.
        """
        self._filtered_files = []
        print_t("Filtering files...", 'loading')
        print_t(f'WORK_PATH: {self._work_path}', 'info')

        for root, _, files in os.walk(self._work_path):
            for file in files:
                print(".", end='', flush=True)
                time.sleep(0.001)

                absolute_path = self.resolve_path(os.path.join(root, file))
                if self._should_include(absolute_path):
                    with open(absolute_path, 'r') as f:
                        num_tokens = self._gpt_client.count_tokens(f.read())

                    if num_tokens <= self._max_tokens:
                        self._filtered_files.append(absolute_path)

        print_t("File filtering complete.", 'quiet')

        return self

    def pop_file(self) -> str | None:
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
