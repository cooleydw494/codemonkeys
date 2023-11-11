from dataclasses import dataclass

from codemonkeys.defs import STOR_PATH
from codemonkeys.entities.monkey import Monkey as Base
from codemonkeys.types import OStr


@dataclass
class Monkey(Base):

    # File Iteration
    WORK_PATH: str = f'{STOR_PATH}/work_path'
    INCLUDE_EXTS: tuple = ('.py', '.js')
    FILEPATH_MATCH_INCLUDE: tuple = ()
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', '__init__.py')
    FILTER_MAX_TOKENS: int = 3500
    FILE_SELECT_PROMPT: OStr = None

    # Main Prompts
    MAIN_PROMPT: str = "Please generate code for the following task..."
    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the contents of a python script, and nothing else."
    OUTPUT_PROMPT: OStr = "Output should be nothing more than the updated file contents."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = None
    CONTEXT_SUMMARY_PROMPT: OStr = None

    # Output
    OUTPUT_PATH: str = f"{STOR_PATH}/output"
    OUTPUT_EXT: OStr = ".py"
    OUTPUT_FILENAME_APPEND: OStr = None
    SKIP_EXISTING_OUTPUT_FILES: bool = True
    RELATIVE_OUTPUT_PATHS: bool = True

    # Git
    GPT_GIT_COMMITS: bool = False
    GIT_REPO_PATH: OStr = None

    # Models
    MAIN_MODEL: str = 'gpt-4'
    SUMMARY_MODEL: str = 'gpt-4'
    FILE_SELECT_MODEL: str = 'gpt-4'

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0
    FILE_SELECT_TEMP: float = 1.0

    # Max Tokens
    MAIN_MAX_TOKENS: int = 8000
    SUMMARY_MAX_TOKENS: int = 8000
    FILE_SELECT_MAX_TOKENS: int = 8000
