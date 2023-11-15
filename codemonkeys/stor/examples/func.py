from codemonkeys.entities.func import Func
from codemonkeys.types import OInt


class ExampleFunc(Func):
    """
    A class to represent a function to be called by a GPT model.

    This class allows for defining a custom function that can be invoked by
    the GPT model during text generation.
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
