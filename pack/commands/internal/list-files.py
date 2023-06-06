import os
import time

from definitions import STORAGE_TEMP_PATH
from pack.modules.internal.config_mgmt.env_class import ENV
from pack.modules.internal.gpt.token_counter import TokenCounter
from pack.modules.internal.theme.theme_functions import print_t


def resolve_path(path: str) -> str:
    """
    Resolves path variables and expands user home.

    :param path: A string path
    :return: A resolved path string
    """
    return os.path.abspath(os.path.expandvars(os.path.expanduser(path)))


def should_include(file_path: str, include_extensions: list, exclude_patterns: list) -> bool:
    """
    Checks if a file should be included based on its extension and patterns in its path.

    :param file_path: The file path
    :param include_extensions: A list of extensions to include
    :param exclude_patterns: A list of path patterns to exclude
    :return: True if file should be included, False otherwise
    """
    return (
        any(file_path.endswith(ext) for ext in include_extensions) and
        not any(pattern in file_path for pattern in exclude_patterns)
    )


def filter_files_by_token_count():
    """Filters files by token count and saves a list of valid files."""
    env = ENV()  # Initialize ENV instance
    include_extensions = env.FILE_TYPES_INCLUDED.split(',')
    exclude_patterns = env.FILEPATH_MATCH_EXCLUDED.split(',')
    max_tokens = env.FILE_SELECT_MAX_TOKENS
    token_counter = TokenCounter('gpt-4')

    output_file = os.path.join(STORAGE_TEMP_PATH)
    print_t(f"WORK_PATH: {env.WORK_PATH}", 'info')

    filtered_files = []
    print_t("Filtering files... this might take a while depending on the size of your WORK_PATH.", 'loading')

    for root, _, files in os.walk(env.WORK_PATH):
        for file in files:
            print(".", end='', flush=True)
            time.sleep(0.001)

            if should_include(file, include_extensions, exclude_patterns):
                absolute_path = resolve_path(os.path.join(root, file))
                with open(absolute_path, 'r') as f:
                    num_tokens = token_counter.count_tokens(f.read())

                if num_tokens <= max_tokens:
                    filtered_files.append(absolute_path)

    print_t("Filtering completed!", 'success')

    with open(output_file, "w") as f:
        for idx, file_path in enumerate(filtered_files, start=1):
            f.write(f"{idx}. {file_path}{os.linesep}")

    print_t(f"📝 List of files saved to {output_file}. Enjoy coding with your 🐒 code monkeys!", 'done')

    with open(output_file, "r") as f:
        lines = f.readlines()
        preview = "".join(lines[:15]) + "..." if len(lines) > 15 else "".join(lines)
        print_t(preview, 'cyan')


if __name__ == "__main__":
    filter_files_by_token_count()
