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
awk '{print $1, $4}' /mnt/iusers01/chem01/$USER/bin/squeue_jobs.txt | column -t > /mnt/iusers01/chem01/$USER/bin/current_jobs.txt

# Remove the temporary file
rm /mnt/iusers01/chem01/$USER/bin/squeue_jobs.txt

# Get the squeue information for user $USER
squeue -u $USER > /mnt/iusers01/chem01/$USER/bin/squeue_jobs.txt

# Compare the job IDs and save the unmatched job IDs to completed_jobs.txt
comm -3 <(awk '{print $1}' /mnt/iusers01/chem01/$USER/bin/current_jobs.txt | sort) <(awk '{print $1}' /mnt/iusers01/chem01/$USER/bin/squeue_jobs.txt | sort) > /mnt/iusers01/chem01/$USER/bin/completed_jobs.txt

# Check if completed_jobs.txt is empty
if [ -s /mnt/iusers01/chem01/$USER/bin/completed_jobs.txt ]; then
  # Print the number of completed jobs
  completed_jobs_count=$(wc -l < /mnt/iusers01/chem01/$USER/bin/completed_jobs.txt)
  echo "Number of completed jobs: $completed_jobs_count"

  # Add a timestamp to the completed jobs and append them to completed_jobs.txt
  date +"%Y-%m-%d %T" | awk -v OFS='\t' '{print $0}' >> /mnt/iusers01/chem01/$USER/bin/completed_jobs.txt
else
  echo "All jobs are still running."
fi

# Print the names of completed jobs
awk 'NR==FNR{a[$1];next} !($1 in a) {print $2}' /mnt/iusers01/chem01/$USER/bin/completed_jobs.txt /mnt/iusers01/chem01/$USER/bin/current_jobs.txt

# Delete the squeue_jobs.txt file
rm -f /mnt/iusers01/chem01/$USER/bin/squeue_jobs.txt
