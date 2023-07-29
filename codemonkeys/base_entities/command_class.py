from codemonkeys.base_entities.utils.cli_runnable_class import CliRunnable


class Command(CliRunnable):
    """
    A base class for framework and user-created Commands for the `monk` CLI.

    The Command class processes named and unnamed arguments and provides a
    `main` method to be implemented within it.

    """

    def run(self) -> None:
        """
        This Method needs to be implemented in a user-created subclass of Command.

        :raises NotImplementedError: This error will be raised if this method is not
            implemented in a subclass of Command.

        """
        raise NotImplementedError("The run() method must be implemented in a subclass of Command.")
