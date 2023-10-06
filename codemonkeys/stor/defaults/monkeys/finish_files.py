from dataclasses import dataclass

from config.monkeys.monkey import OStr, OInt, OFloat, OBool, Monkey
from codemonkeys.defs import STOR_PATH


@dataclass
class FinishFiles(Monkey):

    # General
    WORK_PATH: OStr = f'{STOR_PATH}/work_path'
    FILE_TYPES_INCLUDED: OStr = ".js,.vue,.php"
    FILEPATH_MATCH_INCLUDE: OStr = None
    FILEPATH_MATCH_EXCLUDE: OStr = ".config,.md,.git,__init__.py,help.py"
    FILE_SELECT_MAX_TOKENS: OInt = 6000

    # Main Prompts
    MAIN_PROMPT: OStr = ('Read the contents of {the-file} and write'
                         ' a fully implemented version of whatever is described.')
    MAIN_PROMPT_ULTIMATUM: OStr = ('Return only the contents of a script/module that meets the requirements of'
                                   ' the description existing within {the-file}.')
    OUTPUT_EXAMPLE_PROMPT: OStr = "Make your output a well-structured and readable python script/module only."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = None
    CONTEXT_SUMMARY_PROMPT: OStr = None

    # Output Checks
    OUTPUT_CHECK_PROMPT: OStr = \
        ('Examine the following output and determine if it contains the contents of a python script/module only.'
         ' Respond with only one word: "True" or "False".')
    OUTPUT_TRIES: OInt = 1

    # Output
    OUTPUT_PATH: OStr = f"{STOR_PATH}/output"
    OUTPUT_REMOVE_STRINGS: OStr = "```python\n,```python,```"
    SKIP_EXISTING_OUTPUT_FILES: OBool = True
