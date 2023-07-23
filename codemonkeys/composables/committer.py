import difflib

from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.defs import nl, nl2
from codemonkeys.utils.git.gitter import Gitter


def diff_content(old_content, new_content):
    return nl.join(list(difflib.unified_diff(old_content, new_content)))


class Committer:
    gitter: Gitter | None = None
    gpt_client: GPTClient | None = None
    model: str = '3'
    temp: float = 0.75
    max_tokens: int = 32000
    prompt: str | None = None
    message: str | None = None

    def __init__(self, repo_path: str):
        self.gitter = Gitter(repo_path)
        self.gpt_client = GPTClient(self.model, self.temp, self.max_tokens)

    def set_model(self, model, temp: float = None, max_tokens: int = None):
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        self.gpt_client = GPTClient(self.model, self.temp, self.max_tokens)
        return self

    def set_prompt(self, prompt: str):
        self.prompt = prompt
        return self

    def set_message(self, commit_message: str):
        self.message = commit_message
        return self

    def set_message_via_content(self, old_content: str, new_content: str):
        diff = diff_content(old_content.splitlines(), new_content.splitlines())
        prompt = f"{self.prompt or 'Write a commit message for the following changes:'}{nl2}```{nl}{diff}{nl}```{nl2}"
        prompt += "[Ultimatum: Limit your response to only the git message, including nothing else.]"
        self.message = self.gpt_client.generate(prompt)
        return self.message

    def get_message(self) -> str | None:
        return self.message

    def commit(self):
        self.gitter.commit(self.message, add_all=True)
