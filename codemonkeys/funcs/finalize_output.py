from codemonkeys.entities.func import Func


class FinalizeOutput(Func):
    """
    This Func is intended to be used in default automation to finalize output for file writing.

    The FinalizeOutput function is designed as a generic handler that instructs GPT to provide output
    with the assumption that the result requires no further processing to be used as intended.
    """

    name: str = 'finalize_output'

    _description: str = 'This function is a handler for finalized output for various uses.'

    _parameters: dict = {
        "type": "object",
        "properties": {
            "output": {
                "type": "string",
                "description": "Finalized output requiring no further processing to be used as intended.",
            },
        },
        "required": ["output"],
    }

    @classmethod
    def _execute(cls, output: str) -> str:
        return output
