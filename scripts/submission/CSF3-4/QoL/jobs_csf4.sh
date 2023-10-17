#!/bin/bash

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

