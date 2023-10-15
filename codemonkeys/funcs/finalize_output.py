from codemonkeys.entities.func import Func


class FinalizeOutput(Func):

    """
    This Func is intended to be used in the default automation to finalize output for file writing.
    It is a very vague function that coerces GPT into intuiting the desired output and omitting extraneous text.
    As long as prompts include language that allow GPT to intuit the use-case properly, it can be used in other ways.
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
    def __execute(cls, output: str) -> str:
        return output
