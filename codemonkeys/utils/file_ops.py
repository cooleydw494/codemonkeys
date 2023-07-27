import os


def get_file_contents(path: str) -> str:
    path = resolve_file_path(path)

    if not os.path.isfile(path):
        raise FileNotFoundError(f"File does not exist: {path}")

    with open(path, "r") as f:
        context_file_contents = f.read()

    return context_file_contents


def write_file_contents(path: str, contents: str) -> None:
    path = resolve_file_path(path)

    with open(path, "w") as f:
        f.write(contents)


def file_exists(path: str) -> bool:
    path = resolve_file_path(path)
    return os.path.isfile(path)


def resolve_file_path(path: str) -> str:
    return os.path.expanduser(path)
