# Setting up Conda Environment (CSF3)
```
qrsh -l short
module load apps/binapps/anaconda3/2022.10
conda create -n crest_env python==3.9.13
conda config -n crest_env --add channels conda-forge

```

# Installing Crest
1. Install the latest release version from this [link](https://github.com/crest-lab/crest/releases)
2. unzip crest.zip
3. place the crest file in your ~/bin on CSF
4. chmod u+x crest

# Using Crest (CSF3)
```
qrsh -l short
source activate crest_env
```
Commands available via the [Crest documentation](https://crest-lab.github.io/crest-docs/page/documentation)

# Using Crest (CSF4)

Open interactive Session

Single core:
```
srun --pty bash
```
Multiple cores:    
```
srun -p multicore -n [No. of Cores] --pty bash
source activate crest_env
```
Commands available via the [Crest documentation](https://crest-lab.github.io/crest-docs/page/documentation)

TBD: Create a jobscript to run Crest outside of the short interactive node.
