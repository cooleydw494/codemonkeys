import subprocess
from typing import List

from codemonkeys.utils.git.gitter_error import GitterError
from codemonkeys.utils.misc.handle_exception import handle_exception


class Gitter:
    """
    A utility class for interacting with Git repositories.

    Provides methods for common Git operations such as initializing, cloning, pulling, pushing, and committing to a
    repository. It is designed to encapsulate the command-line interface of Git and expose it through a user-friendly
    Python interface.

    Attributes:
        repo_path (str): The filesystem path to the Git repository.

    Example:
        >>> gitter = Gitter(repo_path='/path/to/repo')
        >>> gitter.status()
        'On branch master\nYour branch is up to date with 'origin/master'.\n\nnothing to commit, working tree clean'
    """

    def __init__(self, repo_path: str):
        """
        Initialize the Gitter instance for a given repository path.

        :param repo_path: The filesystem path to the Git repository.
        :type repo_path: str
        """
        self.repo_path = repo_path

    def init(self) -> str:
        """
        Initialize a new or reinitialize an existing Git repository.

        This method sets up the necessary Git files and directories, if not already present.

        :return: The standard output from the Git 'init' command.
        :rtype: str
        """
        return self._run_git_command(["init"])

    def clone(self, repo_url: str) -> str:
        """
        Clone a Git repository from the specified URL.

        This method will create a local copy of the remote repository provided by 'repo_url'.

        :param repo_url: The URL of the Git repository to clone.
        :type repo_url: str
        :return: The standard output from the Git 'clone' command.
        :rtype: str
        """
        return self._run_git_command(["clone", repo_url])

    def pull(self, remote: str = "origin", branch: str = "main") -> str:
        """
        Update the local working copy from the specified remote branch.

        This method fetches and merges changes from the remote 'branch' of 'remote'.

        :param remote: The name of the remote repository. Defaults to 'origin'.
        :type remote: str
        :param branch: The name of the branch to pull changes from. Defaults to 'main'.
        :type branch: str
        :return: The standard output from the Git 'pull' command.
        :rtype: str
        """
        return self._run_git_command(["pull", remote, branch])

    def push(self, remote: str = "origin", branch: str = "main") -> str:
        """
        Push local commits to the specified remote branch.

        This method sends the local branch commits to the 'branch' of 'remote'.

        :param remote: The name of the remote repository. Defaults to 'origin'.
        :type remote: str
        :param branch: The name of the branch to push changes to. Defaults to 'main'.
        :type branch: str
        :return: The standard output from the Git 'push' command.
        :rtype: str
        """
        return self._run_git_command(["push", remote, branch])

    def commit(self, message: str, add_all: bool = False) -> str:
        """
        Commit staged changes to the repository with the specified message.

        If 'add_all' is True, stages all changes including untracked files before committing.

        :param message: The commit message to use.
        :type message: str
        :param add_all: If True, stages all changes. Defaults to False.
        :type add_all: bool
        :return: The standard output from the Git 'commit' command.
        :rtype: str
        :raises GitterError: If the Git command fails.
        """
        if add_all:
            self._run_git_command(["add", "-A"])
        return self._run_git_command(["commit", "-m", message])

    def status(self) -> str:
        """
        Retrieve the current status of the Git repository.

        This method displays the working tree status, showing staged, unstaged, and untracked changes.

        :return: The standard output from the Git 'status' command.
        :rtype: str
        """
        return self._run_git_command(["status"])

    def checkout(self, branch_name: str) -> str:
        """
        Switch to the specified branch in the repository.

        This method changes the active branch in the local repository to 'branch_name'.

        :param branch_name: The name of the branch to check out.
        :type branch_name: str
        :return: The standard output from the Git 'checkout' command.
        :rtype: str
        """
        return self._run_git_command(["checkout", branch_name])

    def create_branch(self, branch_name: str) -> str:
        """
        Create a new branch in the repository with the given name.

        :param branch_name: The name of the branch to create.
        :type branch_name: str
        :return: The standard output or error message resulting from branch creation.
        :rtype: str

        :raises GitterError: If creation of the branch fails.
        """
        return self._run_git_command(["branch", branch_name])

    def _run_git_command(self, command: List[str]) -> str:
        """
        Run git command and return its output.

        This private method runs a Git command and returns its output or raises an exception in case of an error.

        :param command: The Git command to run, as a list of arguments.
        :type command: List[str]
        :return: The output of the Git command execution.
        :rtype: str

        :raises GitterError: If there's a problem running the Git command.
        """
        try:
            result = subprocess.run(
                ["git"] + command,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            handle_exception(GitterError(command, e.returncode, e.stdout, e.stderr))
