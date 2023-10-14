import os

from codemonkeys.defs import nl2, nl
from codemonkeys.entities.func import Func
from codemonkeys.utils.file_ops import write_file_contents
from codemonkeys.utils.monk.theme_functions import print_t, input_t


class WriteFiles(Func):

    """
    This Func is intended to be used to handle the result of prompts that ask GPT to write a file or files.
    Unlike FinalizeOutput, this Func does not return file contents, but directly writes the files itself.
    An example of an advanced use-case: Asking GPT to scaffold a project based on an architecture template.
    Because of the risky nature of automated file writing, user will be prompted to confirm each file.
    """

    name: str = 'write_files'

    _description: str = 'Writes files to disk to fulfill the requirements of a prompt.'

    _parameters: dict = {
        "type": "object",
        "properties": {
            "files_data": {
                "type": "array",
                "description": "Array of file data objects",
                "items": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Absolute filepath (relative not supported)",
                        },
                        "file_contents": {
                            "type": "string",
                            "description": "The file contents",
                        }
                    },
                    "required": ["file_path", "file_contents"],
                },
            },
        },
        "required": ["files_data"],
    }

    @classmethod
    def __execute(cls, files_data: list) -> list[str]:

        written_filepaths = []

        for file_data in files_data:
            file_path = os.path.expanduser(file_data['file_path'])
            file_contents = file_data['file_contents']

            print_t(f'Preparing to write file to {file_path} with contents:{nl2}{file_contents}{nl}')

            if os.path.exists(file_path):
                print_t(f'File already exists. Contents will be overwritten.', 'info')

            if not os.path.exists(os.path.dirname(file_path)):
                print_t(f'This file write will create new directories.', 'info')

            user_input = input_t(f'Confirm file write?', '(y/n)')
            if user_input.lower() != 'y':
                print_t(f'Skipping file write.', 'warning')
                continue

            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            try:
                write_file_contents(file_path, file_contents)
                written_filepaths.append(file_path)
            except Exception as e:
                print_t(f'File write failed: {e}', 'error')

        return written_filepaths
