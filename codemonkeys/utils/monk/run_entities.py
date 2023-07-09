import importlib.util
import importlib.util
import os
from typing import Any, Dict, List


def run_entity(entity_path: str, entity_name: str, monk_args: Any, named_args: Dict[str, Any], unnamed_args: List[str]):

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
    instance = class_(monk_args, named_args, unnamed_args)
    instance.run()


def run_automation(entity_path: str, entity_name: str, monk_args: Any, named_args: Dict[str, Any],
                   unnamed_args: List[str]):
    run_entity(entity_path, entity_name, monk_args, named_args, unnamed_args)


def run_command(entity_path: str, entity_name: str, monk_args: Any, named_args: Dict[str, Any], unnamed_args: List[str]):
    run_entity(entity_path, entity_name, monk_args, named_args, unnamed_args)
