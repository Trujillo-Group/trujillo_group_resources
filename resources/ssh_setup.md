# Basic ssh setup 
## What is ssh?
SSH stands for Secure Shell and is a network protocol that allows you to connect to a remote machine and execute commands on it. It is a very useful tool for remote computing, as it allows you to work on a remote machine as if it was your local machine. You can use it to run programs, edit files, and even use graphical interfaces.
## How to use ssh?
To use ssh, you need to have an ssh client installed on your machine. On Linux and Mac, this is usually already installed. On Windows, you can use the [Windows Subsystem for Linux](./windows_users.md) to get a Linux distribution on your machine. You can then use the Linux terminal to connect to remote machines via ssh.
## How to connect to a remote machine via ssh?
To connect to a remote machine via ssh, you need to know the IP address of the machine and your username and password. The IP address is usually provided by the administrator of the machine. The username and password are the same as the ones you use to log into the machine.   
**CSF3**: 10.99.203.52
**CSF4**: 10.99.203.214 or 10.99.203.215, both work
Hence, to connect to CSF3, you would type the following into your terminal:
```bash
ssh <username>@10.99.203.52
```
If this is the first time you are connecting to this machine, you will be asked if you want to continue connecting. Type `yes` and press enter. You will then be asked for your password, followed by the two-factor authentication step. If you have entered everything correctly, you should now be logged into the remote machine and can start working on it.
## ssh config file
If you are using ssh a lot, it can be useful to create a config file that contains the IP addresses of the machines you are using. This way, you don't have to remember the IP addresses and can just type `ssh <username>@<machine>` to connect to the machine.
To create a config file, open a terminal and type:
```bash
touch ~/.ssh/config
```
This will create a file called `config` in your `.ssh` directory. You can then open this file in a text editor and add the following lines:
```bash
Host csf3
    HostName 10.99.203.52
    User <username>
Host csf4
    HostName 10.99.203.215
    User <username>
```
You can then save the file and close it. You can now connect to the machines by typing `ssh csf3` or `ssh csf4` into your terminal.

## ssh multiplexing
If you are using ssh a lot a lot and are especially annoyed by the two-factor authentication step, you can use ssh multiplexing to speed up the process. This will allow you to connect to a machine without having to enter your password and two-factor authentication code for the time that the connection is open.
To enable ssh multiplexing, open your ssh config file and add the following lines:
```bash
Host csf3
    HostName 10.99.203.52
    User <username>
    ControlPath ~/.ssh/cm-%r@%h:%p
    ControlMaster auto
Host 10.99.203.5*
    ControlPath ~/.ssh/cm-%r@%h:%p
    ControlMaster auto
    ControlPersist 8h
```
You can then save the file and close it. You can now connect to the machines by typing `ssh csf3` or `ssh csf4` into your terminal. The first time you connect to a machine, you will still have to enter your password and two-factor authentication code. However, if you then open a new ssh connection to the same machine, you will not have to enter your password and two-factor authentication code again. This will be the case for 8 hours, after which you will have to enter your password and two-factor authentication code again.
## ssh keys
If you are using ssh a lot, it can be useful to set up ssh keys. Depending on how the two-factor authentication is set up on the machine you are connecting to, this can allow you to connect to a machine without having to enter your password and two-factor authentication code. On CSF3 and CSF4, this is not possible, but ssh keys are still useful as they allow you to connect to a machine without having to enter your password.   
To set up ssh keys, open a terminal and type:
```bash
ssh-keygen -t ed25519
```
You will then be asked to enter a file in which to save the key. Press enter to save the key in the default location. You will then be asked to enter a passphrase. You can either enter a passphrase or leave it empty. If you leave it empty, you will not have to enter a passphrase when connecting to a machine. You will then be asked to enter the passphrase again. If you have entered a passphrase, you will have to enter it every time you connect to a machine. If you have not entered a passphrase, you will not have to enter a passphrase when connecting to a machine.   
SSH keys are also required for contributing to GitHub repositories via ssh. You can find more information on how to set up ssh keys for GitHub [here](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).

## sshfs
sshfs allows you to mount a remote machine's directory on your local machine. This means that you can access the files on the remote machine as if they were on your local machine. This can be very useful if you want to work on a remote machine but prefer to use your local editor.   
First, you need to create a mount point on your local machine. To do this, open a terminal and type:
```bash
mkdir /path/to/local/directory
```
You can then mount the remote machine on this directory.   
To use sshfs, you need to have fuse installed. On Mac this is software is not installed and not supported by Apple, so you will have to install it yourself (see [here](https://osxfuse.github.io/)). On Linux, fuse is usually already installed.   
To use sshfs, open a terminal and type:
```bash
sshfs <username>@<machine>:/path/to/remote/directory /path/to/local/directory
```
If you have your ssh config file set up, you can also use the names of the machines instead of the IP addresses.
```bash
sshfs csf3:/path/to/remote/directory /path/to/local/directory
```
You can then access the files in the remote directory as if they were on your local machine. You can also use your local editor to edit the files in the remote directory.

## file transfer
If you want to transfer files between your local machine and a remote machine, you can use the `scp` command.
To transfer a file from your local machine to a remote machine, open a terminal and type:
```bash
scp /path/to/local/file <username>@<machine>:/path/to/remote/directory
```
If you have your ssh config file set up, you can also use the names of the machines instead of the IP addresses.
```bash
scp /path/to/local/file csf3:/path/to/remote/directory
```
If you want to transfer a file from a remote machine to your local machine, open a terminal and type:
```bash
scp <username>@<machine>:/path/to/remote/file /path/to/local/directory
```
If you have your ssh config file set up, you can also use the names of the machines instead of the IP addresses.
```bash
scp csf3:/path/to/remote/file /path/to/local/directory
```
## rsync 
You can also use `rsync` to transfer files between your local machine and a remote machine. `rsync` is similar to `scp`, but it is more efficient as it only transfers the parts of the file that have changed.
To transfer a file from your local machine to a remote machine, open a terminal and type, e.g.:
```bash
rsync -avz /path/to/local/file <username>@<machine>:/path/to/remote/directory
```
To transfer a file from a remote machine to your local machine, open a terminal and type, e.g.:
```bash
rsync -avz <username>@<machine>:/path/to/remote/file /path/to/local/directory
```
`rsync` has many more options that you can use. You can find more information on how to use `rsync` [here](https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/). Or by typing `man rsync` into your terminal.   
> [!WARNING]
> Make sure to familiarise yourself with the options before using `rsync`. If you use it incorrectly, you can accidentally delete files on your local and/or remote machine. 
