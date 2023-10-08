from typing import Any


class Func:
    """
    A class to represent a function to be called by a GPT model.
    Pass this in a list to the `funcs` parameter of the GPTClient.generate() method.
    The generate method will handle passing the data correctly and return the result of the _execute method.
    The _execute method can be fully custom or you can simply invoke an exiting function.

    You can pass multiple Funcs in the list. You can also set the `enforce_func` parameter
    to the "name" to force the model to use a specific function.
    """

    name: str = 'function'

    _description: str = 'This function is used if some conditions are met to do something.'

    # For more information on function calling parameters configuration options, see:
    # https://platform.openai.com/docs/guides/gpt/function-calling
    _parameters: dict = {
        "type": "object",
        "properties": {},
        "required": [],
    }

    @classmethod
    def _execute(cls, args) -> Any:
        raise NotImplementedError('This function must be implemented in subclasses of Func.')

    def data(self) -> dict:
        return {
            'name': self.name,
            'description': self._description,
            'parameters': self._parameters,
        }

    def call(self, args: dict) -> Any:
        valid_args = {k: args.get(k) for k in self._parameters['properties'].keys()}
        return self._execute(**valid_args)
