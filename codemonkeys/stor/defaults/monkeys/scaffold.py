from dataclasses import dataclass

from codemonkeys.defs import STOR_PATH

from monkeys.monkey import Monkey

from codemonkeys.types import OStr


@dataclass
class Scaffold(Monkey):

    # Main Prompts
    MAIN_PROMPT: str = ("Review the following architectural documentation for a codebase, and write the best "
                        "implementation of the specified file as possible, with close attention to other usable"
                        " elements declared in the architecture overview (classes, functions, etc).")

    # Context / Summary
    CONTEXT_FILE_PATH: str = f"{STOR_PATH}/context/scaffold.txt"

    # Project Root Dir
    PROJECT_ROOT: str = '~/local-git/twitter_poster'

    # Filepath Extraction
    FILE_SELECT_PROMPT: str = ("Review the following architectural documentation for a codebase and extract a list "
                                   "of all the filepaths that need to be created to scaffold it. Use absolute paths, "
                                   f"with the project root dir {PROJECT_ROOT}.")

    # Output
    SKIP_EXISTING_OUTPUT_FILES = True

    # Git
    GPT_GIT_COMMITS: bool = False
    GIT_REPO_PATH: OStr = None

    # Models
    MAIN_MODEL: str = 'gpt-4'
    FILE_SELECT_MODEL: str = 'gpt-4'

    # Temps
    MAIN_TEMP: float = 1.0
    FILE_SELECT_TEMP: float = 0.8

    # Max Tokens
    MAIN_MAX_TOKENS: int = 6000
    FILE_SELECT_MAX_TOKENS: int = 3000
