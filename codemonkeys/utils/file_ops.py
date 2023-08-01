import os


def get_file_contents(path: str) -> str:
    """
    Reads the contents of a file and returns it as a str.

    :param str path: The path to the file.
    :return: The contents of the file.
    """
    path = resolve_file_path(path)

    if not os.path.isfile(path):
        raise FileNotFoundError(f"File does not exist: {path}")

    with open(path, "r") as f:
        context_file_contents = f.read()

    return context_file_contents


def write_file_contents(path: str, contents: str) -> None:
    """
    Writes the specified contents to a file.

    :param str path: The path to the file.
    :param str contents: New file contents
    """
    path = resolve_file_path(path)

    with open(path, "w") as f:
        f.write(contents)


def file_exists(path: str) -> bool:
    """
    Checks if a file exists at the specified path.

    :param str path: The path of the file.
    :return: True if the file exists, otherwise False.
    """
    path = resolve_file_path(path)
    return os.path.isfile(path)


def resolve_file_path(path: str) -> str:
    """
    Expands a file path that may contain user shortcuts (e.g. ~).

    :param str path: The path to be resolved
    :return: The expanded file path
    """
    return os.path.expanduser(path)
