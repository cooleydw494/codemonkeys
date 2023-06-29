import importlib.util
import os
from typing import Any, Dict, List


def run_automation(entity_path, monk_args):
    # Normalize path and get module name
    entity_path = os.path.normpath(entity_path)
    module_name = os.path.splitext(os.path.basename(entity_path))[0]

    # Create module spec
    spec = importlib.util.spec_from_file_location(module_name, entity_path)

    # Load module
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get class from module (assuming the class name is the same as the file name)
    class_ = getattr(module, module_name)

    # Instantiate class and run
    instance = class_(monk_args)
    instance.main()


def run_command(filepath: str, entity_name: str, monk_args: Any, named_args: Dict[str, Any], unnamed_args: List[str]):

    # Convert the entity_name from kebab-case to CamelCase
    entity_name_camel_case = ''.join(word.capitalize() for word in entity_name.split('-'))

    # Load module from filepath
    spec = importlib.util.spec_from_file_location(entity_name_camel_case, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get the command class from the module
    command_class = getattr(module, entity_name_camel_case)

    # Instantiate the command
    command_instance = command_class(monk_args, named_args, unnamed_args)

    # Run the command
    command_instance.main()
