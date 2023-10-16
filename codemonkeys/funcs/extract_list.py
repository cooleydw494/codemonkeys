from codemonkeys.entities.func import Func


class ExtractList(Func):
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
