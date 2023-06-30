from codemonkeys.base_entitiies.utils.cli_runnable_class import CliRunnable


class Command(CliRunnable):
    """
    Command is a base class for framework and user-created Commands for the `monk` CLI.
    It processes named and unnamed arguments and provides a `main` method to be implemented.
    Run `monk make <name>` to create a new command.
    """

    def run(self):
        raise NotImplementedError("The main() method must be implemented in a subclass of Automation.")
