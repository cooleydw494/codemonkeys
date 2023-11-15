from codemonkeys.entities.barrel import Barrel


class ExampleBarrel(Barrel):
    """
    A Barrel for orchestrating multiple automation tasks with different Monkeys.

    ExampleBarrel is a class that extends from CliRunnable and is designed to chain together
    multiple automations using specified Monkey configurations. It demonstrates how to run
    automations sequentially and pass different Monkeys to alter their behavior.

    Note:
        Refer to the CliRunnable class for more details on defining, passing,
        defaulting, and requiring CLI arguments.
    """

    def run(self) -> None:
        """Use this method to load Monkey configs and chain multiple automations."""
        (self
         .with_monkey('comment-monkey')
         .run_automation('default')

         # Chain multiple automations together
         .with_monkey('write-todos-monkey')
         .run_automation('default')
         .with_monkey('implement-monkey')
         .run_automation('default')

         # You can chain automations without choosing new monkeys
         .run_automation('some-other-automation'))
