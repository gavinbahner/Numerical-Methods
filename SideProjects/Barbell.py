import numpy as np


L = 10 #[ft]
M = 45 #[lb]
lamba = L/M #Line Mass Density [ft/lb]
g = 32.2 #[ft/s^2]
Wbar = M * g #[ft-lb/s^2]
#Weight Added On Right
Madd = 90 #[lb]
Wadd = Madd * g #[ft-lb/s^2]
#Reaction Forces - assumes no acceleration
R = (Wbar + Wadd)/2
#About Right - CCW Pos
SM = Wbar * (3.5) - R * (2*3.5) #[lb-ft]
print(SM)
