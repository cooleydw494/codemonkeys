from dataclasses import dataclass

from codemonkeys.config.monkey_config import MonkeyConfig as CMMonkeyConfig


@dataclass
class MonkeyConfig(CMMonkeyConfig):

    # DO NOT MODIFY - generated from monkey-config-defaults.
    # [MONKEY_CONFIG_PROPS_START]
    from types import NoneType
    from typing import Optional

    from dataclasses import field
    WORK_PATH: Optional[str] = field(default=None)
    FILE_TYPES_INCLUDED: Optional[str] = field(default=None)
    FILEPATH_MATCH_INCLUDE: Optional[NoneType] = field(default=None)
    FILEPATH_MATCH_EXCLUDE: Optional[str] = field(default=None)
    FILE_SELECT_MAX_TOKENS: Optional[int] = field(default=None)
    MAIN_PROMPT: Optional[str] = field(default=None)
    MAIN_PROMPT_ULTIMATUM: Optional[str] = field(default=None)
    OUTPUT_EXAMPLE_PROMPT: Optional[str] = field(default=None)
    CONTEXT_FILE_PATH: Optional[NoneType] = field(default=None)
    CONTEXT_SUMMARY_PROMPT: Optional[NoneType] = field(default=None)
    OUTPUT_CHECK_PROMPT: Optional[NoneType] = field(default=None)
    OUTPUT_TRIES: Optional[int] = field(default=None)
    OUTPUT_PATH: Optional[str] = field(default=None)
    OUTPUT_EXT: Optional[str] = field(default=None)
    OUTPUT_FILENAME_APPEND: Optional[str] = field(default=None)
    OUTPUT_REMOVE_STRINGS: Optional[str] = field(default=None)
    SKIP_EXISTING_OUTPUT_FILES: Optional[bool] = field(default=None)
    EDITOR_PROMPT: Optional[NoneType] = field(default=None)
    EDITOR_PROMPT_ULTIMATUM: Optional[NoneType] = field(default=None)
    OUTPUT_SPLIT_PATH: Optional[NoneType] = field(default=None)
    OUTPUT_SPLIT_TAG: Optional[str] = field(default=None)
    COMMIT_STYLE: Optional[NoneType] = field(default=None)
    STATIC_COMMIT_MESSAGE: Optional[str] = field(default=None)
    MAIN_MODEL: Optional[str] = field(default=None)
    SUMMARY_MODEL: Optional[str] = field(default=None)
    OUTPUT_CHECK_MODEL: Optional[str] = field(default=None)
    MAIN_TEMP: Optional[float] = field(default=None)
    SUMMARY_TEMP: Optional[float] = field(default=None)
    OUTPUT_CHECK_TEMP: Optional[float] = field(default=None)
    MAIN_MAX_TOKENS: Optional[int] = field(default=None)
    SUMMARY_MAX_TOKENS: Optional[int] = field(default=None)
    OUTPUT_CHECK_MAX_TOKENS: Optional[int] = field(default=None)
    # [MONKEY_CONFIG_PROPS_END]
