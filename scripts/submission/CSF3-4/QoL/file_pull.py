#!/usr/bin/Python3
import sys
import subprocess

# Get the source directory from the command line argument
source_dir = sys.argv[1]

# Locating the username
result = subprocess.run(['whoami'], capture_output=True, text=True)
username = result.stdout.strip()


# Construct the rsync command with the source and destination directories
rsync_cmd = ['rsync', '-avz', f'{username}@csf3.itservices.manchester.ac.uk:{source_dir}', '.']

# Execute the rsync command
subprocess.run(rsync_cmd)