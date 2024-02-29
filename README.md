![group logo](docs/logo_horizontal.png)

Welcome to the **Trujillo Research Group**, this repository contains useful documentation, tutorials, resources and scripts useful for your daily research.
It is especially convenient for new members of the team, either undergrad, master or PhD students.

Contributing to this repository is the perfect way to get familiar with the GitHub repositories, code documentation and tutorial writing.
Do not hesitate to collaborate, provide feedback or ask for any help from other members of the team.

Should you find any gaps in this repository, be it Tutorial, Software, or Scripts, please take the time to fill this gap! If you can't, then please place it in the **[To-Do](#to-do)** section below.

> **"The whole is greater than the sum of its parts"**


Checking the [Getting Started](tutorials/getting_started) section is highly recommended for new members as well. Particularly the **guidelines for good practice**.

# Resources
- **[Basic UNIX Commands](tutorials/getting_started/basic_linux.md)**
- **[Basic VI](tutorials/getting_started/basic_vi.md)**
- **[Web Resources](resources/README.md)**
- **[Software Treats](resources/software_treats.md)**
- **[SSH Set Up](tutorials/getting_started/ssh_setup.md)**
- **[Windows Set Up](tutorials/getting_started/windows_users.md)**
- **[Image Formats](resources/image_formats/README.md)**
- **[Presentation Template](resources/presentation)**

# Links to tutorials
- **[Your first Gaussian optimisation](tutorials/gaussian_submission/README.md)**
- **[Your first Reaction Path](tutorials/gaussian_submission/SN2_tutorial/README.md)**
- **[Gaussian Errors](tutorials/gaussian_errors/README.md)**
- **[Transition State Searching](tutorials/TS/README.md)**
- **[Molecular Electrostatic Potential](tutorials/MEP/README.md)**
- **[CREST](tutorials/CREST/README.md)**
- **[NBO](tutorials/NBO/README.md)**
- **[AIMAll](tutorials/AIMAll/README.md)**

# Group scripts

General scripts and modules for Trujillo Group.
```
├── scripts               may contain common bash or python useful for the group
|    ├── submission       submission scripts for CSF3/4 and ICHEC
|    └── analysis         scripts for quick assessment of calculation
├── config                useful configs for setup on either local machine or cluster
|    ├── bashrc           e.g. useful aliases
|    ├── ssh              setup of config files
|    └── vim              useful code highlighting or Plugins
└──tutorials              Step by step tutorials about different things  
     ├── basic_linux      Basic linux commands for beginners 
     └── MEP              Step by step MEP with Gaussian, MultiWFN & Jmol
```

## Guidelines for uploading scripts

When you upload some scripts on the repository, you have to think that these must be understandable for the general end-user. Thus, each uploaded script must meet the following criteria:
1. It must work and be up-to-date. 
2. It must be documented (docstrings, comments, etc. should always be present in order to help the user).
3. It must be human-readable (for Python, check the PEP-8 style guide, [link](https://peps.python.org/pep-0008/)).
4. It must be general (i.e., it should work in all the possible scenarios related to the purpose of the script).
5. It must not contain sensitive data (API keys, passwords, usernames, relative paths, etc.).
6. It must provide information about autorship and date of creation.

## How to upload files

- **Directly from the browser**: In the page repo, move to the subdirectory where you think the file you want to upload is more adapt. On the top right, click on `Add file` and then `Upload files`.

- **From the command line**: Clone the entire repo typing on the command line `git clone git@github.com:Trujillo-Group/General.git`,  enter the repo and add the file you want to add. Then, from the root of the repo, type: `git add *` , `git commit -m "added file xy Name Surname"` , `git push origin main`.


## To-Do
#### Resources
- Add (1) Link for Benchmark Papers (Tim / James)
- Add (1) Link for Methodology Papers (Tim / James)
#### Tutorials
- Add examples for each Gaussian Error (James / Diana)
- TS Tutorial (James)
- Orca Error Tutorial (Tim)
- Software Treats: Visualisation Tools (Diana), Design/Graphics (Iñigo), CLI things (Tim)
#### Scripts
- CSF script for CREST Submission
- CSF script for MEP Submission
