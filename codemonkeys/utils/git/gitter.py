import subprocess
from typing import List

from codemonkeys.utils.git.gitter_error import GitterError


class Gitter:

    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def clone(self, repo_url: str) -> str:
        return self._run_git_command(["clone", repo_url])

    def pull(self, remote: str = "origin", branch: str = "master") -> str:
        return self._run_git_command(["pull", remote, branch])

    def push(self, remote: str = "origin", branch: str = "master") -> str:
        return self._run_git_command(["push", remote, branch])

    def commit(self, message: str, add_all: bool = False) -> str:
        if add_all:
            self._run_git_command(["add", "-A"])
        return self._run_git_command(["commit", "-m", message])

    def status(self) -> str:
        return self._run_git_command(["status"])

    def checkout(self, branch_name: str) -> str:
        return self._run_git_command(["checkout", branch_name])

    def create_branch(self, branch_name: str) -> str:
        return self._run_git_command(["branch", branch_name])

    def _run_git_command(self, command: List[str]) -> str:
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
            raise GitterError(command, e.returncode, e.stdout, e.stderr)