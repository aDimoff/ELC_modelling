awk '{print $1}' demcmc_fitparm.* > tempELC.ecc
awk '{print $2}' demcmc_fitparm.* > tempELC.P
awk '{print $3}' demcmc_fitparm.* > tempELC.primK
awk '{print $4}' demcmc_fitparm.* > tempELC.T0
awk '{print $5}' demcmc_fitparm.* > tempELC.gam1
awk '{print $6}' demcmc_fitparm.* > tempELC.Tperi2
awk '{print $7}' demcmc_fitparm.* > tempELC.Tsupconj2
awk '{print $8}' demcmc_fitparm.* > tempELC.Tinfconj2
