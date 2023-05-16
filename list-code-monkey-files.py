import os
from tokenizers import ByteLevelBPETokenizer

# Variables for tweakability
output_file = "code-monkey-files.txt"
starting_directory = "~/local-git/VirtueMaster"
include_extensions = [".js"]
exclude_patterns = [".config.js"]
max_tokens = 5500  # The maximum number of tokens for a file to be included

# Initialize a BPE tokenizer
tokenizer = ByteLevelBPETokenizer()

# This script searches for files with specified extensions in a given directory
# and its subdirectories, excluding files with specific patterns. The file paths
# are written to an output file, numbered on different lines.

def should_include(file_path):
    return any(file_path.endswith(ext) for ext in include_extensions) and not any(pattern in file_path for pattern in exclude_patterns)

filtered_files = []

# Walk through the starting directory and its subdirectories
for root, _, files in os.walk(starting_directory):
    for file in files:
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

# Write the filtered file paths to the output file
with open(output_file, "w") as f:
    for idx, file_path in enumerate(filtered_files, start=1):
        f.write(f"{idx}. {file_path}\n")

print(f"List of files saved to {output_file}.")

