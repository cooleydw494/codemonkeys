import difflib
from typing import Sequence

from codemonkeys.defs import nl, nl2
from codemonkeys.types import OStr, OFloat, OInt
from codemonkeys.utils.git.gitter import Gitter
from codemonkeys.utils.gpt.gpt_client import GptClient
from codemonkeys.utils.monk.theme_functions import print_t


def diff_content(old_content: Sequence[str], new_content: Sequence[str]) -> str:
    """
    Generates a unified diff between old_content and new_content.

    Compares two sequences of strings, usually lines of text from files, and
    produces a human-readable mismatch highlighting the differences using the unified diff format.

    :param old_content: The original content to compare.
    :type old_content: Sequence[str]
    :param new_content: The updated content to compare.
    :type new_content: Sequence[str]
    :return: The unified diff as a string, with line changes indicated.
    :rtype: str
    """
    return nl.join(list(difflib.unified_diff(old_content, new_content)))


class Committer:
    """A builder class to commit changes to a Git repo."""

    def __init__(self, repo_path: str):
        """
        Initializes the `Committer` class.

        Sets up a `Gitter` instance for Git operations and a `GptClient` for generating commit messages.

        :param repo_path: Path to the Git repository where commits will be made.
        :type repo_path: str
        """
        self._gitter: Gitter = Gitter(repo_path)
        self._gpt_client: GptClient = GptClient(self._model, self._temp, self._max_tokens)
        self._model: str = 'gpt-3.5-turbo'
        self._temp: float = 0.8
        self._max_tokens: int = 8000
        self._prompt: OStr = None
        self._message: str = 'Updated via CodeMonkeys.'

    def model(self, model: str, temp: OFloat = None, max_tokens: OInt = None) -> 'Committer':
        """
        Sets the GPT model, temperature, and maximum tokens.

        Configures the GPT client with model specifications for generating commit messages.

        :param model: GPT model to use.
        :type model: str
        :param temp: Temperature for the GPT model.
        :type temp: OFloat, optional
        :param max_tokens: Maximum number of tokens for the GPT model.
        :type max_tokens: OInt, optional
        :return: The updated Committer instance with new model settings.
        :rtype: Committer
        """
        if model is not None:
            self._model = model
        if temp is not None:
            self._temp = temp
        if max_tokens is not None:
            self._max_tokens = max_tokens
        self._gpt_client = GptClient(self._model, self._temp, self._max_tokens)
        return self

    def prompt(self, prompt: str) -> 'Committer':
        """
        Sets the GPT prompt.

        Defines the prompt that will be used to generate commit messages.

        :param prompt: The GPT prompt.
        :type prompt: str
        :return: The updated Committer instance with the new prompt.
        :rtype: Committer
        """
        self._prompt = prompt
        return self

    def message(self, commit_message: str) -> 'Committer':
        """
        Sets the commit message manually.

        Directly sets the commit message to be used for commits.

        :param commit_message: Commit message.
        :type commit_message: str
        :return: The updated Committer instance with the provided commit message.
        :rtype: Committer
        """
        self._message = commit_message
        return self

    def message_from_context(self, old_content: str, new_content: str) -> 'Committer':
        """
        Generates a commit message based on the diff of old_content and new_content.

        Uses the difference between the old and new content to generate a commit description.
        If the message cannot be generated, a generic message will be used.

        :param old_content: Original content.
        :type old_content: str
        :param new_content: Updated content.
        :type new_content: str
        :return: The Committer instance with the generated or default commit message.
        :rtype: Committer
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

        Returns the commit message set in the Committer instance, if any.

        :return: The current commit message, or None if not set.
        :rtype: OStr
        """
        return self._message

    def commit(self) -> None:
        """
        Performs git commit with the current commit message.

        Stages and commits all changes in the provided Git repository using the set commit message.
        Note that unstaged changes are not included unless already staged.

        :raises Exception: If committing fails.
        """
        self._gitter.commit(self._message, add_all=True)
        print_t(f"Git changes committed with message: {self._message}.", 'info')
