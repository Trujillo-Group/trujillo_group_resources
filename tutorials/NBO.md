# NBO Steps

**1. File generation**

Run single point calculation on previously optimised system with Gaussian (submission scripts available for ICHEC and CSF3-4 found in ```trujillo_group_resources/scripts``` directory). Ensure that you include keyword **"pop=NBO"**, as shown below.

```{shell}
%nprocshared=40
%mem=100GB
# wb97xd/gen scrf=(smd,solvent=dichloromethane) pop=NBO

filename

2 1
 C                 -2.84087900   -0.13629700    0.83103500
 C                 -2.46248200    0.28464400   -0.44227700
```
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




