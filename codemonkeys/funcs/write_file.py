import os

from codemonkeys.defs import nl2, nl
from codemonkeys.entities.func import Func
from codemonkeys.types import OStr
from codemonkeys.utils.misc.file_ops import write_file_contents
from codemonkeys.utils.misc.handle_exception import handle_exception
from codemonkeys.utils.monk.theme_functions import print_t, input_t


class WriteFile(Func):
    """
    This Func is intended to be used to handle the result of prompts that ask GPT to write a file.
    Unlike FinalizeOutput, this Func does not return file contents, but directly writes the files itself.

    WARNING!: Setting _base_path is particularly important as it verifies no file is written outside of that dir without
    confirmation. This is the primary safeguard against accidental file writes that could be destructive.
    """

    name: str = 'write_file'

    _description: str = 'Writes a single file fulfilling the prompt'

    _parameters: dict = {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Absolute filepath",
            },
            "contents": {
                "type": "string",
                "description": "Complete file contents, using JSON compatible unicode characters only",
            }
        },
        "required": ["filepath", "contents"],
    }

    def __init__(self, base_path: OStr = None, skip_existing: bool = False):
        self._base_path = base_path
        self._skip_existing = skip_existing

    def _execute(self, path: str, contents: str) -> OStr:

        file_path = os.path.expanduser(path)

        print_t(f'Preparing to write file to {file_path} with contents:{nl2}{contents}{nl}')

        expanded_base_path = os.path.expanduser(self._base_path) if self._base_path is not None else None
        confirm_base_path = self._base_path is not None and not file_path.startswith(expanded_base_path)
        if confirm_base_path:
            print_t(f'Filepath does not start with base path: {expanded_base_path}.'
                    f' Please review path before writing.', 'warning')
            user_input = input_t(f'Confirm file write?', '(y/n)')
            if user_input.lower() != 'y':
                print_t(f'Skipping file write.', 'warning')
                return None

        file_exists = os.path.exists(file_path)
        if file_exists and self._skip_existing:
            print_t(f'File already exists. Skipping file write.', 'warning')
            return None
        elif file_exists:
            print_t(f'File already exists. Contents will be overwritten.', 'info')

        if not os.path.exists(os.path.dirname(file_path)):
            print_t(f'This file write will create new directories.', 'info')

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        try:
            write_file_contents(file_path, contents)
        except BaseException as e:
            print_t(f'Failed to write file: {file_path}.', 'error')
            handle_exception(e, always_continue=True)

        return file_path
