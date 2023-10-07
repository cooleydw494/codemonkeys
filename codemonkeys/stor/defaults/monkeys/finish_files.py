from dataclasses import dataclass

from config.monkeys.monkey import Monkey

from codemonkeys.defs import STOR_PATH
from codemonkeys.types import OStr


@dataclass
class FinishFiles(Monkey):

    # General
    WORK_PATH: str = f'{STOR_PATH}/work_path'
    FILE_TYPES_INCLUDED: tuple = ('.py', '.js', '.txt')
    FILEPATH_MATCH_INCLUDE: tuple = ()
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', '__init__.py', 'help.py')
    FILE_SELECT_MAX_TOKENS: int = 3500

    # Main Prompts
    MAIN_PROMPT: str = \
        'Read the contents of {the-file} and write a fully implemented version of whatever is described.'

    MAIN_PROMPT_ULTIMATUM: OStr = \
        ('Return only the contents of a script/module that meets the requirements of the description'
         ' existing within {the-file}.')

    OUTPUT_EXAMPLE_PROMPT: OStr = "Make your output a well-structured and readable python script/module only."

    # Output Checks
    OUTPUT_CHECK_PROMPT: OStr = \
        ('Examine the following output and determine if it contains the contents of a python script/module only.'
         ' Respond with only one word: "True" or "False".')
    OUTPUT_TRIES: int = 1

    # Output
    OUTPUT_PATH: str = f"{STOR_PATH}/output"
    OUTPUT_REMOVE_STRINGS: tuple = ('```python\n', '```python', '```')
    SKIP_EXISTING_OUTPUT_FILES: bool = True
