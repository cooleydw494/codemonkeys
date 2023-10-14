from codemonkeys.entities.func import Func


class ExtractList(Func):
    name: str = 'extract_list'

    _description: str = 'Handles processing of a list of strings.'

    _parameters: dict = {
        "type": "object",
        "properties": {
            "extracted_list": {
                "type": "array",
                "description": "The list of strings which fulfills a prompted use-case.",
                "items": {
                    "type": "string"
                }
            },
        },
        "required": ["extracted_list"],
    }

    @classmethod
    def __execute(cls, extracted_list: list[str]) -> list[str]:
        return extracted_list
