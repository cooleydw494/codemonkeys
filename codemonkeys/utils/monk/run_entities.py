from typing import Any, Dict, List

from codemonkeys.utils.imports.monkey import OMonkey
from codemonkeys.utils.misc.defs_utils import load_class


def run_command(path: str, name: str, named_args: Dict[str, Any], unnamed_args: List[str]):
    """
    Locates `Command` using path/name, instantiates it, and runs it with provided arguments.

    This function hook serves to dynamically locate and execute a specified `Command`
    entity within the framework. It utilizes introspection to load a command class by its
    name, create an instance, and invoke its `run` method.

    :param path: The file path to a `Command`.
    :type path: str
    :param name: The name of the `Command`.
    :type name: str
    :param named_args: The named arg data passed to the `Command` instance.
    :type named_args: Dict[str, Any]
    :param unnamed_args: The unnamed args passed to the `Command` instance.
    :type unnamed_args: List[str]
    """
    load_class(path, name)(named_args, unnamed_args).run()


def run_automation(path: str, name: str, named_args: Dict[str, Any], unnamed_args: List[str], monkey: OMonkey = None):
    """
    Locates `Automation` using path/name, instantiates it, and runs it with provided arguments.

    Similar to `run_command`, this function identifies and instantiates an `Automation`
    entity based on its path and name. It also accepts a configurable Monkey object that
    tailors the behavior of the Automation.

    :param path: The file path to an `Automation`.
    :type path: str
    :param name: The name of the `Automation`.
    :type name: str
    :param named_args: The named arg data passed to the `Automation` instance.
    :type named_args: Dict[str, Any]
    :param unnamed_args: The unnamed args passed to the `Automation` instance.
    :type unnamed_args: List[str]
    :param monkey: An optional Monkey instance to customize automation behavior.
    :type monkey: OMonkey
    """
    load_class(path, name)(named_args, unnamed_args, monkey).trigger()


def run_barrel(path: str, name: str, named_args: Dict[str, Any], unnamed_args: List[str]):
    """
    Locates `Barrel` using path/name, instantiates it, and runs it with provided arguments.

    This function facilitates the execution of a `Barrel` by dynamically loading and
    instantiating the specified entity through the given path and name. Upon instantiation,
    it calls the `run` method of the Barrel.

    :param path: The file path to a `Barrel`.
    :type path: str
    :param name: The name of the `Barrel`.
    :type name: str
    :param named_args: The named arg data passed to the `Barrel` instance.
    :type named_args: Dict[str, Any]
    :param unnamed_args: The unnamed args passed to the `Barrel` instance.
    :type unnamed_args: List[str]
    """
    load_class(path, name)(named_args, unnamed_args).run()
