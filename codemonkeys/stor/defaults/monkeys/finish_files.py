from monkeys.monkey import Monkey

from codemonkeys.defs import STOR_PATH
from codemonkeys.types import OStr


class FinishFiles(Monkey):
    """
    Automation Monkey for finishing incomplete file contents.

    This Monkey is designed to read the contents of files and generate a fully implemented
    version of the described functionalities within them. It focuses on specific file extensions
    and excludes certain path patterns to tailor the finishing process.
    """

    # File Iteration
    WORK_PATH: str = f'{STOR_PATH}/work_path'
    INCLUDE_EXTS: tuple = ('.py', '.js', '.txt')
    FILEPATH_MATCH_INCLUDE: tuple = ()
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', '__init__.py', 'help.py')
    FILTER_MAX_TOKENS: int = 4000

    # Main Prompts
    MAIN_PROMPT: str = "Read the contents of {the-file} and write a fully implemented version of whatever is described."

    MAIN_PROMPT_ULTIMATUM: OStr = ('Return only the contents of a script/module that meets the requirements of the '
                                   'description existing within {the-file}.')

    OUTPUT_PROMPT: OStr = "Output should be nothing more than the updated file contents."

    # Output
    OUTPUT_PATH: str = f"{STOR_PATH}/output"
    SKIP_EXISTING_OUTPUT_FILES: bool = False
