class MyProjectWorkspace:

    """
    A mixin class providing a set of properties for workspace configuration.
    """

    # File Iteration
    WORK_PATH: str = "~/my_project"
    INCLUDE_EXTS: tuple = ('.py',)
    FILEPATH_MATCH_EXCLUDE: tuple = ('.git', '__')
    FILTER_MAX_TOKENS: int = 8000

    # Output
    OUTPUT_PATH: str = "~/my_project"
    SKIP_EXISTING_OUTPUT_FILES: bool = False

    # Git
    GPT_GIT_COMMITS: bool = False
    GIT_REPO_PATH: str = "~/my_project"
