#!/bin/bash

# Check if a commit message argument is provided
if [ -z "$1" ]; then
  echo "❌ Error: No commit message provided."
  echo "Usage: commit \"Your commit message\""
  exit 1
fi

echo "🔍 Staging changes..."

# Run git add, displaying only error output
add_result=$(git add . 2>&1 >/dev/null)

# Check if git add was successful
if [ $? -ne 0 ]; then
  echo "❌ Error adding files to staging area:"
  echo "$add_result"
  exit 1
fi

echo "✅ Changes staged"

echo "🚀 Committing changes"

# Run git commit, displaying only error output
commit_result=$(git commit -m "$1" 2>&1)

# If git commit was not successful, display the error message
if [ $? -ne 0 ]; then
  echo "❌ Error committing changes:"
  echo "$commit_result"
  exit 1
fi

# Display commit stats
echo "📊 Commit stats:"
# the options for detail of the git diff command are:
git diff --summary HEAD^

# Run git push, capturing any error output
  push_result=$(git push 2>&1)

  # Check if git push was successful
  if [ $? -ne 0 ]; then
    # Check for specific error message indicating a pull is needed first
    if [[ "$push_result" == *"Updates were rejected"* ]]; then
      echo "❌ Error pushing changes:"
      echo "It looks like the remote repository has changes that you don't have yet. Please pull those changes and resolve any conflicts before pushing again. 🔄"
    else
      echo "❌ Error pushing changes:"
      echo "$push_result"
    fi
    exit 1
  fi
  echo "✅ Push successful!"
