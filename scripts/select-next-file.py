input_file = "listed-files.txt"

with open(input_file, 'r') as file:
    lines = file.readlines()

# Get the next file and remove the line number
next_file = lines[0].split('. ', 1)[1].strip()

# Write the remaining lines back to the file
with open(input_file, 'w') as file:
    file.writelines(lines[1:])

# Output the saved file path
print(next_file)

