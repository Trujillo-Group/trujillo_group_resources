# Setting up Conda Environment

> [!IMPORTANT]  
> This can only be done in CSF3


1. qrsh -l short
2. module load apps/binapps/anaconda3/2022.10
3. conda create -n crest_env python==3.9.13
4. conda install -n crest_env xtb

# Installing Crest
1. Install the latest release version from this [link](https://github.com/crest-lab/crest/releases)
2. unzip crest.zip
3. place the crest file in your ~/bin on CSF
4. chmod u+x crest

# Using Crest
1. qrsh -l short
2. source activate crest-env
3. Do whatever you please with crest!

TBD: Create a jobscript to run Crest outside of the short interactive node.

