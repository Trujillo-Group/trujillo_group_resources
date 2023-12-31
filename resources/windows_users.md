# How to survive as Windows user in a Linux world
Windows is a great operating system, but it's not very handy when it comes to installing, using and interfacing with Unix/Linux software. And basically all the remote servers you will be using in the future will be running some kind of Linux. So it's a good idea to get used to it.   
There are a few ways to use Unix on a Windows machine, but this guide will focus on one. It's called Windows Subsystem for Linux ([WSL](https://learn.microsoft.com/en-us/windows/wsl/)), which already says it all.   
You can find a guide on how to install and setup the WSL [here](https://learn.microsoft.com/en-us/windows/wsl/install).    
Once you have setup your WSL, you can open the WSL terminal and you will be able to use all the Unix commands like your it was a normal Linux machine. You can install all the packages you need, and also access your Windows files from the WSL terminal via the `/mnt/c` directory. You can also invoke Windows programs from the WSL terminal, e.g. `code .` will open the current directory in Visual Studio Code.
## VS Code and WSL
If you want to use VS Code as your editor in the WSL distribution, you will need to install the respective WSL extension in VS Code. You can find further information [here](https://code.visualstudio.com/docs/remote/wsl).
