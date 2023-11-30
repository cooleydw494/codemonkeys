from codemonkeys.entities.automation import Automation


class ExampleAutomation(Automation):
    """
    Example Automation.
    """

    def run(self) -> None:
        """
        Execute the main logic of the automation.

        This method handles file processing according to Monkey configurations and
        applies GPT-powered logic across the specified files.
        """
        m = self._monkey
        print(m.MAIN_PROMPT)
