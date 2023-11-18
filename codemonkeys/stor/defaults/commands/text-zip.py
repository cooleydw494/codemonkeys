import fnmatch
import os
import time
import zipfile
from typing import Dict, Any, List

from codemonkeys.defs import TEMP_PATH
from codemonkeys.entities.command import Command
from codemonkeys.utils.monk.theme_functions import print_t


class TextZip(Command):

    required_arg_keys = ['dir']
    unnamed_arg_keys = ['dir']
    dir: str

    text_extensions = [
        '.txt', '.py', '.js', '.html', '.scss', '.css', '.md', '.json',
        '.yml', '.yaml', '.php', '.config', '.vue',
    ]

    excluded_dirs = [
        'node_modules', 'vendor', 'codemonkeys.egg-info', 'public', 'tests', '.github'
    ]

    excluded_files = [
        '.env*', '*.xml', '*.lock', '__init__.py', '.*',
    ]

    def __init__(self, named_args: Dict[str, Any], unnamed_args: List[str]):
        super().__init__(named_args, unnamed_args)

        self.dir = os.path.expanduser(self.dir)
        dir_name = os.path.basename(self.dir)
        timestamp = int(time.time())
        self.zip_filepath = os.path.expanduser(f'{TEMP_PATH}/{dir_name}-{timestamp}.zip')

    def run(self):
        os.makedirs(os.path.dirname(self.zip_filepath), exist_ok=True)

        with zipfile.ZipFile(self.zip_filepath, 'w') as zipf:
            for root, dirs, files in os.walk(self.dir):
                # Exclude directories
                dirs[:] = [d for d in dirs if d not in self.excluded_dirs]
                for file in files:
                    if any(fnmatch.fnmatch(file, pattern) for pattern in self.excluded_files):
                        continue
                    if self.is_text_file(file):
                        file_path = os.path.join(root, file)
                        # Add file to zip
                        zipf.write(file_path, os.path.relpath(file_path, self.dir))

        print_t(f"Zip file created: {self.zip_filepath}", 'info')
        os.system(f'open -R "{self.zip_filepath}"')

    def is_text_file(self, filepath):
        return os.path.splitext(filepath)[1].lower() in self.text_extensions
