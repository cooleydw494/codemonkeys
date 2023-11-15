from codemonkeys.entities.cli_runnable import CliRunnable


class Command(CliRunnable):
    """
    A base class for framework/user Commands for the `monk` CLI.

    The Command class processes named and unnamed arguments and provides a `run()` method that derived classes must
    implement to execute command-specific logic. The class manages CLI arguments, passing them from `argparse` to the
    constructor and allowing subclasses to define argument handling through class variables.
    """

    def run(self) -> None:
        """
        This Method needs to be implemented in a user-created subclass of Command.

        This abstract method defines the execution behavior of a Command when called from the `monk` CLI. Subclasses
        must provide specific implementations, detailing the operational logic corresponding to the command.

        :raise NotImplementedError: This error will be raised if this method is not
            implemented in a subclass of Command.

        """
        raise NotImplementedError("The run() method must be implemented in a subclass of Command.")
