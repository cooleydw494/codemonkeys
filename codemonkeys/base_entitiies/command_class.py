from typing import List, Dict, Any


class Command:
    named_arg_keys = []
    unnamed_arg_keys = []
    required_named_arg_keys = []
    required_unnamed_arg_keys = []

    def __init__(self, monk_args: Any, named_args: Dict[str, Any], unnamed_args: List[str]):
        self.monk_args = monk_args

        self._unnamed_args = {}
        self._named_args = {}

        for key in self.named_arg_keys:
            if key in self.required_named_arg_keys and key not in named_args:
                raise ValueError(f"Named argument {key} is required but was not provided.")
            self._named_args[key] = named_args.get(key, getattr(self, key, None))

        for key in self.unnamed_arg_keys:
            if key in self.required_unnamed_arg_keys and unnamed_args is None:
                raise ValueError(f"Unnamed argument {key} is required but was not provided.")
            self._unnamed_args[key] = getattr(self, key, None)

        for key, value in zip(self._unnamed_args, unnamed_args or []):
            self._unnamed_args[key] = value

    @property
    def command_args(self):
        args = self._named_args.copy()  # Named args
        args.update(self._unnamed_args)  # Include unnamed args
        return args

    def main(self):
        raise NotImplementedError("Subclasses must implement this method")
