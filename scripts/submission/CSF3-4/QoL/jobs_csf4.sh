#!/bin/bash

# N.B. For this script to work you must have a bin folder in your home directory on CSF. (This script will create the necessary files in this folder.)

# Checks the status of your jobs on CSF4
# Notifies of any completed jobs since last checked. (Requires consistent use)
# Pushes completed jobs to a file in your /bin directory

# Define the colors
GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
LIGHT_BLUE=$(tput setaf 6)
DEFAULT=$(tput sgr0)

echo "${GREEN}------ Current Jobs ------${DEFAULT}"

# Retreive the number of running and pending jobs
running_jobs=$(squeue -u $USER | awk '$7 == "R" {print}' | wc -l)
pending_jobs=$(squeue -u $USER | awk '$7 == "PD" {print}' | wc -l)
total_jobs=$((running_jobs + pending_jobs))

# Print the results
echo "You currently have:"
echo "  $running_jobs jobs running"
echo "  $pending_jobs jobs pending"
echo "Total: $total_jobs"
echo "${GREEN}----- Completed Jobs -----${DEFAULT}"

# Run the squeue command and store the output in a temporary file
squeue -u $USER > /mnt/iusers01/chem01/$USER/bin/.squeue_jobs.txt

# Use awk to remove the first column and then use the column command to format the output into two separate columns
awk '{print $1, $4}' /mnt/iusers01/chem01/$USER/bin/.squeue_jobs.txt | column -t > /mnt/iusers01/chem01/$USER/bin/.temp_current_jobs.txt
rm /mnt/iusers01/chem01/$USER/bin/.squeue_jobs.txt

# Retreive the completed jobs
touch /mnt/iusers01/chem01/$USER/bin/.temp_completed_jobs.txt
grep -v -f /mnt/iusers01/chem01/$USER/bin/.temp_current_jobs.txt /mnt/iusers01/chem01/$USER/bin/.current_jobs.txt > /mnt/iusers01/chem01/$USER/bin/.temp_completed_jobs.txt

# Update current_jobs.txt
cp -f /mnt/iusers01/chem01/$USER/bin/.temp_current_jobs.txt /mnt/iusers01/chem01/$USER/bin/.current_jobs.txt
rm /mnt/iusers01/chem01/$USER/bin/.temp_current_jobs.txt

current_date_time=$(date "+%Y-%m-%d %H:%M:%S")

  # Push completed jobs to file and return results
if [ -s /mnt/iusers01/chem01/$USER/bin/.temp_completed_jobs.txt ]; then
  awk -v date_time="$current_date_time" '{print $0, date_time}' ORS="\n" /mnt/iusers01/chem01/$USER/bin/.temp_completed_jobs.txt >> /mnt/iusers01/chem01/$USER/bin/.completed_jobs.txt
  echo "${LIGHT_BLUE}Newly Completed Jobs:${DEFAULT}"
  cat /mnt/iusers01/chem01/$USER/bin/.temp_completed_jobs.txt
  rm /mnt/iusers01/chem01/$USER/bin/.temp_completed_jobs.txt
else
  echo "${RED}No new jobs completed since last check${DEFAULT}"
  rm /mnt/iusers01/chem01/$USER/bin/.temp_completed_jobs.txt
fi
