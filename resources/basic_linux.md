# Basic UNIX terminal commands 

This page contains the most essential UNIX commands and the most common options for each of them.

> [!IMPORTANT]
> This are brief descriptions and the most common options.
> For more detailed information you can use `man [command]` command to get more information or, sometimes, use run the desired command with the `-h` (`command -h`) for more information.

## Sections 

- [File related commands](#file-related-commands)
- [Directory related commands](#directory-related-commands)
- [Cluster relateed commands](#cluster-related-commands)
- [Process management commands](#process-management-commands)
- [Git commands](#git-commands)

## File related commands

| Command  | Description                               | Examples                   | Common Options                                                              |
|----------|-------------------------------------------|----------------------------|-----------------------------------------------------------------------------|
| `ls`     | List files and directories in a directory.| `ls`                       | `-l`: Long format                                                           |
|          |                                           |                            | `-a`: Show hidden files                                                     |
|          |                                           |                            | `-h`: Human-readable sizes                                                  |
| `exa`    | Modern replacement for `ls`.              | `exa`                      | `-l`: Long format                                                           |
|          |                                           |                            | `-a`: Show hidden files                                                     |
|          |                                           |                            | `-h`: Human-readable sizes                                                  |
| `touch`  | Create an empty file or update timestamps.| `touch file.txt`           |                                                                             |
| `cat`    | Concatenate and display file content.     | `cat file.txt`             | `-n`: Number lines                                                          |
|          |                                           |                            | `-E`: Show line endings                                                     |
| `mv`     | Move or rename files and directories.     | `mv file1.txt newfile.txt` |                                                                             |
| `cp`     | Copy files or directories.                | `cp file1.txt file2.txt`   | `-r`: Recursive copy                                                        |
| `rm`     | Remove files or directories.              | `rm file.txt`              | `-f`: Force (careful)                                                       |
|          |                                           |                            | `-i`: Interactive                                                           |
|          |                                           |                            | `-r`: Recursive remove                                                      |
| `grep`   | Search for text patterns in files.        | `grep "pattern" file.txt`  | `-i`: Case-insensitive                                                      |
|          |                                           |                            | `-r`: Recursive search                                                      |
|          |                                           |                            | `-A NUM`: Prints the NUM number of lines after each match.                  |
|          |                                           |                            | `-B NUM`: Prints the NUM number of lines before each match.                 |
| `sed`    | Stream editor for text manipulation.      | `sed 's/old/new/' file.txt`| `-i`: saves the changes in the file instead of showing them in the terminal |
| `head`   | Display the beginning of a file.          | `head file.txt`            | `-n`: Number of lines to display (default 10)                               |
| `tail`   | Display the end of a file.                | `tail file.txt`            | `-n`: Number of lines to display (default 10)                               |
| `chmod`  | Change file permissions.                  | `chmod 755 file.txt`       | `-R`: Recursive                                                             |
|          |                                           | `chmod +x file.txt`        |                                                              |

## Directory related commands
| Command  | Description                         | Examples                | Common Options                                  |
|----------|-------------------------------------|-------------------------|-------------------------------------------------|
| `pwd`    | Print the current working directory.| `pwd`                   |                                                 |
| `cd`     | Change the current directory.       | `cd /path/to/directory` | `-`: Previous directory                         |
|          |                                     | `cd ..`                 |                                                 |
| `mkdir`  | Create a new directory.             | `mkdir new_dir`         | `-p`: Create parent dirs if they don't exist    |
| `rmdir`  | Remove empty directories.           | `rmdir empty_dir`       |                                                 |

## Cluster related commands
| Command  | Description                                   | Examples                              | Common Options                                                                                      |
|----------|-----------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------|
| `ssh`    | Securely connect to a remote server.          | `ssh username@hostname`               | `-i "~/.ssh/private_key"`: Specify private key                                                      |
| `sbatch` | Submit a batch job to a cluster.              | `sbatch script.job`                   |                                                                                                     |
| `scancel`| Cancel a pending or running job on a cluster. | `scancel job_id`                      |                                                                                                     |
| `squeue` | View job status on a cluster.                 | `squeue`                              | `squeue -u username`                                                                                |
| `rsync`  | Synchronize files and directories.            | `rsync source/ destination/`          | `-e "ssh -i ~/.ssh/private_key"`: for either remote source or destination with specific private key |
| `scp`    | Securely copy files between hosts.            | `scp file.txt username@hostname:/path`| `-i "~/.ssh/private_key"`: Specify private key                                                      |
| `sshfs`  | Mount a remote filesystem over SSH.           | `sshfs username@hostname:/path /mnt`  | `-o IdentityFile=/path/to/file/.ssh/private_key`: Specify private key                               |

## Process Management Commands 
| Command  | Description                            | Examples                | Common Options                                    |
|----------|----------------------------------------|-------------------------|---------------------------------------------------|
| `ps`     | List processes.                        | `ps`                    | `ps aux`: User-friendly format                    |
| `top`    | Monitor system processes in real-time. | `top`                   |                                                   |
| `kill`   | Terminate processes by ID or name.     | `kill PID`              |                                                   |
|          |                                        | `killall process_name`  |                                                   |
| `ping`   | Send ICMP echo requests to a host.     | `ping google.com`       |                                                   |
| `uname`  | Display system information.            | `uname -a`              |                                                   |
| `df`     | Display disk space usage.              | `df -h`                 |                                                   |
| `free`   | Display system memory usage.           | `free -m`               |                                                   |


## Git commands
| Command       | Description                                       | Examples                                            |
|---------------|---------------------------------------------------|-----------------------------------------------------|
| `git clone`   | Clone a Git repository.                           | `git clone <repository_url>`                        |
| `git init`    | Initialize a new Git repository.                  | `git init`                                          |
| `git status`  | Show the status of the working directory.         | `git status`                                        |
| `git log`     | Display commit history.                           | `git log`                                           |
| `git diff`    | Show changes between commits or working dir.      | `git diff`                                          |
| `git add`     | Stage changes for commit.                         | `git add file.txt`, `git add .`                     |
| `git commit`  | Commit staged changes.                            | `git commit -m "Commit message"`                    |
| `git branch`  | List branches in the repository.                  | `git branch`                                        |
| `git checkout`| Switch branches or restore working dir.           | `git checkout branch_name`, `git checkout file.txt` |
| `git merge`   | Merge changes from one branch into another.       | `git merge branch_name`                             |
| `git pull`    | Fetch changes from a remote repository and merge. | `git pull origin branch_name`                       |
| `git push`    | Push local changes to a remote repository.        | `git push origin branch_name`                       |
| `git remote`  | Manage remote repositories.                       | `git remote add origin <repository_url>`            |

