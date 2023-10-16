import subprocess
from typing import List

from codemonkeys.utils.git.gitter_error import GitterError
from codemonkeys.utils.misc.handle_exception import handle_exception


class Gitter:
    """
    A composable class used to interact with git repos.

    :param str repo_path: a string representing the path to the git repo.
    """

    def __init__(self, repo_path: str):
        """
        :param str repo_path: The path to the repo.
        """
        self.repo_path = repo_path

    def init(self) -> str:
        """
        Initializes the git repo.

        :return: The output of the git command.
        """
        return self._run_git_command(["init"])

    def clone(self, repo_url: str) -> str:
        """
        Clones the repo at the provided URL.

        :param str repo_url: The URL of the repo to clone.
        :return: The output of the git command.
        """
        return self._run_git_command(["clone", repo_url])

    def pull(self, remote: str = "origin", branch: str = "main") -> str:
        """
        Pull the latest changes from the specified remote and branch.

        :param str remote: The name of the remote repo. Default: "origin".
        :param str branch: The name of the branch to pull from. Default: "main".
        :return: The output of the git command.
        """
        return self._run_git_command(["pull", remote, branch])

    def push(self, remote: str = "origin", branch: str = "main") -> str:
        """
        Push committed changes to the specified remote and branch.

        :param str remote: The name of the remote repo. Default: "origin".
        :param str branch: The name of the branch to push to. Default: "main".
        :return: The output of the git command.
        """
        return self._run_git_command(["push", remote, branch])

    def commit(self, message: str, add_all: bool = False) -> str:
        """
        Commit changes with the provided message.
        If the add_all flag is True, stages all changes.

        :param str message: The commit message.
        :param bool add_all: Whether to stage all changes. Default: False.
        :return: The output of the git command.
        """
        if add_all:
            self._run_git_command(["add", "-A"])
        return self._run_git_command(["commit", "-m", message])

    def status(self) -> str:
        """
        Returns the status of the current repo.

        :return: The status of the current repo.
        """
        return self._run_git_command(["status"])

    def checkout(self, branch_name: str) -> str:
        """
        Switch to the specified branch.

        :param str branch_name: The name of the branch to switch to.
        :return: The output of the git command.
        """
        return self._run_git_command(["checkout", branch_name])

    def create_branch(self, branch_name: str) -> str:
        """
        Create a new branch with the provided branch name.

        :param str branch_name: The name of the new branch.
        :return: The output of the git command.
        """
        return self._run_git_command(["branch", branch_name])

    def _run_git_command(self, command: List[str]) -> str:
        """
        Runs the provided git command and returns the result.

        :param List[str] command: The git command.
        :return: The output of the git command.
        :raise GitterError: If the git command fails.
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
