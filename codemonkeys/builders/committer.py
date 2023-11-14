import difflib
from typing import Sequence

from codemonkeys.defs import nl, nl2
from codemonkeys.types import OStr, OFloat, OInt
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

    def __init__(self, repo_path: str):
        """
        Initializes the `Committer` class.

        :param str repo_path: Path to the Git repository.
        """
        self._gitter: Gitter = Gitter(repo_path)
        self._gpt_client: GPTClient = GPTClient(self._model, self._temp, self._max_tokens)
        self._model: str = 'gpt-3.5-turbo'
        self._temp: float = 0.8
        self._max_tokens: int = 8000
        self._prompt: OStr = None
        self._message: str = 'Updated via CodeMonkeys.'

    def model(self, model: str, temp: OFloat = None, max_tokens: OInt = None) -> 'Committer':
        """
        Sets the GPT model, temperature, and maximum tokens.

        :param str model: GPT model to use.
        :param float temp: Temperature for the GPT model.
        :param int max_tokens: Maximum number of tokens for the GPT model.
        :return: The updated Committer instance.
        """
        if model is not None:
            self._model = model
        if temp is not None:
            self._temp = temp
        if max_tokens is not None:
            self._max_tokens = max_tokens
        self._gpt_client = GPTClient(self._model, self._temp, self._max_tokens)
        return self

    def prompt(self, prompt: str) -> 'Committer':
        """
        Sets the GPT prompt

        :param str prompt: The GPT prompt.
        :return: The updated Committer instance.
        """
        self._prompt = prompt
        return self

    def message(self, commit_message: str) -> 'Committer':
        """
        Sets the commit message manually.

        :param str commit_message: Commit message.
        :return: The updated Committer instance.
        """
        self._message = commit_message
        return self

    def message_from_context(self, old_content: str, new_content: str) -> 'Committer':
        """
        Generates a commit message based on the diff of old_content and new_content.

        :param str old_content: Original content.
        :param str new_content: Updated content.
        :return: The generated commit message.
        """
        diff = diff_content(old_content.splitlines(), new_content.splitlines())
        prompt = f"{self._prompt or 'Write a commit message for the following changes:'}{nl2}{nl}{diff}{nl}{nl2}"
        prompt += "[Ultimatum: Limit your response to only the git message, including nothing else.]"
        self._message = self._gpt_client.generate(prompt)
        if self._message is None:
            print_t('Could not generate commit message. Using generic commit message.', 'warning')
            self._message = 'Updated via CodeMonkeys.'
        return self

    def get_message(self) -> OStr:
        """
        Gets the current commit message.

        :return: The current commit message, or None if not set.
        """
        return self._message

    def commit(self) -> None:
        """
        Performs git commit with the current commit message.

        Note:
            All staged changes are committed with the current commit message.
        """
        self._gitter.commit(self._message, add_all=True)
        print_t(f"Git changes committed with message: {self._message}.", 'info')
