## Installing Crest

1. Install the latest release version from this [link](https://github.com/crest-lab/crest/releases)
1. unzip crest.zip
1. place the crest file in your ~/bin on CSF
1. chmod u+x crest

# CSF3-4

## Setting up Conda Environment

> Only need to do once & on either CSF **not** both

### CSF3

```
qrsh -l short
module load apps/binapps/anaconda3/2022.10
conda create -n crest_env python==3.9.13
conda config -n crest_env --add channels conda-forge
```

### CSF4

```
srun --pty bash
module load anaconda3/2022.10
conda create -n crest_env python==3.9.13
conda config -n cres_env --add channels conda-forge
```

## Accessing Crest

### CSF3

```
qrsh -l short
module load apps/binapps/anaconda3/2023.09
source activate crest_env
```

### CSF4

1. Decide on No. of cores
   Single core:

```
srun --pty bash
```

Multiple cores:

```
srun -p multicore -n [No. of Cores] --pty bash
```

2. Load Conda environment

```
module load anaconda3/2022.10
source activate crest_env
```

##### Done!

## Using Crest

Recommended energy window (Smaller Systems): 3 kcal/mol.<sup>[Ref.](https://onlinelibrary.wiley.com/doi/10.1002/anie.202205735)</sup>
Recommended energy window (Larger Systems): 6 kcal/mol.

### Option 1: Interactive Session

```
crest input.xyz --gfn2 --alpb Ether --T 1 > crest.out
```

Flags:

- `--gfn2`: Use GFN2-xTB method
- `--alpb`: Solvent model followed by solvent name
- `--T`: Number of cores

Commands available via the [Crest documentation](https://crest-lab.github.io/crest-docs/page/documentation)

### Option 2: Batch Submission

1. Download [sub_csf4_crest](../../scripts/submission/CSF3-4/CREST/sub_csf4_crest) and put it in your CSF bin
1. `sub_csf4_crest -i input.xyz [-s] [solvent] [-c] [cores] [-ch] [charge] [-m] [multiplicity] [-e] [energy window (kcal/mol)]`

Allows the user to run crest without requiring an interactive session.

## RMSD

Sometimes (most times) you may obtain 100s+ of potential conformers. Many of these are can be structurally very similar, and the root-mean-square deviation (RMSD) of Cartesian coordinates between two conformers can be used as a structure based metric to narrow down the number of conformers.
Different RMSD algorithms exist which have been implemented in various python packages. Our group has made use of the [rmsd](https://github.com/charnley/rmsd) package and more recently the symmetry corrected RMSD algorithm implemented in [symmrmsd](https://github.com/RMeli/spyrmsd/tree/develop). `symmrmsd` is a more recent implementation and is recommended for use since the symmetry of the molecule is taken into account and duplicates are removed.

### Setting up RMSD

> Many of these setup steps can be done in alternative/more efficient ways, the steps provided are the ones which worked for me (James), so if you know what you are doing feel free to use seperate scripts etc.

1. Install [RMSD](https://github.com/iribirii/rmsd) (Iribirii's version)
1. Install [crestparse.py](https://github.com/juhesiit/crestparse)
1. Download the [rmsd.ipynb Jupyter Notebook](tbd)
1. Copy the following to your bin folder:
   - rmsd/calculate_rmsd.py
   - crestparse.py
   - rmsd.ipynb

### Using RMSD

**N.B.** The Jupyter Notebook deletes the conformers that don't make the cutoff. It is **very** important you run this notebook on a backup of your files.

1. Extract all of your .xyz files from crest_conformers.xyz to a new file called rmsd

```
mkdir rmsd
cd rmsd
crestparse.py ../crest_conformers.xyz -e
```

2. Run rmsd.ipynb

1. Repeat with varied  `rmnsd_cutoff` and `energy_cutoff` values until you get the required number of conformers

### Symmetry Corrected RMSD

For further information on the symmetry corrected RMSD algorithm, please refer to the [spyrmsd](https://spyrmsd.readthedocs.io/en/develop/) documentation or their [publication](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-020-00455-2).
A script that can be used for filtering conformers based on symmetry corrected RMSD is available [here](../../scripts/analysis/spyrmsd_filter.py).
This script relies on the `spyrmsd`, `numpy`, `pandas`, `pymatgen` and an `openbabel` installation. Consider creating a virtual environment to install the required packages.
The symmetry mode can be turned off by using the `--no_sym` flag. The script has been tested on the output of CREST and GOAT conformer generation methods. In addition to structure based filtering, the script can also be used to filter conformers based on the Boltzmann distribution of the conformers and for printing the ensemble properties. This allows for selecting those conformers which are most likely to be populated at a given temperature. The population threshold can be set manually using the `--population_threshold_conformers` flag. Hence, the following flags are available:
```
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        .xyz file with conformers
  --output OUTPUT, -o OUTPUT
                        Name of the output file, format will be .xyz and contains the filtered conformers
  --threshold THRESHOLD, -t THRESHOLD
                        RMSD threshold for filtering
  --backend BACKEND, -b BACKEND for the graph used by spyrmsd, default is rustworkx
                        Graph backend, e.g. networkx or rustworkx
  --no_sym              Do not use symmetry correction, by default symmetry correction is used
  --no_strip            Do not strip hydrogens from the conformers, by default hydrogens are stripped
  --no_center           Do not center the conformers at origin, by default conformers are centered
  --no_minimize         Do not calculate minimum RMSD, by default minimum RMSD is calculated
  --print_ensemble_properties, -prop
                        Print ensemble
  --population_threshold_conformers, -pop POPULATION_THRESHOLD_CONFORMERS,  
                        Conformer structures with cummulative population below this threshold. 
  --population_temperature_conformers, -temp POPULATION_TEMPERATURE_CONFORMERS
                        Temperature for population calculation in [K], default is 298.15 K
```

An example of how to use the script is as follows:
```bash
python spyrmsd_filter.py -i crest_conformers.xyz -o filtered_conformers.xyz --symmetry_mode --rmsd_cutoff 0.5 --population_threshold_conformers 99
```

This will filter the conformers based on the symmetry corrected RMSD and conformers with an RMSD of 0.5 or less will be removed. The script will also create an .xyz file with those conformers which represent 99% of the population at 298.15 K, and .csv file with the ensemble properties.
