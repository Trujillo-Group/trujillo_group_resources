# QTAIM Theory

Quantum Theory of Atoms in Molecules was primarily developed by Richard Bader in which atoms and bonds are described through a system's observable electron density distribution function. To better understand this theory the following resources have been provided:

[Cryst.bbk.ac.uk "The Quantum chemical theory Atoms in Molecules"](https://www.cryst.bbk.ac.uk/PPS2/projects/loesel/chap03c.htm)

# AIMAll Steps

**1. WFN/WFX generation**

Run single point calculation on previously optimised system with Gaussian (submission scripts available for ICHEC and CSF3-4 found in ```trujillo_group_resources/scripts``` directory). Ensure that you include keyword **"output=wfx"** or **"output=wfn"**, as well as **filename.wfx** or **filename.wfn** as shown below.

It is important to note that the wfn extension is used for calculations which do not require the inclusion of pseudopotentials. Example for both cases has been included. 

```{shell}
%nprocshared=40
%mem=100GB
# wb97xd def2svp scrf=(smd,solvent=dichloromethane) output=wfn

filename

2 1
 C                 -2.84087900   -0.13629700    0.83103500
 C                 -2.46248200    0.28464400   -0.44227700

filename.wfn

```

```{shell}
%nprocshared=40
%mem=100GB
# wb97xd/gen scrf=(smd,solvent=dichloromethane) pseudo=read output=wfx

filename

2 1
 C                 -2.84087900   -0.13629700    0.83103500
 C                 -2.46248200    0.28464400   -0.44227700
 I                  1.28782300    1.60990900   -0.80103900
 O                  2.74823200   -0.53732200   -1.30854400
 C                  4.09251600   -0.14782400   -1.40571500
 H                  4.21779800    0.59136900   -2.21872500

C H N I O 0
def2svp
****

I 0
def2svp

filename.wfx

```

**N.B.** It is highly advised to use the same basis set as used for optimisation.


**1. WFN/WFX submission**

Once the wfx/wfn output file has been generated, it can now be submitted to AIMAll using the script **sub_aimall** (found in ```trujillo_group_resources/scripts/submission/QTAIM``` directory
).



