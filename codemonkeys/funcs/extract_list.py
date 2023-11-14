from codemonkeys.entities.func import Func


class ExtractList(Func):
    """
    A Func for processing and extracting items from a list of strings.

    This function is designed to be used within prompts that generate lists of strings. It helps
    in cleaning and extracting individual strings from structured or semi-structured outputs.
    """

    name: str = 'extract_list'

    _description: str = 'Process a list of strings fulfilling a prompt'

    _parameters: dict = {
        "type": "object",
        "properties": {
            "strings": {
                "type": "array",
                "description": "List of strings",
                "items": {
                    "type": "string"
                }
            },
        },
        "required": ["strings"],
    }

    @classmethod
    def _execute(cls, strings: list[str]) -> list[str]:
        return strings
