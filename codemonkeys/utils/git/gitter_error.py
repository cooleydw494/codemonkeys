from typing import List


class GitterError(Exception):
    """
    Custom exception for Gitter errors.

    :param List[str] command: A list of command tokens.
    :param int returncode: The exit status of the command.
    :param str stdout: The output from the command.
    :param str stderr: The error _message from the command.
    """

    def __init__(self, command: List[str], returncode: int, stdout: str, stderr: str):
        """
        Initialize GitterError with command details, return code and system output.
        
        :param List[str] command: A list of command tokens.
        :param int returncode: The exit status of the command.
        :param str stdout: The output from the command.
        :param str stderr: The error _message from the command.
        """
        self.command = command
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self) -> str:
        """
        Return a formatted string with error information.

        :return: The string representation of the GitterError.
        """
        return (
            f"Git command '{' '.join(self.command)}' failed with return code {self.returncode}.\n"
            f"Output: {self.stdout}\n"
            f"Error: {self.stderr}"
        )
