from codemonkeys.types import OInt

"""This stubbed file isn't intended as an example of a real use-case, but an example of how to use the class."""


class Func:
    """
    A class to represent a function to be called by a GPT model.
    Pass this in a list to the `funcs` parameter of the GPTClient.generate() method.
    The generate method will handle passing the data correctly and return the result of the _execute method.
    The _execute method can be fully custom or you can simply invoke an exiting function.

    You can pass multiple Funcs in the list. You can also set the `enforce_func` parameter
    to the "name" to force the model to use a specific function.
    """

    name: str = 'func_name'

    _description: str = 'This function either adds arg1 to arg2 or returns arg1 if arg2 is not provided.'

    # For more information on function calling parameters configuration options, see:
    # https://platform.openai.com/docs/guides/gpt/function-calling
    _parameters: dict = {
        "type": "object",
        "properties": {
            "arg1": {
                "type": "int",
                "description": "Description for arg1",
            },
            "arg2": {
                "type": "int",
                "description": "Description for arg2",
            },
        },
        "required": ["arg1"],
    }

    @classmethod
    def _execute(cls, arg1: int, arg2: OInt) -> int:
        if arg2 is None:
            return arg1
        return arg1 + arg2
