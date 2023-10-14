import os


def get_file_contents(path: str) -> str:
    """
    Reads the contents of a file and returns it as a str.

    :param str path: The path to the file.
    :return: The contents of the file.
    """
    path = os.path.expanduser(path)

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
    path = os.path.expanduser(path)

    with open(path, "w") as f:
        f.write(contents)
