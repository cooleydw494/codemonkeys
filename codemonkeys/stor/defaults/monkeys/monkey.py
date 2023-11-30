from dataclasses import dataclass

from codemonkeys.defs import STOR_PATH
from codemonkeys.entities.monkey import Monkey as Base
from codemonkeys.types import OStr


@dataclass
class Monkey(Base):
    """
    A configuration entity for defining monkey behavior in the CodeMonkeys framework.

    The Monkey class holds configuration that determines the file iteration behavior,
    prompt composition, model selections, and output settings for GPT-powered
    file operations within the CodeMonkeys automation tasks.

    This class, which overrides the framework base class, can be used to set defaults for your project.
    It can also be used to extend the base class with additional properties and behavior.

    Attributes:
        WORK_PATH: The directory path where file processing will take place.
        INCLUDE_EXTS: A tuple of file extensions to include during processing.
        FILEPATH_MATCH_INCLUDE: A tuple of file patterns to specifically include during iteration.
        FILEPATH_MATCH_EXCLUDE: A tuple of file patterns to exclude during iteration.
        FILTER_MAX_TOKENS: The maximum number of tokens each file must be below to be processed.
        FILE_SELECT_PROMPT: An optional string to define a specific prompt when selecting files for processing.
        MAIN_PROMPT: The primary prompt text provided to GPT models during processing.
        MAIN_PROMPT_ULTIMATUM: An additional prompt to limit GPT responses to appropriate content.
        OUTPUT_PROMPT: A prompt that instructs GPT to specifically format the output.
        CONTEXT_FILE_PATH: An optional path for providing additional context during GPT processing.
        CONTEXT_SUMMARY_PROMPT: An optional prompt that can provide summary information for context.
        OUTPUT_PATH: The directory path where processed outputs will be stored.
        OUTPUT_EXT: The file extension for output files.
        OUTPUT_FILENAME_APPEND: An optional string to append to output filenames.
        SKIP_EXISTING_OUTPUT_FILES: A boolean that indicates whether existing output files should be skipped.
        RELATIVE_OUTPUT_PATHS: A boolean to indicate if output paths should be relative to the WORK_PATH.
        GPT_GIT_COMMITS: A boolean indicating whether GPT should make git commits after processing.
        GIT_REPO_PATH: An optional path that directs where GPT should perform git operations.
        MAIN_MODEL: The GPT model used for the main processing.
        SUMMARY_MODEL: The GPT model used for generating summaries if needed.
        FILE_SELECT_MODEL: The model used when prompting for file selection.
        MAIN_TEMP: The temperature setting for the main model processing.
        SUMMARY_TEMP: The temperature setting for summary model processing.
        FILE_SELECT_TEMP: The temperature setting for the file selection model.
        MAIN_MAX_TOKENS: The maximum token count allowed for the main processing responses.
        SUMMARY_MAX_TOKENS: The maximum token count allowed for summary responses.
        FILE_SELECT_MAX_TOKENS: The maximum token count for file selection prompts.
    """

    # File Iteration
    WORK_PATH: str = f'{STOR_PATH}/work_path'
    INCLUDE_EXTS: tuple = ('.py', '.js')
    FILEPATH_MATCH_INCLUDE: tuple = ()
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', '__init__.py')
    FILTER_MAX_TOKENS: int = 3500

    # GPT File Selection
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
    OUTPUT_FILENAME_PREPEND: OStr = None
    SKIP_EXISTING_OUTPUT_FILES: bool = True
    RELATIVE_OUTPUT_PATHS: bool = True

    # Git
    GPT_GIT_COMMITS: bool = False
    GIT_REPO_PATH: OStr = None

    # Models
    MAIN_MODEL: str = 'gpt-4-1106-preview'
    SUMMARY_MODEL: str = 'gpt-4-1106-preview'
    FILE_SELECT_MODEL: str = 'gpt-4-1106-preview'

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0
    FILE_SELECT_TEMP: float = 1.0

    # Max Tokens
    MAIN_MAX_TOKENS: int = 8000
    SUMMARY_MAX_TOKENS: int = 8000
    FILE_SELECT_MAX_TOKENS: int = 4000
