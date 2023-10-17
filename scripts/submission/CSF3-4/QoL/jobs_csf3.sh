#!/bin/bash

# Get the number of running jobs
running_jobs=$(qstat -u $USER | awk '$5 == "r" {print}' | wc -l)

# Get the number of pending jobs
pending_jobs=$(qstat -u $USER | awk '$5 == "qw" {print}' | wc -l)

# Get the total number of jobs
total_jobs=$((running_jobs + pending_jobs))

# Print the results
echo "You currently have:"
echo "  $running_jobs jobs running"
echo "  $pending_jobs jobs pending"
echo "Total: $total_jobs" 
