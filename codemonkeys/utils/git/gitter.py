import subprocess

from codemonkeys.utils.git.gitter_error import GitterError


class Gitter:

    def __init__(self, repo_path):
        self.repo_path = repo_path

    def _run_git_command(self, command):
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

    def clone(self, repo_url):
        return self._run_git_command(["clone", repo_url])

    def pull(self, remote="origin", branch="master"):
        return self._run_git_command(["pull", remote, branch])

    def push(self, remote="origin", branch="master"):
        return self._run_git_command(["push", remote, branch])

    def commit(self, message, add_all=False):
        if add_all:
            self._run_git_command(["add", "-A"])
        return self._run_git_command(["commit", "-m", message])

    def status(self):
        return self._run_git_command(["status"])

    def checkout(self, branch_name):
        return self._run_git_command(["checkout", branch_name])

    def create_branch(self, branch_name):
        return self._run_git_command(["branch", branch_name])
