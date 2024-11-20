#!/bin/bash

# Get the current commit count and increment it for the commit message
commit_count=$(git rev-list --count HEAD)
new_commit_number=$((commit_count + 1))
commit_message="Auto commit #$new_commit_number"

#Run eneumerator
python3 /home/ubuntu/gitshit/iShitYouNot.py

# Log file
log_file="commit_log.md"

# Add a horizontal line for separation in the log file
echo -e "\n\n---\n\n" >> "$log_file"

# Log the entire command line output to commit_log.md
{
    # Add all files
    git add --all

    # Commit the changes with the incremented message
    git commit -m "$commit_message"

    # Push the changes to the remote repository
    git push
} >> "$log_file" 2>&1  # Redirect both stdout and stderr to the log file

# Log successful commit details separately
echo "Successfully committed and pushed with message: '$commit_message'" >> "$log_file"
echo "Logged last commit details to $log_file"
#!/bin/bash

# Get the current commit count and increment it for the commit message
commit_count=$(git rev-list --count HEAD)
new_commit_number=$((commit_count + 1))
commit_message="Auto commit #$new_commit_number"

# Log file
log_file="commit_log.md"

# Add a horizontal line for separation in the log file
echo -e "\n\n---\n\n" >> "$log_file"

# Log the entire command line output to commit_log.md
#!/bin/bash

# Get the current commit count and increment it for the commit message
commit_count=$(git rev-list --count HEAD)
new_commit_number=$((commit_count + 1))
commit_message="Auto commit #$new_commit_number"

# Log file
log_file="commit_log.md"

# Add a horizontal line for separation in the log file
echo -e "\n\n---\n\n" >> "$log_file"

# Log the entire command line output to commit_log.md
{
    # Add all files
    git add --all

    # Commit the changes with the incremented message
    git commit -m "$commit_message"

    # Push the changes to the remote repository
    git push
} >> "$log_file" 2>&1  # Redirect both stdout and stderr to the log file

# Log successful commit details separately
echo "Successfully committed and pushed with message: '$commit_message'" >> "$log_file"
echo "Logged last commit details to $log_file"
