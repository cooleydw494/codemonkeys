from typing import Union

from codemonkeys.entities.command import Command


class ExampleCommand(Command):
    """
    Use this class to define CLI arguments, requirements, etc (look at Command and CliRunnable for more info).
    Of course, use the run() method to implement the Command functionality.
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
    named_arg_one: str = None
    named_arg_two: bool = True
    unnamed_arg_one: str = 'default_value'
    unnamed_arg_two: Union[int, None] = None

    def run(self) -> None:
        """
        Execute your Command logic here,, utilizing args as needed.
        """
        print(f"named_arg_one: {self.named_arg_one}")
