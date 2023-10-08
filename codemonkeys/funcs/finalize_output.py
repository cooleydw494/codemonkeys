from codemonkeys.entities.func import Func


class FinalizeOutput(Func):

    """
    This Func is intended to be used in the default automation along with the FIX_OUTPUT_PROMPT.
    It is a very vague function that allows the FIX_OUTPUT_PROMPT to be used with flexibility to dictate the output.
    The intention is to coerce GPT to do a better job of delivering a result that doesn't include extraneous text.

    The default FIX_OUTPUT_PROMPT is meant to ensure the result contains nothing but the contents of a file.
    """

    name: str = 'finalize_output'

    _description: str = 'This function handles finalized output for a variety of cases, such as writing a file.'

    _parameters: dict = {
        "type": "object",
        "properties": {
            "output": {
                "type": "string",
                "description": "The finalized output, requiring no further processing to be used as intended.",
            },
        },
        "required": ["output"],
    }

    @classmethod
    def _execute(cls, output: str) -> str:
        return output
