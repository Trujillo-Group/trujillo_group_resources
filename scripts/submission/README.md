# Submission scripts
## CSF3/4
The queue manager on **CSF3** is Sun Grid Engine (SGE) and the scripts that create the submit files for orca and gaussian calculations are orca_rungen_csf3 and gaussian_rungen_csf3, respectively.

The queue manager on **CSF4** is SLURM and requires a different run.sh file. The \*\_csf4 scripts generate the respective file.
### Usage
The scripts are written in python and can be run on CSF3/4 directly or from your local machine. The scripts need be stored in `~/bin` and need to be made executable by running `[sudo] chmod u+x foo`. The script can be invoked from any directory by calling its name and specifing the name of the input file and the number of cores required for the calculation. A help message is displayed when the script is called without any arguments.

**Example:**

`orca_rungen_csf4 -i test.inp -c 20`

This will create a `run.sh` file in the current directory and will submit the calculation specified in `test.inp` to the `multicore` queue and allocates 20 cores.
### Local Machine
The script can be run from a local machine as well. Store the script in `~/bin` and make it executeable. You might have to adjust the shebang to give the correct python path.
