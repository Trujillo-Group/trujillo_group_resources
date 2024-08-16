![group logo](docs/figures/logo_horizontal.png)

Welcome to the **Trujillo Research Group**, this repository contains useful documentation, tutorials, resources and scripts useful for your daily research.
It is especially convenient for new members of the team, either undergrad, master or PhD students.

Contributing to this repository is the perfect way to get familiar with the GitHub repositories, code documentation and tutorial writing.
Do not hesitate to collaborate, provide feedback or ask for any help from other members of the team.

Should you find any gaps in this repository, be it Tutorial, Software, or Scripts, please take the time to fill this gap! If you can't, then please place it in the **[To-Do](#to-do)** section below.

> **"The whole is greater than the sum of its parts"**

Firstly, it is **mandatory** for members of the group to familiarise themselves with the [Guidelines for Conduct](resources/conduct).

Secondly the [Getting Started](tutorials/getting_started) section is highly recommended for new members. Particularly the **guidelines for good practice**.

# Resources
- **[Guidelines for Conduct](docs/guidelines)**
- **[Basic UNIX Commands](tutorials/getting_started/basic_linux.md)**
- **[Basic VI](tutorials/getting_started/basic_vi.md)**
- **[Web Resources](resources/README.md)**
- **[Software Treats](resources/software_treats.md)**
- **[SSH Set Up](tutorials/getting_started/ssh_setup.md)**
- **[Windows Set Up](tutorials/getting_started/windows_users.md)**
- **[Image Formats](resources/image_formats/README.md)**
- **[Gaussian Errors](resources/gaussian_errors/README.md)**
- **[Submission Workflows](resources/workflows/README.md)**

# Tutorials
- **[Your first Gaussian optimisation](tutorials/gaussian_submission/README.md)**
- **[Your first Reaction Path](tutorials/gaussian_submission/SN2_tutorial/README.md)**
- **[Transition State Searching](tutorials/TS/README.md)**
- **[MEP](tutorials/MEP/README.md)**
- **[CREST](tutorials/CREST/README.md)**
- **[NBO](tutorials/NBO/README.md)**
- **[AIMAll](tutorials/AIMAll/README.md)**

# Directories Overview

```
├── scripts                   
|    ├── submission           Submission scripts for CSF3/4 and ICHEC
|    └── analysis             Scripts for quick assessment of calculation
├── resources                 
|    ├── Image Formats        Information on image formatting
|    ├── Web Resources        Lots of information from DFT to visualisation tools
|    ├── Software Treats      Various packages to improve quality of life in the terminal
|    └── Gaussian Errors      Guide to reading the "flawless" Gaussian output files
└──tutorials                    
     ├── Getting Started      Various guides for first time setups
     ├── Gaussian Submission  Step by step guide submitted calculations using Gaussian
     ├── TS                   Step by step guide to finding Transition States
     ├── MEP                  Step by step MEP with Gaussian, MultiWFN & Jmol
     ├── CREST                Step by step Conformational Search tutorial with CREST
     ├── AIMAll               Step by step Atoms-In-Molecules tutorial with AIMAll & Gaussian
     └── NBO                  Step by step Non-Bonding Orbitals tutorial with Gaussian
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
- Workflow Manager (Tim / James)
- Add Link for Benchmark Papers (Tim / James)
- Add Link for Methodology Papers (Tim / James)
- Add examples for each Gaussian Error
- Add recommended softwares/websites for organisation
