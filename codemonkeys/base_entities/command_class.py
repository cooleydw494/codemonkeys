from codemonkeys.base_entities.cli_runnable_class import CliRunnable


class Command(CliRunnable):
    """
    A base class for framework/user Commands for the `monk` CLI.

    The Command class processes named and unnamed arguments and provides a `run()` method

    """

    def run(self) -> None:
        """
        This Method needs to be implemented in a user-created subclass of Command.

        :raise NotImplementedError: This error will be raised if this method is not
            implemented in a subclass of Command.

        """
        raise NotImplementedError("The run() method must be implemented in a subclass of Command.")
