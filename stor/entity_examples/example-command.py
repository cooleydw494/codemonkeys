from codemonkeys.base_entitiies.command_class import Command


class ExampleCommand(Command):

    # Specify named args (passed with -name=value or --name=value)
    named_arg_keys = ['named_arg_one', 'named_arg_two']
    # Set defaults for optional named args
    named_arg_one = 'default_named'
    # Set required named args (you should still define it and set to None)
    required_named_arg_keys = ['named_arg_two']
    named_arg_two = None

    # Specify unnamed args (passed without - or --) (define in passing order)
    unnamed_arg_keys = ['unnamed_arg_one', 'unnamed_arg_two']
    # Set defaults for optional unnamed args
    unnamed_arg_one = 'default'
    # Set required named args (then define and set to None)
    required_unnamed_arg_keys = ['unnamed_arg_two']
    unnamed_arg_two = None

    def main(self):
        # Implement the command functionality here
        print(f"Command Args: {self.command_args}")
        print(f"Monk Args: {self.monk_args}")
