from codemonkeys.entities.automation import Automation


class DefaultAutomation(Automation):
    """
    The Default Automation for CodeMonkeys.

    This automation serves as a generic template for running GPT-powered file operations,
    whether individually, or in bulk across a directory. It exemplifies how Monkeys can be
    configured to guide the automation flow and specific GPT interactions.
    """

    def run(self) -> None:
        """
        Execute the main logic of the automation.

        This method handles file processing according to Monkey configurations and
        applies GPT-powered logic across the specified files.
        """
