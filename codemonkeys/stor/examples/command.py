from codemonkeys.entities.command import Command
from codemonkeys.types import OStr, OBool, OInt


class ExampleCommand(Command):
    """
    Define command-line interface behavior for custom commands.

    This class serves as a scaffold for creating new CLI commands within the CodeMonkeys framework.
    It specifies the CLI arguments and the command's functionality which can be tailored based on the
    developer's requirements.
    """

    # Specify args that are required (must be initialized as None)
    required_arg_keys = ['named_arg_one']

    # Specify named args
    # Passed with --name=value, passing without value sets to True
    # Do not include '--' in definition
    named_arg_keys = ['named_arg_one', 'named_arg_two']

    # Specify unnamed args (passed without --name) (define in passing order)
    unnamed_arg_keys = ['unnamed_arg_one']

    # Define and set defaults for all args (incl required)
    # Setting type-hints will provide validation in CliRunnable base class.
    named_arg_one: OStr = None
    named_arg_two: OBool = True
    unnamed_arg_one: str = 'default_value'
    unnamed_arg_two: OInt = None

    def run(self) -> None:
        """
        Execute the defined command-line interface behavior.

        This method should be implemented with the command's functionality. It will be invoked when
        the command is run from the CLI, utilizing arguments as necessary.
        """
        print(f"named_arg_one: {self.named_arg_one}")
