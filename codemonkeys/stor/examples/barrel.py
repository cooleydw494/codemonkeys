from codemonkeys.entities.barrel import Barrel

"""
Barrels are intended to orchestrate multiple automations / Monkey configs.
I'd recommend having a few fleshed out automations working as intended before reaching for barrels.
"""


class ExampleBarrel(Barrel):
    """
    Barrels are extended from CliRunnable, so you can define/pass/default/require CLI args if you wish.
    Check out the CliRunnable class or look at Command implementations to get a feel for this.
    """

    def run(self) -> None:
        """Use this method to load Monkey configs and chain multiple automations."""
        (self
         # Load a Monkey config (omit name to _prompt user)
         .with_monkey('comment-monkey')
         .run_automation('default')

         # Chain multiple automations together
         .with_monkey('write-todos-monkey')
         .run_automation('default')
         .with_monkey('implement-monkey')
         .run_automation('default')

         # You can chain automations without choosing new monkeys
         .run_automation('some-other-automation'))
