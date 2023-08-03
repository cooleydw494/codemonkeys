import importlib.util
import os
from typing import Any, Dict, List, Optional

from codemonkeys.utils.monk.theme_functions import print_t

try:
    from config.framework.monkey_config import MonkeyConfig
except ImportError:
    print_t('Could not import user MonkeyConfig class from config.framework.monkey_config. Using default '
            'MonkeyConfig class. automation', 'warning')
    from codemonkeys.config.monkey_config import MonkeyConfig


def run_command(entity_path: str, entity_name: str, monk_args: Any, named_args: Dict[str, Any],
                unnamed_args: List[str]):
    """
    Locates `Command` using path/name, instantiates it, and runs it.

    :param str entity_path: The file path to a `Command`.
    :param str entity_name: The name of the `Command`.
    :param Any monk_args: The arg data passed to the `Command` instance.
    :param Dict[str, Any] named_args: The named arg data passed to the `Command` instance.
    :param List[str] unnamed_args: The unnamed args passed to the `Command` instance.
    """
    _run_entity(entity_path, entity_name, monk_args, named_args, unnamed_args)


def run_automation(entity_path: str, entity_name: str, monk_args: Any, named_args: Dict[str, Any],
                   unnamed_args: List[str], monkey_config: Optional[MonkeyConfig] = None):
    """
    Locates `Automation` using path/name, instantiates it, and runs it.

    :param str entity_path: The file path to an `Automation`.
    :param str entity_name: The name of the `Automation`.
    :param Any monk_args: The arg data passed to the `Automation` instance.
    :param Dict[str, Any] named_args: The named arg data passed to the `Automation` instance.
    :param List[str] unnamed_args: The unnamed args passed to the `Automation` instance.
    :param MonkeyConfig monkey_config: A MonkeyConfig instance or None.
    """
    _run_entity(entity_path, entity_name, monk_args, named_args, unnamed_args, monkey_config)


def run_barrel(entity_path: str, entity_name: str, monk_args: Any, named_args: Dict[str, Any], unnamed_args: List[str]):
    """
    Locates `Barrel` using path/name, instantiates it, and runs it.

    :param str entity_path: The file path to a `Barrel`.
    :param str entity_name: The name of the `Barrel`.
    :param Any monk_args: The arg data passed to the `Barrel` instance.
    :param Dict[str, Any] named_args: The named arg data passed to the `Barrel` instance.
    :param List[str] unnamed_args: The unnamed args passed to the `Barrel` instance.
    """
    _run_entity(entity_path, entity_name, monk_args, named_args, unnamed_args)


def _run_entity(entity_path: str, entity_name: str, monk_args: Any, named_args: Dict[str, Any], unnamed_args: List[str],
                monkey_config: Optional[MonkeyConfig] = None):
    """
    Locates Entity class using path/name, instantiates it, and runs it.

    :param str entity_path: The file path to an Entity class.
    :param str entity_name: The name of the Entity class.
    :param Any monk_args: The arg data passed to the Entity class instance.
    :param Dict[str, Any] named_args: The named arg data passed to the Entity class instance.
    :param List[str] unnamed_args: The unnamed args passed to the Entity class instance.
    :param MonkeyConfig monkey_config: A MonkeyConfig instance or None.
    """
    # Convert the entity_name from kebab-case to CamelCase
    entity_name_camel_case = ''.join(word.capitalize() for word in entity_name.split('-'))

    # Normalize path
    entity_path = os.path.normpath(entity_path)

    # Create module spec
    spec = importlib.util.spec_from_file_location(entity_name_camel_case, entity_path)

    # Load module
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get class from module (assuming the class name is the same as the entity name)
    class_ = getattr(module, entity_name_camel_case)

    # Instantiate class and run
    if class_.__name__ == 'Automation':
        instance = class_(monk_args, named_args, unnamed_args, monkey_config)
    else:
        instance = class_(monk_args, named_args, unnamed_args)

    instance.run()
