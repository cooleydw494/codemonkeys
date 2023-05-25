import importlib.util
import os


def import_cm_modules(cm_modules):
    """
    This function is used to import modules for the framework. It uses an unconventional but simple
    import strategy that's designed specifically for the needs of the framework. It provides a way to import
    modules from anywhere in the framework without compromising on the simplicity of the pseudo-package paradigm.

    The function accepts a list of tuples. Each tuple contains two elements:
        1) The absolute path to the python file (module) to be imported.
        2) The name of the entity (function, class, variable) to be imported from that module.

    The function returns a dictionary. The keys are the names of the imported entities and the values are the
    imported entities themselves.

    In the event of an error (such as the file not existing, the module being invalid, or the named entity
    not being found in the module), an exception is raised with a detailed error message.

    Args:
        cm_modules (list[tuple[str, str]]): A list of tuples. Each tuple contains a path to a module and
                                             the name of an entity to import from that module.

    Returns:
        dict[str, Any]: A dictionary mapping the names of imported entities to the entities themselves.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ImportError: If there's a problem with the module or the named entity does not exist in the module.
    """

    imported_modules = {}

    for module_path, entity_to_import in cm_modules:

        if not os.path.exists(module_path):
            raise FileNotFoundError(f"No file found at path: {module_path}")

        spec = importlib.util.spec_from_file_location('module', module_path)

        if spec is None:
            raise ImportError(
                f"Cannot determine the module from path: {module_path}. Check if it's a valid Python module.")

        module = importlib.util.module_from_spec(spec)

        try:
            spec.loader.exec_module(module)
        except Exception as e:
            raise ImportError(
                f"An error occurred while importing the module at {module_path}. The error message is: {str(e)}")

        try:
            imported_entity = getattr(module, entity_to_import)
        except AttributeError:
            raise ImportError(
                f"Module {module_path} has no entity {entity_to_import}. Verify spelling/case of the entity name.")

        imported_modules[entity_to_import] = imported_entity

    return imported_modules
