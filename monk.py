#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the value of BASE_DIR_ABS_PATH from the environment
base_dir_abs_path = os.getenv("BASE_DIR_ABS_PATH")

# Check if the value is present and valid
if not base_dir_abs_path:
    print("⚠️ BASE_DIR_ABS_PATH environment variable is not set. This must be an absolute path.")
    exit(1)

# Directory where the scripts are located
scripts_dir = os.path.join(base_dir_abs_path, "scripts")

# Parse command line arguments
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()  # Create a mutually exclusive group
group.add_argument('-e', '--edit', action='store_true', help='Open the script in vim')
group.add_argument('-p', '--print', action='store_true', help='Print the contents of the script to the terminal')
group.add_argument('-cp', '--copy_path', action='store_true',
                   help='Copy the absolute path of the script to the clipboard')
group.add_argument('-cc', '--copy_contents', action='store_true', help='Run the script')
parser.add_argument('command_name', nargs='?', help='The name of the script to run')
args = parser.parse_args()

# If the command_name is 'install', 'reinstall', or 're-install', print an error and exit
if args.command_name in ['install', 'reinstall', 're-install']:
    print("⚠️  Do not re-install code-monkeys with the install script")
    sys.exit(1)

# Run the Python script helpers and get the path of the script to run
# Using subprocess.call() because it needs to be interactive
exit_code = subprocess.call([sys.executable, os.path.join(scripts_dir, "internal/find-script.py"), args.command_name])

# If the exit code is not 0, exit
if exit_code != 0:
    sys.exit(exit_code)

# Set script path by reading the file at base path /storage/found-script.txt
with open(os.path.join(base_dir_abs_path, "storage/txt/found-script.txt"), "r") as f:
    script_path = f.read()

# If the script_path is empty, exit
if not script_path:
    sys.exit(1)

# Check if open_in_editor is true, if so, open the script in vim and exit
if args.edit:
    subprocess.run(['vim', script_path.strip()])
    sys.exit(0)

if args.print:
    print(script_path.strip())
    subprocess.run(['cat', script_path.strip()])
    sys.exit(0)

if args.copy_path:
    subprocess.run(['pbcopy'], input=script_path.strip().encode('utf-8'))
    print("✅ Copied script absolute path to clipboard")
    sys.exit(0)

if args.copy_contents:
    subprocess.run(['pbcopy'], input=open(script_path.strip(), 'rb').read())
    print("✅ Copied script contents to clipboard")
    sys.exit(0)

# Get the extension of the script
extension = os.path.splitext(script_path.strip())[1]

# Run the script with the provided arguments
if extension == ".sh":
    subprocess.call(['bash', script_path.strip()] + sys.argv[2:])
elif extension == ".py":
    subprocess.call([sys.executable, script_path.strip()] + sys.argv[2:])
else:
    print(f"⚠️ Unsupported script type: {extension}")
    sys.exit(1)
