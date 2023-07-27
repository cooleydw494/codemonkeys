from typing import List


class GitterError(Exception):
    def __init__(self, command: List[str], returncode: int, stdout: str, stderr: str):
        self.command = command
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self) -> str:
        return (
            f"Git command '{' '.join(self.command)}' failed with return code {self.returncode}.\n"
            f"Output: {self.stdout}\n"
            f"Error: {self.stderr}"
        )
