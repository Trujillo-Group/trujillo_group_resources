## Installing Crest
1. Install the latest release version from this [link](https://github.com/crest-lab/crest/releases)
2. unzip crest.zip
3. place the crest file in your ~/bin on CSF
4. chmod u+x crest

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


### Option 1
```
crest input.xyz --gfn2 --alpb Ether --T 1
```

Commands available via the [Crest documentation](https://crest-lab.github.io/crest-docs/page/documentation)

### Option 2


1. Download [sub_csf4_crest](../../scripts/submission/CSF3-4/CREST/sub_csf4_crest) and put it in your CSF bin
2. ```sub_csf4_crest -i input.xyz [-s] [solvent] [-c] [cores] [-ch] [charge] [-m] [multiplicity] [-e] [energy window (kcal/mol)]```

Allows the user to run crest without requiring an interactive session.

## RMSD

Sometimes (Most times) you may obtain 100s+ of potential conformers. A lot of these are often very similar, and a method to separate conformers is to use the statistical model 'root means squared difference' (RMSD) to further distinguish the structures across their conformational space.

### Setting up RMSD
> Many of these setup steps can be done in alternative/more efficient ways, the steps provided are the ones which worked for me (James), so if you know what you are doing feel free to use seperate scripts etc.

1. Install [RMSD](https://github.com/iribirii/rmsd) (Iribirii's version)
2. Install [crestparse.py](https://github.com/juhesiit/crestparse)
3. Download the [rmsd.ipynb Jupyter Notebook](tbd)
4. Copy the following to your bin folder:
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

3. Repeat with varied  ``rmnsd_cutoff`` and ```energy_cutoff``` values until you get the required number of conformers 