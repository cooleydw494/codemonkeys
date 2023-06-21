import os

import Levenshtein


def find_project_root():
    """Find the root directory of the project (i.e., the closest parent directory containing a `.env` file)."""
    cwd = os.getcwd()

    while cwd != os.path.dirname(cwd):  # Stop when we reach the root directory
        if '.env' in os.listdir(cwd):
            return cwd
        cwd = os.path.dirname(cwd)

    raise RuntimeError("Could not find project root")


def levenshtein_distance(str1, str2):
    # determine if string1 or string2 fully contains the other and if so print(0) to emulate a match
    if str1 in str2 or str2 in str1:
        return 0
    return Levenshtein.distance(str1, str2)
