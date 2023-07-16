import os


def get_file_contents(path) -> str:
    path = resolve_file_path(path)

    if not os.path.isfile(path):
        raise FileNotFoundError(f"File does not exist: {path}")

    with open(path, "r") as f:
        context_file_contents = f.read()

    return context_file_contents


def resolve_file_path(path) -> str:
    return os.path.expanduser(path)