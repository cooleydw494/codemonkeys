import argparse
from typing import List, Dict, Any


class CliRunnable:
    named_arg_keys = []
    unnamed_arg_keys = []
    required_arg_keys = []

    def __init__(self, monk_args: argparse.Namespace, named_args: Dict[str, Any], unnamed_args: List[str]):
        self.monk_args = monk_args

        # Named args: mapped by key and checked for required ones
        # Now support keys with '-' or '--' prefix
        for key in self.named_arg_keys:
            # Check all possible versions: key, --key. Flag-style '-' args not allowed
            possible_keys = [key, f"--{key}"]
            matched_key = next((k for k in possible_keys if k in named_args), None)

            # If an arg was provided, override the default
            if matched_key is not None:
                setattr(self, key, named_args[matched_key])

        # Unnamed args: ordered list, checked for required ones
        for key, value in zip(self.unnamed_arg_keys, unnamed_args or []):
            # If an arg was provided, override the default
            if value is not None:
                setattr(self, key, value)

        # Check that all required arguments are provided
        for key in self.required_arg_keys:
            if getattr(self, key, None) is None:
                raise ValueError(f"Argument {key} is required but was not provided.")

    def main(self):
        """
        The main logic of the command.
        """
        raise NotImplementedError("Subclasses must implement this method")