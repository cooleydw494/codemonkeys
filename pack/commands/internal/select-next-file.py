import os
from definitions import STORAGE_INTERNAL_PATH


def main():
    input_file = os.path.join(STORAGE_INTERNAL_PATH, "listed-files.txt")

    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Get the next file and remove the line number
    next_file = lines[0].split('. ', 1)[1].strip()

    # Write the remaining lines back to the file
    with open(input_file, 'w') as file:
        file.writelines(lines[1:])

    # Output the saved file path
    return next_file


if __name__ == "__main__":
    main()
