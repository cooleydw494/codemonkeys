import difflib

from codemonkeys.defs import nl, nl2
from codemonkeys.utils.git.gitter import Gitter
from codemonkeys.utils.gpt.gpt_client import GPTClient
from codemonkeys.utils.monk.theme_functions import print_t


def diff_content(old_content: str, new_content: str) -> str:
    """
    Generates a unified diff between old_content and new_content.

    :param old_content: The original content.
    :type old_content: str
    :param new_content: The updated content.
    :type new_content: str
    :return: The unified diff as a string.
    :rtype: str
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

        :param repo_path: Path to the Git repository.
        :type repo_path: str
        """
        self.gitter = Gitter(repo_path)
        self.gpt_client = GPTClient(self.model, self.temp, self.max_tokens)

    def set_model(self, model: str, temp: float = None, max_tokens: int = None) -> 'Committer':
        """
        Sets the GPT model, temperature, and maximum tokens for the Committer.

        :param model: GPT model to use.
        :type model: str
        :param temp: Temperature for the GPT model. Defaults to None.
        :type temp: float, optional
        :param max_tokens: Maximum number of tokens for the GPT model. Defaults to None.
        :type max_tokens: int, optional
        :return: The updated Committer instance.
        :rtype: Committer
        """
        self.model = model
        self.temp = temp
        self.max_tokens = max_tokens
        self.gpt_client = GPTClient(self.model, self.temp, self.max_tokens)
        return self

    def set_prompt(self, prompt: str) -> 'Committer':
        """
        Sets the GPT prompt for the Committer

        :param prompt: The GPT prompt.
        :type prompt: str
        :return: The updated Committer instance.
        :rtype: Committer
        """
        self.prompt = prompt
        return self

    def set_message(self, commit_message: str) -> 'Committer':
        """
        Sets the commit message manually for the Committer.

        :param commit_message: Commit message.
        :type commit_message: str
        :return: The updated Committer instance.
        :rtype: Committer
        """
        self.message = commit_message
        return self

    def set_message_via_content(self, old_content: str, new_content: str):
        """
        Generates a commit message based on the diff of old_content and new_content.

        :param old_content: Original content.
        :type old_content: str
        :param new_content: Updated content.
        :type new_content: str
        :return: The generated commit message.
        :rtype: str
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
        :rtype: str | None
        """
        return self.message

    def commit(self) -> None:
        """
        Performs git commit with the current commit message.

        Note:
            All staged changes are committed with the current commit message.
        """
        self.gitter.commit(self.message, add_all=True)
