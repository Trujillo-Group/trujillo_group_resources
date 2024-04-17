#!/bin/bash

# This script uses Multiwfn to convert all the files with the .wfx extension (filename.wfx) to filename_CRIT.txt files

# Define the path to Multiwfn, path given below is just an example
multiwfn_path="/home/user/Downloads/Multiwfn_3.8_dev_bin_Linux_noGUI/Multiwfn"

# Read options from mep_options.txt, which must be present in your working directory OR included in PATH in your bash profile
mep_options=$(<mep_options.txt)

# Loop through all files with the .wfx extension in the current directory
for file in *.wfx; do
    # Check if the file exists and is readable
    if [ -r "$file" ]; then
        # Run Multiwfn with specified options
        echo "Running Multiwfn on $file..."
        echo "$mep_options" | "$multiwfn_path" "$file" > /dev/null
        
        # Rename the output file
        mv surfanalysis.txt "${file%.wfx}_CRIT.txt"
        
        echo "Multiwfn analysis completed for $file"
    else
        echo "Error: File $file not found or not readable."
    fi
done
