#!/bin/bash

# N.B. For this script to work you must have a bin folder in your home directory. (This script will create the necessary files in this folder.)

# This script will check the status of your jobs on CSF4
# and print the number of running and pending jobs.

# Define the colors
GREEN=$(tput setaf 2)
DEFAULT=$(tput sgr0)

echo "${GREEN}------ Current Jobs ------${DEFAULT}"

# Get the number of running jobs
running_jobs=$(squeue -u $USER | awk '$7 == "R" {print}' | wc -l)

# Get the number of pending jobs
pending_jobs=$(squeue -u $USER | awk '$7 == "PD" {print}' | wc -l)

# Get the total number of jobs
total_jobs=$((running_jobs + pending_jobs))

# Print the results
echo "You currently have:"
echo "  $running_jobs jobs running"
echo "  $pending_jobs jobs pending"
echo "Total: $total_jobs"

echo "${GREEN}----- Completed Jobs -----${DEFAULT}"

# Run the squeue command and store the output in a temporary file
squeue -u $USER > /mnt/iusers01/chem01/$USER/bin/squeue_jobs.txt

# Use awk to remove the first column and then use the column command to format the output into two separate columns
awk '{print $1, $4}' /mnt/iusers01/chem01/$USER/bin/squeue_jobs.txt | column -t > /mnt/iusers01/chem01/$USER/bin/temp_current_jobs.txt

# Remove squeue_jobs.txt
rm /mnt/iusers01/chem01/$USER/bin/squeue_jobs.txt

# Create the temporary completed jobs file
touch /mnt/iusers01/chem01/$USER/bin/temp_completed_jobs.txt

# Compare current_jobs.txt to squeue_jobs.txt and add any jobs which are in current_jobs.txt but not in squeue_jobs.txt to completed_jobs.txt
grep -v -f /mnt/iusers01/chem01/$USER/bin/temp_current_jobs.txt /mnt/iusers01/chem01/$USER/bin/current_jobs.txt > /mnt/iusers01/chem01/$USER/bin/temp_completed_jobs.txt

# copy temp_current_jobs.txt to current_jobs.txt
cp -f /mnt/iusers01/chem01/$USER/bin/temp_current_jobs.txt /mnt/iusers01/chem01/$USER/bin/current_jobs.txt
rm /mnt/iusers01/chem01/$USER/bin/temp_current_jobs.txt

# Get the current date and time
current_date_time=$(date "+%Y-%m-%d %H:%M:%S")

# Check if temp_completed_jobs.txt is empty
if [ -s /mnt/iusers01/chem01/$USER/bin/temp_completed_jobs.txt ]; then
  # Append the contents of temp_completed_jobs.txt to completed_jobs.txt (following a line break) with an extra column containing the date and time
  awk -v date_time="$current_date_time" '{print $0, date_time}' ORS="\n" /mnt/iusers01/chem01/$USER/bin/temp_completed_jobs.txt >> /mnt/iusers01/chem01/$USER/bin/completed_jobs.txt

  # Echo the contents of temp_completed_jobs.txt to the terminal after "Newly Completed Jobs:"
  echo "Newly Completed Jobs:"
  cat /mnt/iusers01/chem01/$USER/bin/temp_completed_jobs.txt

  # Remove temp_completed_jobs.txt
  rm /mnt/iusers01/chem01/$USER/bin/temp_completed_jobs.txt
else
  # Echo "No new jobs completed since last check"
  echo "No new jobs completed since last check"

  # Remove temp_completed_jobs.txt
  rm /mnt/iusers01/chem01/$USER/bin/temp_completed_jobs.txt
fi
