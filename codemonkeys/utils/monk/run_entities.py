import importlib.util
import os
from typing import Any, Dict, List, Optional

from codemonkeys.config_imports import MonkeyConfig


def run_command(entity_path: str, entity_name: str, named_args: Dict[str, Any],
                unnamed_args: List[str]):
    """
    Locates `Command` using path/name, instantiates it, and runs it.

    :param str entity_path: The file path to a `Command`.
    :param str entity_name: The name of the `Command`.
    :param Dict[str, Any] named_args: The named arg data passed to the `Command` instance.
    :param List[str] unnamed_args: The unnamed args passed to the `Command` instance.
    """
    command = load_class(entity_path, entity_name)
    command(named_args, unnamed_args).run()


def run_automation(entity_path: str, entity_name: str, named_args: Dict[str, Any],
                   unnamed_args: List[str], monkey_config: Optional[MonkeyConfig] = None):
    """
    Locates `Automation` using path/name, instantiates it, and runs it.

    :param str entity_path: The file path to an `Automation`.
    :param str entity_name: The name of the `Automation`.
    :param Dict[str, Any] named_args: The named arg data passed to the `Automation` instance.
    :param List[str] unnamed_args: The unnamed args passed to the `Automation` instance.
    :param MonkeyConfig monkey_config: A MonkeyConfig instance or None.
    """
    automation = load_class(entity_path, entity_name)
    automation(named_args, unnamed_args, monkey_config).run()


def run_barrel(entity_path: str, entity_name: str, named_args: Dict[str, Any], unnamed_args: List[str]):
    """
    Locates `Barrel` using path/name, instantiates it, and runs it.

    :param str entity_path: The file path to a `Barrel`.
    :param str entity_name: The name of the `Barrel`.
    :param Dict[str, Any] named_args: The named arg data passed to the `Barrel` instance.
    :param List[str] unnamed_args: The unnamed args passed to the `Barrel` instance.
    """
    barrel = load_class(entity_path, entity_name)
    barrel(named_args, unnamed_args).run()


def load_class(entity_path: str, entity_name: str) -> Any:
    """
    Locates Entity class using path/name, loads the module, and returns the class reference for instantiation.
    This logic assumes an entity's class name is the same as the filename/CLI-name, but in CamelCase.

    :param str entity_path: The file path to the Entity class.
    :param str entity_name: The name of the Entity class.
    """
    # Convert entity_name from kebab-case to CamelCase
    entity_name_camel_case = ''.join(word.capitalize() for word in entity_name.split('-'))

    # Normalize path
    entity_path = os.path.normpath(entity_path)

    # Create module spec, load module, and get class
    module_spec = importlib.util.spec_from_file_location(entity_name_camel_case, entity_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    entity_class = getattr(module, entity_name_camel_case)

    return entity_class
