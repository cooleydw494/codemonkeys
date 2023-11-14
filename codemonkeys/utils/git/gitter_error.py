from typing import List


class GitterError(BaseException):
    """
    Custom exception for Gitter errors.

    This exception is raised when a git-related command executed by Gitter encounters an error.
    It encapsulates details about the command, its exit status, and the output or error message produced.

    :param command: A list of command tokens representing the git command executed.
    :type command: List[str]
    :param returncode: The exit status of the command.
    :type returncode: int
    :param stdout: The output from the command.
    :type stdout: str
    :param stderr: The error message from the command.
    :type stderr: str
    """

    def __init__(self, command: List[str], returncode: int, stdout: str, stderr: str):
        """
        Initialize GitterError with command details, return code, and system output.

        :param command: A list of command tokens.
        :param returncode: The exit status of the command.
        :param stdout: The output from the command.
        :param stderr: The error message from the command.
        """
        self.command = command
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self) -> str:
        """
        Return a formatted string with error information.

        :return: The string representation of the GitterError.
        :rtype: str
        """
        return (
            f"Git command '{' '.join(self.command)}' failed with return code {self.returncode}.\n"
            f"Output: {self.stdout}\n"
            f"Error: {self.stderr}"
        )
