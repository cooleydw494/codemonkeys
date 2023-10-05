from dataclasses import dataclass
from typing import Optional

from codemonkeys.config.monkey_config import MonkeyConfig as CMMonkeyConfig


@dataclass
class MonkeyConfig(CMMonkeyConfig):

    WORK_PATH: Optional[str] = None
    FILE_TYPES_INCLUDED: Optional[str] = None
    FILEPATH_MATCH_INCLUDE: Optional[str] = None
    FILEPATH_MATCH_EXCLUDE: Optional[str] = None
    FILE_SELECT_MAX_TOKENS: Optional[int] = None
    MAX_TOKENS: Optional[int] = None
    MAIN_PROMPT: Optional[str] = None
    MAIN_PROMPT_ULTIMATUM: Optional[str] = None
    OUTPUT_EXAMPLE_PROMPT: Optional[str] = None
    CONTEXT_FILE_PATH: Optional[str] = None
    CONTEXT_SUMMARY_PROMPT: Optional[str] = None
    OUTPUT_CHECK_PROMPT: Optional[str] = None
    OUTPUT_TRIES: Optional[int] = None
    OUTPUT_PATH: Optional[str] = None
    OUTPUT_EXT: Optional[str] = None
    OUTPUT_FILENAME_APPEND: Optional[str] = None
    OUTPUT_REMOVE_STRINGS: Optional[str] = None
    SKIP_EXISTING_OUTPUT_FILES: Optional[bool] = None
    EDITOR_PROMPT: Optional[str] = None
    EDITOR_PROMPT_ULTIMATUM: Optional[str] = None
    OUTPUT_SPLIT_PATH: Optional[str] = None
    OUTPUT_SPLIT_TAG: Optional[str] = None
    COMMIT_STYLE: Optional[str] = None
    STATIC_COMMIT_MESSAGE: Optional[str] = None
    MAIN_MODEL: Optional[str] = None
    SUMMARY_MODEL: Optional[str] = None
    OUTPUT_CHECK_MODEL: Optional[str] = None
    MAIN_TEMP: Optional[float] = None
    SUMMARY_TEMP: Optional[float] = None
    OUTPUT_CHECK_TEMP: Optional[float] = None
    MAIN_MAX_TOKENS: Optional[int] = None
    SUMMARY_MAX_TOKENS: Optional[int] = None
    OUTPUT_CHECK_MAX_TOKENS: Optional[int] = None
