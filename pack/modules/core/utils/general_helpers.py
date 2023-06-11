import os

import Levenshtein

from definitions import STOR_TEMP_PATH


def select_next_file():
    input_file = os.path.join(STOR_TEMP_PATH, "files-to-process.txt")

    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Get the next file and remove the line number
    next_file = lines[0].split('. ', 1)[1].strip()

    # Write the remaining lines back to the file
    with open(input_file, 'w') as file:
        file.writelines(lines[1:])

    # Output the saved file path
    return next_file


def levenshtein_distance(str1, str2):
    # determine if string1 or string2 fully contains the other and if so print(0) to emulate a match
    if str1 in str2 or str2 in str1:
        return 0
    return Levenshtein.distance(str1, str2)
