# Natural Bonding Orbital (NBO) Analysis
An illustration is provided to help get a very basic grasp of what this analysis is used for. NBO helps you identify natural orbital populations, as well as quantify charge-transfer between atoms, as depicted below.

![Illustration of NBO](NBO_Example.png)

## Steps

This tutorial has been written for NBO version 7.0.8. For any further details see the [manual](https://nbo7.chem.wisc.edu/nboman.pdf).

**0. Gaining Access**

For CSF, you must [request access](https://ri.itservices.manchester.ac.uk/csf4/software/applications/nbo/) to NBO 7.0.8.

**1. File generation**

Run single point calculation on previously optimised system with Gaussian (submission scripts available for ICHEC and CSF3-4 (No need for first 2 lines) found in ```trujillo_group_resources/scripts``` directory). Ensure that you include keyword **"pop=nbo7"**, as shown below.

```{shell}
%nprocshared=40
%mem=100GB
# wb97xd def2svp scrf=(smd,solvent=dichloromethane) pop=nbo7

filename

2 1
 C                 -2.84087900   -0.13629700    0.83103500
 C                 -2.46248200    0.28464400   -0.44227700
```

**N.B.** It is highly advised to use the same basis set as used for optimisation.

**2. Data analysis**

Once the single point calculation is complete, you may analyse the **filename.log** output file using the following commands. The examples below are studying the charge transfer from the **lone pairs (LP)** of electrons of the oxygen atom to the **antibonding orbitals BD*** of the iodine atom.

This command will extract all the charge transfer data from all the lone pairs (LP) of electrons to the antibonding orbitals (BD*) in the system.

```{shell}
grep 'LP' B2_cat6b_ts1_product.log | grep 'BD\*'
```

In order to narrow this data set down for ease of analysis, we will use the following command, **grep -v** eliminates irrelevant atoms, in this case the hydrogen and fluorine.

```{shell}
grep 'LP' B2_cat6b_ts1_product.log | grep 'BD\*' | grep -v F | grep -v H
```
Adding **> filename.txt** as shown below will extract all the specified data in a textfile name "filename.txt"

```{shell}
grep 'LP' B2_cat6b_ts1_product.log | grep 'BD\*' | grep -v F | grep -v H > filename.txt
```
