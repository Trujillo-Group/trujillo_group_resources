# ORCA submission scripts for CSF3/4
# ================================
This python script can be use as-is on CSF3/4 for creating and submitting ORCA jobs. Place the script in the same directory as your ORCA input file and run it from there, or place it in a directory that is in your PATH variable (e.g your ```bin``` in your csf3/4 home directory). Running the ```orca_rungen``` script will create a submission script named ```run.sh```. This script can be submitted to the slurm workload manager on CSF3/4.
The settings regarding the CSF configuration and ORCA version/additional software can be passed as arguments to the script. You can run the script in an interactive mode by running it with the ```-inter```/```--interactive``` flag. The submission script will apply the settings to the ORCA input file and submit the job to the respective queue, depending on the chosen configuration.

#### Available options:
```bash
$ orca_rungen -h
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file name
  -n NODES, --nodes NODES
                        Number of nodes. multicore=1, multinode>1, serial=0; default=1
  -cpg CORES_PER_GROUP, --cores_per_group CORES_PER_GROUP
                        Number of cores per group
  -c CORES, --cores CORES
                        Number of cores
  -nbo, --nbo           Request NBO module; needed only if nbo analysis is requested in input file
  -o5, --orca5          Request Orca 5 module; default is Orca6.1
  -inter, --interactive
                        Run script interactively
  -s, --submit          Submit job after creating runscript
  ```

## CSF3 
The configuration for CSF3 outlined on the respective [documentation page](https://ri.itservices.manchester.ac.uk/csf3/overview/configuration/). If you want to run calculations in parallel, you can request up to 168 cores per node in the ```multicore``` queue. This script only creates scripts for the ```multicore``` queue, assuming the use of the amd nodes. If you want to use other nodes consult the [CSF3 documentation](https://ri.itservices.manchester.ac.uk/csf3/overview/configuration/) for the respective settings. 
The memory settings are adjusted automatically based on the chosen queue. The amd nodes have 8GB per core. If your job requires more memory, the [high memory queue](https://ri.itservices.manchester.ac.uk/csf3/batch-slurm/high-memory-jobs-slurm/) can be accessed by submitting your job to the ```himem```  in the orca input file.


## CSF4
The configuration for CSF4 outlined on the respective [documentation page](https://ri.itservices.manchester.ac.uk/csf4/overview/configuration/). The maximum number of cores per node is 40 in the multicore queue. More cores can be requested by using the multinode queue. We recommend using the amd queue on CSF3 if you need more than 40 cores!
The memory settings are adjusted automatically to ```%maxcore 4600``` in the orca input file. CSF4 does not have a high memory queue, so if you need more memory, you will have to switch to the amd or high memory queue on CSF3.


## Example usage
```bash
$ orca_rungen -i test.inp -c 20 -o5 -nbo
```
This script will create a submission script for an ORCA job with the input file ```test.inp```, requesting 20 cores, the ORCA5 version, and the NBO package.

```bash
$ orca_rungen -i test.inp -c 20 -cpg 4 -amd -s
```
This script will create a submission script for an ORCA6 job with the input file ```test.inp```, requesting 20 cores, four cores per group, and will automatically submit the job to the amd queue after the changes have been made to the input file.
You can also run the scripts in interactive mode by running them with the ```-inter```/```--interactive``` flag. This will prompt you for the necessary information.