import os

from codemonkeys.defs import nl2, nl
from codemonkeys.entities.func import Func
from codemonkeys.types import OStr
from codemonkeys.utils.misc.file_ops import write_file_contents
from codemonkeys.utils.monk.theme_functions import print_t


class WriteFile(Func):

    """
    This Func is a single-file-only version of WriteFiles.
    """

    name: str = 'write_file'

    _description: str = 'Writes a single file to disk to fulfill the requirements of a prompt.'

    _parameters: dict = {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Absolute filepath (relative not supported)",
            },
            "contents": {
                "type": "string",
                "description": "Complete file contents",
            }
        },
        "required": ["filepath", "contents"],
    }

    @classmethod
    def __execute(cls, path: str, contents: str) -> OStr:

        file_path = os.path.expanduser(path)

        print_t(f'Preparing to write file to {file_path} with contents:{nl2}{contents}{nl}')

        if os.path.exists(file_path):
            print_t(f'File already exists. Contents will be overwritten.', 'info')

        if not os.path.exists(os.path.dirname(file_path)):
            print_t(f'This file write will create new directories.', 'info')

        # user_input = input_t(f'Confirm file write?', '(y/n)')
        # if user_input.lower() != 'y':
        #     print_t(f'Skipping file write.', 'warning')
        #     return None

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        try:
            write_file_contents(file_path, contents)
        except Exception as e:
            print_t(f'File write failed: {e}', 'error')

        return file_path
