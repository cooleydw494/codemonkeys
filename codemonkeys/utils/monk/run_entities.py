from typing import Any, Dict, List, Optional

from codemonkeys.config.imports.monkey import Monkey
from codemonkeys.utils.defs_utils import load_class


def run_command(entity_path: str, entity_name: str, named_args: Dict[str, Any], unnamed_args: List[str]):
    """
    Locates `Command` using path/name, instantiates it, and runs it.

    :param str entity_path: The file path to a `Command`.
    :param str entity_name: The name of the `Command`.
    :param Dict[str, Any] named_args: The named arg data passed to the `Command` instance.
    :param List[str] unnamed_args: The unnamed args passed to the `Command` instance.
    """
    load_class(entity_path, entity_name)(named_args, unnamed_args).run()


def run_automation(entity_path: str, entity_name: str, named_args: Dict[str, Any], unnamed_args: List[str],
                   monkey: Optional[Monkey] = None):
    """
    Locates `Automation` using path/name, instantiates it, and runs it.

    :param str entity_path: The file path to an `Automation`.
    :param str entity_name: The name of the `Automation`.
    :param Dict[str, Any] named_args: The named arg data passed to the `Automation` instance.
    :param List[str] unnamed_args: The unnamed args passed to the `Automation` instance.
    :param Monkey monkey: A Monkey instance or None.
    """
    load_class(entity_path, entity_name)(named_args, unnamed_args, monkey).trigger()


def run_barrel(entity_path: str, entity_name: str, named_args: Dict[str, Any], unnamed_args: List[str]):
    """
    Locates `Barrel` using path/name, instantiates it, and runs it.

    :param str entity_path: The file path to a `Barrel`.
    :param str entity_name: The name of the `Barrel`.
    :param Dict[str, Any] named_args: The named arg data passed to the `Barrel` instance.
    :param List[str] unnamed_args: The unnamed args passed to the `Barrel` instance.
    """
    load_class(entity_path, entity_name)(named_args, unnamed_args).run()
