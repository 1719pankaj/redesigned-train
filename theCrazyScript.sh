#!/bin/bash

# Get the current commit count and increment it for the commit message
commit_count=$(git rev-list --count HEAD)
new_commit_number=$((commit_count + 1))
commit_message="Auto commit #$new_commit_number"

# Add all files, including the script itself
git add --all

# Commit the changes with the incremented message
git commit -m "$commit_message"

# Push the changes to the remote repository
git push

echo "Successfully committed and pushed with message: '$commit_message'"
