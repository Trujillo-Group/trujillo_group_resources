# Submission scripts
## CSF3/4
The queue manager on **CSF3** is Sun Grid Engine (SGE) and the scripts that create the submit files for orca and gaussian calculations are orca_rungen_csf3 and gaussian_rungen_csf3, respectively.

The queue manager on **CSF4** is SLURM and requires a different run.sh file. The \*\_csf4 scripts generate the respective file.

### Usage

The scripts are written in python and can be run on CSF3/4 directly or from your local machine. The scripts need be stored in `~/bin` and need to be made executable by running `[sudo] chmod u+x foo`. The script can be invoked from any directory by calling its name and specifing the name of the input file and the number of cores required for the calculation. A help message is displayed when the script is called without any arguments.

**Example:**

`orca_rungen_csf4 -i test.inp -c 20`

This will create a `run.sh` file in the current directory and will submit the calculation specified in `test.inp` to the `multicore` queue and allocates 20 cores.


#### CSF4

**sub_csf4** - Gaussian16, NBO7 (g16), ORCA

**sub_csf4_g09** - Gaussian09

**sub_csf4_g16_bash** - Gaussian16

**sub_csf4_mep** - MEP

**sub_csf4_crest** - CREST

**sub_csf4_xtb** - xTB

#### CSF3

**sub_csf3** - Gaussian16, NBO7 (g16), ORCA

**sub_csf3_g09** - Gaussian09

**sub_csf3_mep** - MEP
