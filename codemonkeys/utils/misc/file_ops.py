import os


def get_file_contents(path: str) -> str:
    """
    Reads the contents of a file and returns it as a string.

    Given a file path, this function reads the file and returns its contents as a string. If the
    file does not exist, it raises a FileNotFoundError.

    :param path: The path to the file to be read.
    :type path: str
    :return: The contents of the file as a string.
    :rtype: str
    :raises FileNotFoundError: If the file specified by the path does not exist.
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

    This function takes a file path and a string of contents, then writes those contents to the
    file located at the path. It overwrites any existing contents in the file.

    :param path: The path to the file where contents will be written.
    :type path: str
    :param contents: The new contents to write to the file.
    :type contents: str
    """
    path = os.path.expanduser(path)

    with open(path, "w") as f:
        f.write(contents)
