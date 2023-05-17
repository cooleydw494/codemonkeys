import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Get the value of BASE_DIR_ABS_PATH from the environment
base_dir_abs_path = os.getenv("BASE_DIR_ABS_PATH")

# Check if the value is present and valid
if not base_dir_abs_path:
    print("⚠️ BASE_DIR_ABS_PATH environment variable is not set. This must be an absolute path.")
    exit(1)

script_names = []
for root, dirs, files in os.walk(f"{base_dir_abs_path}/scripts"):
    for file in files:
        if file.endswith('.py') or file.endswith('.sh'):
            # Strip the extension from the file name
            script_name, _ = os.path.splitext(file)
            script_names.append(script_name)

# Write the script names to a cache file
with open(f"{base_dir_abs_path}/storage/script-names-cache.txt", 'w') as f:
    for name in script_names:
        f.write(f"{name}\n")

