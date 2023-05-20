import os
import time

from dotenv import load_dotenv
from tokenizers import ByteLevelBPETokenizer

# Load environment variables from .env file
load_dotenv()

base_dir_abs_path = os.getenv("BASE_DIR_ABS_PATH")

# Only files with these extensions will be included
include_extensions = os.getenv("FILE_TYPES_INCLUDED", ".js")
include_extensions = include_extensions.split(',')

# No files with one of these strings in the absolute filepath will be included
exclude_patterns = os.getenv("FILEPATH_MATCH_EXCLUDED", ".git,.config,tests")
exclude_patterns = exclude_patterns.split(',')

# The maximum number of tokens for a file to be included
max_tokens = int(os.getenv("FILE_SELECT_MAX_TOKENS", 5500))


def resolve_path(path):
    path = os.path.expandvars(path)  # Expand environment variables
    path = os.path.expanduser(path)  # Handle '~'
    path = os.path.abspath(path)  # Handle relative paths
    return path


# Do not alter output_file unless you're prepared to make other script alterations
output_file = os.path.join(base_dir_abs_path, "storage/listed-files.txt")
starting_directory = resolve_path(os.getenv("WORK_PATH"))
print(starting_directory)

# Initialize a BPE tokenizer
tokenizer = ByteLevelBPETokenizer()


def should_include(file_path):
    return any(file_path.endswith(ext) for ext in include_extensions) and not any(
        pattern in file_path for pattern in exclude_patterns)


filtered_files = []

print("🔍 Starting to search for files... this might take a while depending on the size of your project.")

# Walk through the starting directory and its subdirectories
for root, _, files in os.walk(starting_directory):
    for file in files:
        # Simulate loading
        print(".", end='', flush=True)
        time.sleep(0.001)

        # Check if the file should be included based on the conditions
        if should_include(file):
            absolute_path = os.path.abspath(os.path.join(root, file))

            # Check the number of tokens
            with open(absolute_path, 'r') as f:
                text = f.read()
            num_tokens = len(tokenizer.encode(text).tokens)

            # Only include the file if it doesn't exceed the maximum number of tokens
            if num_tokens <= max_tokens:
                filtered_files.append(absolute_path)

print("\n✅ File search completed!")

# Write the filtered file paths to the output file
with open(output_file, "w") as f:
    for idx, file_path in enumerate(filtered_files, start=1):
        f.write(f"{idx}. {file_path}\n")

print(f"📝 List of files saved to {output_file}. Enjoy coding with your 🐒 code monkeys!")
# print the contents of the file to the console, truncating it with ellipsis if over 15 lines
with open(output_file, "r") as f:
    lines = f.readlines()
    if len(lines) > 15:
        print("".join(lines[:15]) + "...")
    else:
        print("".join(lines))
