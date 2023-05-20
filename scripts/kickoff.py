#!/usr/bin/env python3

import subprocess
import sys

# Get the arguments passed to kickoff.py
args = sys.argv[1:]

# Create the command to run main.py with the arguments
command = ["python", "main.py"] + args

# Run the command
subprocess.run(command)
