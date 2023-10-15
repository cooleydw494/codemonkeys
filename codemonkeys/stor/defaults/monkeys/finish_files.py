from dataclasses import dataclass

from monkeys.monkey import Monkey

from codemonkeys.defs import STOR_PATH
from codemonkeys.types import OStr


@dataclass
class FinishFiles(Monkey):

    # File Iteration
    WORK_PATH: str = f'{STOR_PATH}/work_path'
    INCLUDE_EXTS: tuple = ('.py', '.js', '.txt')
    FILEPATH_MATCH_INCLUDE: tuple = ()
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', '__init__.py', 'help.py')
    FILTER_MAX_TOKENS: int = 3500

    # Main Prompts
    MAIN_PROMPT: str = \
        'Read the contents of {the-file} and write a fully implemented version of whatever is described.'

    MAIN_PROMPT_ULTIMATUM: OStr = \
        ('Return only the contents of a script/module that meets the requirements of the description'
         ' existing within {the-file}.')

    OUTPUT_PROMPT: OStr = "Output should be nothing more than the updated file contents."

    # Output
    OUTPUT_PATH: str = f"{STOR_PATH}/output"
    SKIP_EXISTING_OUTPUT_FILES: bool = True
