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

# Log the last 10 commit messages into commit_log.md
log_file="commit_log.md"
echo -e "\n\n---\n\n" >> "$log_file"  # Add a horizontal line (markdown)

# Get the last 10 commit messages and append them to the commit_log.md
git log -n 10 --pretty=format:"%h - %s" >> "$log_file"

echo "Successfully committed and pushed with message: '$commit_message'"
echo "Logged last 10 commits to $log_file"
