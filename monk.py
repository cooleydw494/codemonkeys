#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys

from modules.internal.find_script import find_script
from definitions import ROOT_PATH

# Check if the value is present and valid
if not ROOT_PATH:
    print("⚠️ ROOT_PATH environment variable is not set. This must be an absolute path.")
    exit(1)

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

# If there is no argument, use 'help'
if args.command_name is None:
    args.command_name = 'help'

# If the user is not running the script (using the other flags), do not do warn them about the setup script
if args.command_name in ['install'] and not (args.edit or args.print or args.copy_path or args.copy_contents):
    answer = input(
        "⚠️ You are about to run install with the monk command. If you can run the monk command you likely have "
        "already installed code-monkeys, and running this script may not be a good idea because it is not designed "
        "to handle post-install edge cases. This is not suggested. Are you sure you want to continue? (y/n): ")
    if answer.lower() == 'y':
        print("🚀 Starting the setup... Hang tight! 🌟")
    else:
        if answer.lower() == 'n':
            print("🚀 Aborting setup... 🌟")
            sys.exit(0)
        else:
            print("Invalid input. Aborting setup... 🌟")
        sys.exit(1)


script_path = find_script(args.command_name)

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
