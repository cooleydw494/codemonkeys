#!/usr/bin/env python3

import subprocess
import sys
import os

from pack.modules.custom.theme.theme_functions import print_t

# Check if a commit message argument is provided
if len(sys.argv) < 2:
    print_t("Error: No commit message provided.", 'error')
    print_t("Usage: commit \"Your commit message\"", 'info')
    sys.exit(1)

print_t("Staging local changes...", 'info')

# Run git add, displaying only error output
add_result = subprocess.run(["git", "add", "."], universal_newlines=True, stderr=subprocess.PIPE)

# Check if git add was successful
if add_result.returncode != 0:
    print_t("Error adding files to staging area:", 'error')
    print_t(add_result.stderr)
    sys.exit(1)

print_t("Changes staged... 🚀 Committing changes", 'success')

# Run git commit, displaying only error output
commit_result = subprocess.run(["git", "commit", "-m", sys.argv[1]], universal_newlines=True, stderr=subprocess.PIPE)

# If git commit was not successful, display the error message
if commit_result.returncode != 0:
    print_t("Error committing changes:", 'error')
    print_t(commit_result.stderr)
    sys.exit(1)

# Display commit stats
print_t("📊 Commit stats:", 'info')
subprocess.run(["git", "diff", "--stat", "--summary", "HEAD^"], universal_newlines=True)

# Run git push, capturing any error output
push_result = subprocess.run(["git", "push"], universal_newlines=True, stderr=subprocess.PIPE)

# Check if git push was successful
if push_result.returncode != 0:
    # Check for specific error message indicating a pull is needed first
    if "Updates were rejected" in push_result.stderr:
        print_t("Error pushing changes:", 'error')
        print_t("🔄 It looks like the remote repository has changes that you don't have yet. Please pull those changes "
              "and resolve any conflicts before pushing again.", 'info')
    else:
        print_t("Error pushing changes:", 'error')
        print_t(push_result.stderr)
    sys.exit(1)

print_t("Push successful!", 'done')
