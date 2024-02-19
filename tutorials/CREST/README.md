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
Commands available via the [Crest documentation](https://crest-lab.github.io/crest-docs/page/documentation)

