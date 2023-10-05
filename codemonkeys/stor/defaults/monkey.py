from dataclasses import dataclass
from typing import Optional

from codemonkeys.config.monkey import Monkey as BaseMonkey


@dataclass
class Monkey(BaseMonkey):

    # General
    WORK_PATH: Optional[str] = None
    FILE_TYPES_INCLUDED: Optional[str] = None
    FILEPATH_MATCH_INCLUDE: Optional[str] = None
    FILEPATH_MATCH_EXCLUDE: Optional[str] = None
    FILE_SELECT_MAX_TOKENS: Optional[int] = None

    # Main Prompts
    MAIN_PROMPT: Optional[str] = None
    MAIN_PROMPT_ULTIMATUM: Optional[str] = None
    OUTPUT_EXAMPLE_PROMPT: Optional[str] = None

    # Context / Summary
    CONTEXT_FILE_PATH: Optional[str] = None
    CONTEXT_SUMMARY_PROMPT: Optional[str] = None

    # Output Checks
    OUTPUT_CHECK_PROMPT: Optional[str] = None
    OUTPUT_TRIES: Optional[int] = None

    # Output
    OUTPUT_PATH: Optional[str] = None
    OUTPUT_EXT: Optional[str] = None
    OUTPUT_FILENAME_APPEND: Optional[str] = None
    OUTPUT_REMOVE_STRINGS: Optional[str] = None
    SKIP_EXISTING_OUTPUT_FILES: Optional[bool] = None

    # Editor
    EDITOR_PROMPT: Optional[str] = None
    EDITOR_PROMPT_ULTIMATUM: Optional[str] = None

    # Output Splitting
    OUTPUT_SPLIT_PATH: Optional[str] = None
    OUTPUT_SPLIT_TAG: Optional[str] = None

    # Git
    COMMIT_STYLE: Optional[str] = None
    STATIC_COMMIT_MESSAGE: Optional[str] = None

    # Models
    MAIN_MODEL: Optional[str] = None
    SUMMARY_MODEL: Optional[str] = None
    OUTPUT_CHECK_MODEL: Optional[str] = None

    # Temps
    MAIN_TEMP: Optional[float] = None
    SUMMARY_TEMP: Optional[float] = None
    OUTPUT_CHECK_TEMP: Optional[float] = None

    # Max Tokens
    MAIN_MAX_TOKENS: Optional[int] = None
    SUMMARY_MAX_TOKENS: Optional[int] = None
    OUTPUT_CHECK_MAX_TOKENS: Optional[int] = None
