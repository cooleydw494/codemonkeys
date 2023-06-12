import importlib.util
import os


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
