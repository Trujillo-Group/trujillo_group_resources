%mem=140GB
%nprocshared=40
# opt freq b3lyp/6-31+g(d,p) scrf=(smd,solvent=THF)

br(-)...H3C-br

-1 1
 C                  0.00000000    0.00000000   -0.28687100
 H                  0.89721000   -0.51800500   -0.60275900
 H                 -0.89721000   -0.51800500   -0.60275900
 O                  0.00000000    0.00000000    1.14312900
 H                 -0.78281858    0.45398670    1.46358359
 C                  0.00000000    1.47304751   -0.73601578
 H                  0.08111629    1.52093956   -1.80186122
 H                 -0.91138060    1.94035340   -0.42632141
 H                  0.83026435    1.98133021   -0.29193267
 Br                 0.00000000    0.00000000   -3.35960700
