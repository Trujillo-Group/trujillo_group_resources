%mem=140GB
%nprocshared=40
# opt=(calcfc,ts,noeigentest) freq b3lyp/6-31+g(d,p)  scrf=(smd,solvent=THF)

cl(-)...H3C-cl (ts)

-1 1
 C                  0.00000000    1.53999536   -0.76177279
 H                  0.00201100    1.89418500    0.24790322
 H                  0.87264407    1.89790273   -1.26703969
 H                 -0.87465511    1.89789469   -1.26355613
 C                  0.00000000    0.00000000   -0.76555200
 H                  0.87465490   -0.35789882   -0.26376794
 H                 -0.87264464   -0.35790736   -0.26028608
 Br                 0.00000000    0.00000000   -3.13155700
 O                  0.00000000    0.00000000    1.71767200
 H                  0.96000000    0.00000000    1.71767200

