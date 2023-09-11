# General
General scripts and modules for Trujillo Group.
- `scripts`: may contain common bash or python useful for the group
  - `submission`: submission scripts for CSF3/4 and ICHEC
  - `analysis`: scripts for quick assessment of calculation
- `config`: useful configs for setup on either local machine or cluster
  - `bashrc`: e.g. useful aliases
  - `ssh`: setup of config files
  - `vim`: useful code highlighting or Plugins
- `thisCouldBeYourContribution`: Whatever you think is useful

# Guidelines for uploading scripts

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
