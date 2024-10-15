![group logo](docs/figures/logo_horizontal.png)

Welcome to the **Trujillo Research Group**, this repository contains useful documentation, tutorials, resources and scripts useful for your daily research.
It is especially convenient for new members of the team, either undergrad, master or PhD students.

Contributing to this repository is the perfect way to get familiar with the GitHub repositories, code documentation and tutorial writing.
Do not hesitate to collaborate, provide feedback or ask for any help from other members of the team.

Should you find any gaps in this repository, be it Tutorial, Software, or Scripts, please take the time to fill this gap! If you can't, then please place it in the **[To-Do](#to-do)** section below.

> **"The whole is greater than the sum of its parts"**

Firstly, it is **mandatory** for members of the group to familiarise themselves with the [Group Guidelines](docs/guidelines).

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

## Guidelines for Uploading Scripts

When uploading scripts to the repository, ensure they are user-friendly and meet the following criteria:
1. **Functionality**: The script must work and be up-to-date.
2. **Documentation**: Include docstrings and comments to assist users.
3. **Readability**: Follow the PEP-8 style guide for Python scripts ([link](https://peps.python.org/pep-0008/)).
4. **Generality**: The script should be applicable in various scenarios related to its purpose.
5. **Security**: Avoid including sensitive data (API keys, passwords, usernames, etc.).
6. **Attribution**: Provide information about authorship and the date of creation.


## How to upload files

**Directly from the browser**

In the appropriate directory/subdirectory in the repo - `Add file` --> `Upload files`

**From the Command Line**

1. Clone the repository - `git clone git@github.com:Trujillo-Group/General.git`.

2. Enter the repo and add the file you want to add. 

3. From the root of the repo, type - `git add *` , `git commit -m "added file / changed file for X reason"`, `git push origin main`.

## Tasks
### 2024
**Tutorials**
- [ ] How to calculate redox potentials (@tire98 | @JamesOBrien02)
- [ ] Minimum-Energy Crossing Points (@tire98 | @JamesOBrien02)
- [ ] 

**Resources**
- [ ] Add Link for Benchmark Papers (@tire98 | @JamesOBrien02)
- [ ] Add Link for Methodology Papers (@tire98 | @JamesOBrien02)
- [ ] Add examples for each Gaussian Error (@JamesOBrien02 | @jak713)

**Scripts**
- [x] Update sub_csf3 to include AMD cores (@tire98)
- [ ] Workflow Manager (@tire98 | @JamesOBrien02)




## Repo Day
1. Clean up Repo.
2. Suggest/Add wanted scripts or tutorials.
3. Check over tutorials.
4. Incorporate new scripts into old tutorials.
5. Clean up old scripts.
6. Highlight underused scripts.
7. Add Posters/Presentations to Group-Seminars.
