import subprocess
from typing import List

from codemonkeys.utils.git.gitter_error import GitterError
from codemonkeys.utils.misc.handle_exception import handle_exception


class Gitter:
    """
    A builder class used to interact with git repos.

    This class provides a high-level interface to execute git commands. It can be used to init, clone, pull,
    push, commit, and manage branches in a git repository.

    Attributes:
        repo_path (str): The file system path to the git repository.
    """

    def __init__(self, repo_path: str):
        """
        Initialize a Gitter instance with the specified repository path.

        :param repo_path: The file system path to the git repository.
        :type repo_path: str
        """
        self.repo_path = repo_path

    def init(self) -> str:
        """
        Initialize a new or existing git repository.

        This method creates an empty Git repository or reinitialize an existing one.

        :return: The standard output from the git init command.
        :rtype: str
        """
        return self._run_git_command(["init"])

    def clone(self, repo_url: str) -> str:
        """
        Clone a git repository from a given URL into a new directory.

        :param repo_url: The URL of the repository to clone.
        :type repo_url: str
        :return: The standard output from the git clone command.
        :rtype: str
        """
        return self._run_git_command(["clone", repo_url])

    def pull(self, remote: str = "origin", branch: str = "main") -> str:
        """
        Pull updates from a remote branch into the current branch.

        :param remote: The name of the remote repository. Defaults to 'origin'.
        :type remote: str
        :param branch: The name of the branch to pull changes from. Defaults to 'main'.
        :type branch: str
        :return: The standard output from the git pull command.
        :rtype: str
        """
        return self._run_git_command(["pull", remote, branch])

    def push(self, remote: str = "origin", branch: str = "main") -> str:
        """
        Push local changes to a remote branch.

        :param remote: The name of the remote repository. Defaults to 'origin'.
        :type remote: str
        :param branch: The name of the branch to push changes to. Defaults to 'main'.
        :type branch: str
        :return: The standard output from the git push command.
        :rtype: str
        """
        return self._run_git_command(["push", remote, branch])

    def commit(self, message: str, add_all: bool = False) -> str:
        """
        Commit staged changes to the repository with a message.

        If add_all is set to True, all changes including new files, deletions, and modifications will be staged.

        :param message: The commit message that summarizes the change.
        :type message: str
        :param add_all: If True, automatically stage all changes. Defaults to False.
        :type add_all: bool
        :return: The standard output from the git commit command.
        :rtype: str

        :raises GitterError: If the git command fails.
        """
        if add_all:
            self._run_git_command(["add", "-A"])
        return self._run_git_command(["commit", "-m", message])

    def status(self) -> str:
        """
        Check the status of the git repository.

        This method returns the current state of the repository, including staged changes, untracked files, and other statuses.

        :return: The standard output from the git status command.
        :rtype: str
        """
        return self._run_git_command(["status"])

    def checkout(self, branch_name: str) -> str:
        """
        Switch to another branch in the git repository.

        This method allows you to switch your working directory to another branch, creating it if it doesn't exist.

        :param branch_name: The name of the branch to switch to.
        :type branch_name: str
        :return: The standard output from the git checkout command.
        :rtype: str
        """
        return self._run_git_command(["checkout", branch_name])

    def create_branch(self, branch_name: str) -> str:
        """
        Create a new branch with the specified name.

        :param branch_name: The name of the new branch to create.
        :type branch_name: str
        :return: The standard output indicating successful branch creation, or an error message.
        :rtype: str
        """
        return self._run_git_command(["branch", branch_name])

    def _run_git_command(self, command: List[str]) -> str:
        """
        A private method to execute the specified git command.

        The git command is executed within the current working directory set to `self.repo_path` and its output is captured and returned.

        :param command: The git command as a list of arguments.
        :type command: List[str]
        :return: The standard output of the git command if it executes successfully.
        :rtype: str
        :raise GitterError: If the git command fails to execute properly, encapsulating detailed error info.
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
