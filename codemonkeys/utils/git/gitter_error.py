class GitterError(Exception):
    def __init__(self, command, returncode, stdout, stderr):
        self.command = command
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        return (
            f"Git command '{' '.join(self.command)}' failed with return code {self.returncode}.\n"
            f"Output: {self.stdout}\n"
            f"Error: {self.stderr}"
        )
