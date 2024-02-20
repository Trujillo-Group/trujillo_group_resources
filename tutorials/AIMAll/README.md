# AIMAll Steps

**1. WFN/WFX generation**

Run single point calculation on previously optimised system with Gaussian (submission scripts available for ICHEC and CSF3-4 found in ```trujillo_group_resources/scripts``` directory). Ensure that you include keyword **"output=wfx"** or **"output=wfn"**, as well as **filename.wfx** or **filename.wfn** as shown below.

```{shell}
%nprocshared=40
%mem=100GB
# wb97xd def2svp scrf=(smd,solvent=dichloromethane) output=wfx

filename

2 1
 C                 -2.84087900   -0.13629700    0.83103500
 C                 -2.46248200    0.28464400   -0.44227700

filename.wfx

```

**1. WFN/WFX submission**

Once the wfx/wfn output file has been generated, it can now be submitted to AIMAll using the script **sub_aimall** (found in ```trujillo_group_resources/scripts/submission/QTAIM``` directory
).



