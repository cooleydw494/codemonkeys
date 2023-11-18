from typing import List, Dict, Any, get_type_hints, Optional


class CliRunnable:
    """
    A base class for CLI-runnable entities such as Automations, Barrels, and Commands. Handles management of CLI args.
    Subclasses of `CliRunnable` will override argument-related class attributes and implement the `run` method.

    Attributes:
        named_args (Dict[str, Any]): A dictionary holding the named arguments provided to the CLI.
        unnamed_args (List[str]): A list holding the unnamed arguments provided to the CLI.
        named_arg_keys (list): A list of keys for named arguments that this CLI entity accepts.
        unnamed_arg_keys (list): A list of keys for unnamed arguments that this CLI entity accepts.
        required_arg_keys (list): A list of keys for arguments that are required for this CLI entity.

    """
    named_arg_keys: list = []
    unnamed_arg_keys: list = []
    required_arg_keys: list = []

    def __init__(self, named_args: Dict[str, Any], unnamed_args: List[str]):
        """
        Initializes the `CliRunnable` instance.
        
        :param named_args: Dict of named args and values (e.g. `--key value`).
        :type named_args: Dict[str, Any]
        :param unnamed_args: List of unnamed args (e.g. `value`).
        :type unnamed_args: List[str]
        """
        self.named_args: Optional[Dict[str, Any]] = named_args
        self.unnamed_args: Optional[List[str]] = unnamed_args

        # Named args: mapped by key
        for key in self.named_arg_keys:
            # Check possible formats: key, --key. Flag-style '-' args not allowed
            possible_keys = [key, f"--{key}"]
            matched_key = next((k for k in possible_keys if k in named_args), None)

            # Override default values with provided values
            if matched_key is not None:
                self._set_arg(key, named_args[matched_key])

        # Unnamed args: ordered list
        for key, value in zip(self.unnamed_arg_keys, unnamed_args or []):
            # If an arg was provided, override the default
            if value is not None:
                self._set_arg(key, value)

        # Check that all required args are provided
        for key in self.required_arg_keys:
            if getattr(self, key, None) is None:
                raise ValueError(f"Argument {key} is required but was not provided.")

    def _set_arg(self, key: str, value: Any):
        """
        Sets an argument's value, with type checking if a type hint is specified.
        
        :param key: The key of the argument to set.
        :type key: str
        :param value: The value of the argument to set.
        :type value: Any
        """

        # Get the expected type from the type hint, if any
        expected_type = get_type_hints(self.__class__).get(key)

        if expected_type is not None:
            # If it's a Union type, check if it allows None
            if hasattr(expected_type, "__args__"):
                allow_none = expected_type.__args__[1] is type(None)
                expected_type = expected_type.__args__[0]
            else:
                allow_none = False

            # if expected type is bool, coerce allowed bool values
            if expected_type is bool:
                true = value in [1, "1", "true", "True", True]
                false = value in [0, "0", "false", "False", False]
                value_is_bool = true or false
                if value_is_bool:
                    value = true
                else:
                    raise TypeError(f"Argument {key} should be of type bool, but got {type(value).__name__}")

            # Check the type of the value
            if not isinstance(value, expected_type) and not (allow_none and value is None):
                raise TypeError(
                    f"Argument {key} should be of type {expected_type.__name__}, but got {type(value).__name__}")

        setattr(self, key, value)

    def run(self) -> None:
        """
        The main logic of the CliRunnable (e.g. Command, Automation, Barrel).
        Subclasses must implement this method.

        :raises NotImplementedError: Always, unless overridden by subclass implementation.
        """
        raise NotImplementedError("Subclasses must implement this method")
