from dataclasses import dataclass

from codemonkeys.config.monkey import Monkey as Base
from codemonkeys.types import OStr
from codemonkeys.defs import STOR_PATH


@dataclass
class Monkey(Base):
    # General
    WORK_PATH: str = f'{STOR_PATH}/work_path'
    FILE_TYPES_INCLUDED: tuple = ('.py', '.js')
    FILEPATH_MATCH_INCLUDE: tuple = ()
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', '__init__.py')
    FILE_SELECT_MAX_TOKENS: int = 3500

    # Main Prompts
    MAIN_PROMPT: str = "Please generate code for the following task..."
    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the contents of a python script, and nothing else."
    OUTPUT_EXAMPLE_PROMPT: OStr = "Limit your output to file contents, like: ```<new file contents>```."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = f"{STOR_PATH}/context/context-file.txt"
    CONTEXT_SUMMARY_PROMPT: OStr = "Provide a summary of this file..."

    # Output Checks
    OUTPUT_CHECK_PROMPT: OStr = \
        'Examine the following output and determine if it contains the contents of a python script.' \
        ' Respond with only one word: "True" or "False".'
    OUTPUT_TRIES: int = 1

    # Output
    OUTPUT_PATH: str = f"{STOR_PATH}/output"
    OUTPUT_EXT: OStr = ".py"
    OUTPUT_FILENAME_APPEND: OStr = None
    OUTPUT_REMOVE_STRINGS: tuple = ('```python\n', '```python', '```')
    SKIP_EXISTING_OUTPUT_FILES: bool = True

    # Editor
    EDITOR_PROMPT: OStr = None
    EDITOR_PROMPT_ULTIMATUM: OStr = None

    # Output Splitting
    OUTPUT_SPLIT_PATH: OStr = None
    OUTPUT_SPLIT_TAG: OStr = '[SPLIT]'

    # Git
    COMMIT_STYLE: OStr = None
    STATIC_COMMIT_MESSAGE: str = 'File updated with CodeMonkeys.'

    # Models
    MAIN_MODEL: str = 'gpt-4'
    SUMMARY_MODEL: str = 'gpt-4'
    OUTPUT_CHECK_MODEL: str = 'gpt-3.5-turbo'

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0
    OUTPUT_CHECK_TEMP: float = 0.5

    # Max Tokens
    MAIN_MAX_TOKENS: int = 8000
    SUMMARY_MAX_TOKENS: int = 8000
    OUTPUT_CHECK_MAX_TOKENS: int = 8000
