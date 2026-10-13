# Submission scripts
## CSF3
The queue manager on **CSF3** is SLURM and the scripts that create the submit files for orca and gaussian calculations are orca_rungen and gaussian_rungen, respectively.

### Usage

The scripts are written in python and can be run on CSF3/4 directly or from your local machine. The scripts need be stored in `~/bin` and need to be made executable by running `[sudo] chmod u+x foo`. The script can be invoked from any directory by calling its name and specifing the name of the input file and the number of cores required for the calculation. A help message is displayed when the script is called without any arguments.

**Example:**

`orca_rungen -i test.inp -c 20`

This will create a `run.sh` file in the current directory and will submit the calculation specified in `test.inp` to the `multicore` queue and allocates 20 cores.


#### CSF3

**orca_rungen** - ORCA 6.1.0

**gaussian_rungen** - Gaussian16, Gaussian16, NBO7 (g16)

**m_rungen** - Multiwfn
