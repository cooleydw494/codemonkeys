import os

import Levenshtein

import importlib.util


def find_project_root():
    """Find the root directory of the project (i.e., the closest parent directory containing a `.env` file)."""
    cwd = os.getcwd()

    while cwd != os.path.dirname(cwd):  # Stop when we reach the root directory
        if '.env' in os.listdir(cwd):
            return cwd
        cwd = os.path.dirname(cwd)

    raise RuntimeError("Could not find project root")


def import_class_from_path_with_fallback(path, class_name, fallback_class):
    """
    Try to import a class from a Python file at a given path. If the import fails, return a fallback class.

    Args:
    - path (str): The path to the Python file.
    - class_name (str): The name of the class to import.
    - fallback_class (type): The class to use if the import fails.

    Returns:
    - The imported class, or the fallback class if the import fails.
    """
    try:
        spec = importlib.util.spec_from_file_location(class_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, class_name)
    except (ImportError, FileNotFoundError, AttributeError):
        return fallback_class


def levenshtein_distance(str1, str2):
    # determine if string1 or string2 fully contains the other and if so print(0) to emulate a match
    if str1 in str2 or str2 in str1:
        return 0
    return Levenshtein.distance(str1, str2)
