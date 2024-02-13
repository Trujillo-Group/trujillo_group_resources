> [!IMPORTANT]  
> This advice is general and non-exhaustive. For you to be most likely to fix these errors it is necessary to view the output files with a visualisation tool, and to apply your own intuition alongside this!

# Introduction
This tutorial aims to provide more specific help for Gaussian Errors typical to our group's calculations, such as metal-free transition state (TS) calculations. Should you need any further help, below are some resources which provide general information on dealing with Gaussian Errors.

[Alliance Doc Wiki](https://docs.alliancecan.ca/wiki/Gaussian_error_messages)

[Blog by Zhe Wang](https://wongzit.github.io/gaussian-common-errors-and-solutions/)

Lastly, this is by no means an exhaustive list, and should you find any alternative fix/error to what is in this tutorial, please add it! Thanks.

# Index
- [Convergence Error](#convergence-error)
- [Product Formed instead of TS](#product-formed-instead-of-ts)
- [Link9999](#link9999)
- [Reading Basis Center](#reading-basis-center)
- [Unrecognised Atomic Symbol](#unrecognised-atomic-symbol)
- [End of file reading PCM Input](#end-of-file-reading-pcm-input)
- [End of file reading Connectivity](#end-of-file-reading-connectivity)
- [galloc: could not allocate memory](#galloc-could-not-allocate-memory)
- [No such File or Directory](#no-such-file-or-directory)

# Convergence Error

**Explanation:** The SCF (self-consistent field) procedure failed to converge.

**Solution:** Execute ```grep "Converged?" file.log -A5```

If 2/4 values are consistently converged, consider the following keywords:

1. scf=xqc

2. MaxStep=3 or MaxStep=4

Else:

1. Check keywords are correct

2. Consider alternative initial geometry

3. Run quick preoptimisation using [xtb](https://github.com/grimme-lab/xtb)

# Product formed instead of TS

**Explanation:** Initial geometry is too close to the product.

**Solution:** Consider the following

1. Pull reactants further apart and rerun

2. Run a [Scan](https://gaussian.com/opt/) over a greater range of bond distances/angles for the pivotal bond breaking/making etc. 

```
opt=modredundant

...
...

B atom1 atom2 S NumberOfSteps StepSizeInAngstroms

```

# Link9999

**Explanation:** This error most commonly occurs when an optimisation fails to converge. The output file will most likely show a repetitive back and forth when visualised. 

**Solution:** Consider the following

1. A poor intial geometry. Try an alternative starting geometry.

2. Preoptimize the structure with a worse basis set (eg. B3LYP) or semi-empirical methods (eg. [xtb](https://github.com/grimme-lab/xtb))

# Reading Basis Center

**Explanation:** This is an input error and relates to the use of ```gen``` as the basis set. This error can be typical when using pseudopotentials. 

**Solution:** Consider the following

1. If using a pseudo=read, reread over the bottom of your input file. Typical example:
```
H C S N O I 0
def2svp
****
[Blank Line]
I 0
def2svp
[Blank Line]
```

2. Remove the ```gen``` keyword and specify your basis set
    
# Unrecognised Atomic Symbol

**Explanation:** This is typically an input error.

**Solution:** Consider the following

1. Reread your input file and ensure it follows this structure:

```
# Keywords
[Blank Line]
Title
[Blank Line]
Charge Multiplicity
Element 1       X   Y   Z
.
.
.
Last Element    X   Y   Z
[Blank Line]
```

2. If using pseudopotentials, this error can typically occur with a misinput at the bottom of the file. See previous error for example.

3. Check all your atomic symbols are correctly input.

# End of file reading PCM Input

**Explanation:** PCM is an acronym for Polarizable Continuum Model, a.k.a. solvent modelling. This is an error that occurs typically when using ```scrf=read```
**Solution:** Consider the following

1. Ensure solvent is correctly included at end of file

2. Remove ```scrf=read```


# End of file reading Connectivity

**Explanation:** This is an error that occurs typically when unecessarily including ```geom=connectivity```
**Solution:** Remove ```geom=connectivity```

# galloc: could not allocate memory

**Explanation:** This is an error relating to memory allocation. Be aware: Gaussian typically uses roughly 1GB more than specific with ```%mem```. 

**Solution:** If using CSF, ```%mem``` is not necessary so you may remove it. Otherwise consider the following

1. Increase the amount allocated using ```%mem```

2. Ensure amount is greater than 1GB

# No such file or directory

**Explanation:** This is likely a pathing issue regarding ```GAUSS_SCRDIR```

**Solution:** Change ```GAUSS_SCRDIR``` to your existing scratch directory.
