#!/usr/bin/env python3

import subprocess
import sys
import os

# Check if a commit message argument is provided
if len(sys.argv) < 2:
    print("❌ Error: No commit message provided.")
    print("Usage: commit \"Your commit message\"")
    sys.exit(1)

print("🔍 Staging changes...")

# Run git add, displaying only error output
add_result = subprocess.run(["git", "add", "."], universal_newlines=True, stderr=subprocess.PIPE)

# Check if git add was successful
if add_result.returncode != 0:
    print("❌ Error adding files to staging area:")
    print(add_result.stderr)
    sys.exit(1)

print("✅ Changes staged")

print("🚀 Committing changes")

# Run git commit, displaying only error output
commit_result = subprocess.run(["git", "commit", "-m", sys.argv[1]], universal_newlines=True, stderr=subprocess.PIPE)

# If git commit was not successful, display the error message
if commit_result.returncode != 0:
    print("❌ Error committing changes:")
    print(commit_result.stderr)
    sys.exit(1)

# Display commit stats
print("📊 Commit stats:")
subprocess.run(["git", "diff", "--stat", "--summary", "HEAD^"], universal_newlines=True)

# Run git push, capturing any error output
push_result = subprocess.run(["git", "push"], universal_newlines=True, stderr=subprocess.PIPE)

# Check if git push was successful
if push_result.returncode != 0:
    # Check for specific error message indicating a pull is needed first
    if "Updates were rejected" in push_result.stderr:
        print("❌ Error pushing changes:")
        print("It looks like the remote repository has changes that you don't have yet. Please pull those changes "
              "and resolve any conflicts before pushing again. 🔄")
    else:
        print("❌ Error pushing changes:")
        print(push_result.stderr)
    sys.exit(1)

print("✅ Push successful!")
