import difflib
from typing import Sequence

from codemonkeys.defs import nl, nl2
from codemonkeys.utils.git.gitter import Gitter
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t


def diff_content(old_content: Sequence[str], new_content: Sequence[str]) -> str:
    """
    Generates a unified diff between old_content and new_content.

    :param Sequence[str] old_content: The original content.
    :param Sequence[str] new_content: The updated content.
    :return: The unified diff as a string.
    """
    return nl.join(list(difflib.unified_diff(old_content, new_content)))


class Committer:
    """A composable class to commit changes to a Git repo."""

    gitter: Gitter | None = None
    gpt_client: GPTClient | None = None
    model: str = '3'
    temp: float = 0.75
    max_tokens: int = 32000
    prompt: str | None = None
    message: str | None = None

    def __init__(self, repo_path: str):
        """
        Initializes the `Committer` class.

        :param str repo_path: Path to the Git repository.
        """
        self.gitter = Gitter(repo_path)
        self.gpt_client = GPTClient(self.model, self.temp, self.max_tokens)

    def set_model(self, model: str, temp: float = None, max_tokens: int = None) -> 'Committer':
        """
        Sets the GPT model, temperature, and maximum tokens for the Committer.

        :param str model: GPT model to use.
        :param float temp: Temperature for the GPT model.
        :param int max_tokens: Maximum number of tokens for the GPT model.
        :return: The updated Committer instance.
        """
        if model is not None:
            self.model = model
        if temp is not None:
            self.temp = temp
        if max_tokens is not None:
            self.max_tokens = max_tokens
        self.gpt_client = GPTClient(self.model, self.temp, self.max_tokens)
        return self

    def set_prompt(self, prompt: str) -> 'Committer':
        """
        Sets the GPT prompt for the Committer

        :param str prompt: The GPT prompt.
        :return: The updated Committer instance.
        """
        self.prompt = prompt
        return self

    def set_message(self, commit_message: str) -> 'Committer':
        """
        Sets the commit message manually for the Committer.

        :param str commit_message: Commit message.
        :return: The updated Committer instance.
        """
        self.message = commit_message
        return self

    def set_message_via_content(self, old_content: str, new_content: str):
        """
        Generates a commit message based on the diff of old_content and new_content.

        :param str old_content: Original content.
        :param str new_content: Updated content.
        :return: The generated commit message.
        """
        diff = diff_content(old_content.splitlines(), new_content.splitlines())
        prompt = f"{self.prompt or 'Write a commit message for the following changes:'}{nl2}{nl}{diff}{nl}{nl2}"
        prompt += "[Ultimatum: Limit your response to only the git message, including nothing else.]"
        self.message = self.gpt_client.generate(prompt)
        if self.message is None:
            print_t('Could not generate commit message. Using generic commit message.', 'warning')
            return 'Updated via CodeMonkeys.'
        return self.message

    def get_message(self) -> str | None:
        """
        Gets the current commit message.

        :return: The current commit message, or None if not set.
        """
        return self.message

    def commit(self) -> None:
        """
        Performs git commit with the current commit message.

        Note:
            All staged changes are committed with the current commit message.
        """
        self.gitter.commit(self.message, add_all=True)
