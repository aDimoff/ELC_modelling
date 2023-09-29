awk '{print $3,$2}' generation.* > ttempELC.ecc
awk '{print $4,$2}' generation.* > ttempELC.P
awk '{print $5,$2}' generation.* > ttempELC.primK
awk '{print $6,$2}' generation.* > ttempELC.T0
awk '{print $7,$2}' generation.* > ttempELC.argper
awk '{print $8,$2}' generation.* > ttempELC.Q
awk '{print $9,$2}' generation.* > ttempELC.gam1
