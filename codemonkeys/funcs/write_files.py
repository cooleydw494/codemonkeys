import os

from codemonkeys.defs import nl2, nl
from codemonkeys.entities.func import Func
from codemonkeys.types import OStr
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

    _description: str = 'This function handles writing files to disk to fulfill the requirements of a prompt.'

    _parameters: dict = {
        "type": "object",
        "properties": {
            "files_data": {
                "type": "array",
                "description": "An array of objects with the following properties: file_path and file_contents.",
            },
            "root_path": {
                "type": "string",
                "description": "The root path to append the file_path within files_data for each file. Required if "
                               "files_data does not include absolute paths.",
            }
        },
        "required": ["files_data"],
    }

    @classmethod
    def _execute(cls, files_data: list, root_path: OStr = None) -> str:
        # note: don't forget to prompt user to confirm each file write
        for file_data in files_data:
            file_path = file_data['file_path']
            file_contents = file_data['file_contents']
            if root_path is not None:
                file_path = os.path.join(root_path, file_path)

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
            write_file_contents(file_path, file_contents)
            return file_path
