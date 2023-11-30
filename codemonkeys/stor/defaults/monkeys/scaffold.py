from monkeys.monkey import Monkey
from codemonkeys.defs import STOR_PATH
from mixins.my_project_workspace import MyProjectWorkspace


class Scaffold(Monkey):
    """
    Monkey subclass for scaffolding a codebase from architectural documentation.

    This Monkey automates the creation of a file structure based on an architectural
    overview of a codebase. It generates a list of required filepaths to be created and
    suggests the best implementation for specified files.
    """

    mixins = (
        MyProjectWorkspace,
    )

    # Filepath Extraction
    FILE_SELECT_PROMPT: str = ("Review the following architectural documentation for a codebase and extract a list "
                               "of all the filepaths that need to be created to scaffold it. Always use absolute "
                               f"paths, beginning with this fully qualified root path: {MyProjectWorkspace.OUTPUT_PATH}.")

    # Main Prompts
    MAIN_PROMPT: str = ("Review the following architectural documentation for a codebase, and write the best "
                        "implementation of the specified file as possible, with close attention to other usable "
                        "elements declared in the architecture overview (classes, functions, etc).")

    MAIN_PROMPT_ULTIMATUM: str = ("Take your time carefully considering architecture information and how it affects "
                                  "implementation of each file, ensuring among other things, that naming and imports "
                                  "are correct.")

    # Context / Summary
    CONTEXT_FILE_PATH: str = f"{STOR_PATH}/context/scaffold-architecture.txt"
