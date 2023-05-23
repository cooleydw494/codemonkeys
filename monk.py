#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from termcolor import colored

from definitions import ROOT_DIR_NAME

try:
    from modules.internal.find_script import find_script
    from modules.internal.monk_environment_checks import monk_environment_checks
except ImportError:
    print(colored("⚠️  CodeMonkeys must be 'installed' as a source package. Please run the `setup.py` script.", 'red'))
    exit(1)

monk_environment_checks()

# Create argument parser - use custom help
parser = argparse.ArgumentParser(add_help=False)
# Flags
# TODO: implement -v --version flag
parser.add_argument('-v', '--version', action='store_true')
parser.add_argument('-h', '--help', action='store_true')

# Flags - mutually exclusive
group = parser.add_mutually_exclusive_group()
group.add_argument('-e', '--edit', action='store_true')
group.add_argument('-p', '--print', action='store_true')
group.add_argument('-cp', '--copy_path', action='store_true',
                   help='Copy the absolute path of the script to the clipboard')
group.add_argument('-cc', '--copy_contents', action='store_true')

parser.add_argument('command_name', nargs='?')
args = parser.parse_args()
flag_args_present = any([arg.startswith('-') for arg in sys.argv[1:]])

if args.command_name is None and (args.help is True):
    args.command_name = 'help'

# If the user is not running the script (using the other flags), do not do warn them about the setup script
if args.command_name in ['install'] and flag_args_present is False:
    answer = input(
        "⚠️ You are about to run install with the monk command. If you can run the monk command you likely have "
        f"already installed {ROOT_DIR_NAME}, and running this script may not be a good idea because it is not designed "
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
