class MyProjectWorkspace:

    """
    A mixin class providing a set of properties for workspace configuration.

    This mixin is designed to define workspace-related properties that are shared across
    multiple Monkey configurations. It centralizes the configuration for ease of management
    and consistency. Properties defined here override the default settings in Monkeys
    where the mixin is applied, unless explicitly overridden in the Monkey itself.

    Example:
        To apply this workspace configuration to a Monkey, simply include MyProjectWorkspace in the mixins tuple:

        .. code-block:: python

            from monkeys.monkey import Monkey
            from mixins.MyProjectWorkspace import MyProjectWorkspace

            class MyMonkey(Monkey):
                mixins = (MyProjectWorkspace,)

                # Other properties and methods
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
