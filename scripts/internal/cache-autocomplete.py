import os

from definitions import ROOT_PATH

# Check if the value is present and valid
if not ROOT_PATH:
    print("⚠️ ROOT_PATH environment variable is not set. This must be an absolute path.")
    exit(1)

script_names = []
for root, dirs, files in os.walk(f"{ROOT_PATH}/scripts"):
    for file in files:
        if file.endswith('.py') or file.endswith('.sh'):
            # Strip the extension from the file name
            script_name, _ = os.path.splitext(file)
            script_names.append(script_name)

# Write the script names to a cache file
with open(f"{ROOT_PATH}/storage/script-names-cache.txt", 'w') as f:
    for name in script_names:
        f.write(f"{name}\n")
