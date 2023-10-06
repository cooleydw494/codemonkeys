from dataclasses import dataclass

from codemonkeys.config.monkey import OStr, OInt, OFloat, OBool, Monkey as BaseMonkey
from codemonkeys.defs import STOR_PATH


@dataclass
class Monkey(BaseMonkey):
    # TODO: replace this with a link to proper documentation once its all sorted out better

    # This file is used to set default values for Monkey configs.
    # It is also the source of truth for all Monkey config options, so if you add or alter
    # something here, it is written to the Monkey class and .env.
    # (you must update .env manually)

    # RULES
    # - Keys must be SNAKE_CASE
    # - Keys with a word-boundaried "PATH" are validated as PATH
    # - Keys with a word-boundaried "PROMPT" are validated as PROMPT
    # - Keys with a word-boundaried "MODEL" are validated as MODEL
    # - Keys with a word-boundaried "TEMP" are validated as TEMP
    # - Other keys are validated as primitives (str, bool, etc)
    #
    #   PATH values will replace 'ROOT_PATH' with your project's root path
    #
    # - Validation logic is defined in
    #   `modules/source/config/monkey_validations.py`

    # General
    WORK_PATH: OStr = f'{STOR_PATH}/work_path'
    FILE_TYPES_INCLUDED: OStr = ".js,.vue,.php"
    FILEPATH_MATCH_INCLUDE: OStr = None
    FILEPATH_MATCH_EXCLUDE: OStr = ".config,.md,.git,__init__.py"
    FILE_SELECT_MAX_TOKENS: OInt = 3000

    # Main Prompts
    MAIN_PROMPT: OStr = "Please generate code for the following task..."
    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the contents of a python script, and nothing else."
    OUTPUT_EXAMPLE_PROMPT: OStr = "Limit your output to file contents, like: ```<new file contents>```."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = f"{STOR_PATH}/context/context-file.txt"
    CONTEXT_SUMMARY_PROMPT: OStr = "Provide a summary of this file..."

    # Output Checks
    OUTPUT_CHECK_PROMPT: OStr = \
        'Examine the following output and determine if it contains the contents of a python script.' \
        ' Respond with only one word: "True" or "False".'
    OUTPUT_TRIES: OInt = 1

    # Output
    OUTPUT_PATH: OStr = f"{STOR_PATH}/output"
    OUTPUT_EXT: OStr = ".py"
    OUTPUT_FILENAME_APPEND: OStr = None
    OUTPUT_REMOVE_STRINGS: OStr = "```python\n,```python,```"
    SKIP_EXISTING_OUTPUT_FILES: OBool = True

    # Editor
    EDITOR_PROMPT: OStr = None
    EDITOR_PROMPT_ULTIMATUM: OStr = None

    # Output Splitting
    OUTPUT_SPLIT_PATH: OStr = None
    OUTPUT_SPLIT_TAG: OStr = '[SPLIT]'

    # Git
    COMMIT_STYLE: OStr = None
    STATIC_COMMIT_MESSAGE: OStr = 'File updated with CodeMonkeys.'

    # Models
    MAIN_MODEL: OStr = 'gpt-4'
    SUMMARY_MODEL: OStr = 'gpt-4'
    OUTPUT_CHECK_MODEL: OStr = 'gpt-3.5-turbo'

    # Temps
    MAIN_TEMP: OFloat = 1.0
    SUMMARY_TEMP: OFloat = 1.0
    OUTPUT_CHECK_TEMP: OFloat = 0.5

    # Max Tokens
    MAIN_MAX_TOKENS: OInt = 8000
    SUMMARY_MAX_TOKENS: OInt = 8000
    OUTPUT_CHECK_MAX_TOKENS: OInt = 8000
