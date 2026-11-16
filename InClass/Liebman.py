import numpy as np

L =10
intPt = 4
dx = L/(intPt+1)
hp = 0.01
Tair = 20
lamb = 1.5

TB = 40
TE = 200

intT = np.array([0,0,0,0])
prevT = np.zeros(len(intT))
iter = 100
iterT = np.zeros((iter,len(intT)))
for j in range(iter):
    for i in range(len(intT)):
        if i == 0:
            intT[i] = (TB + intT[i+1] + Tair*hp*((dx)**2))/(2+hp*((dx)**2))
            
        elif (i < len(intT)-1):
            intT[i] = ((intT[i-1] + intT[i+1] + Tair*hp*((dx)**2))/(2+hp*((dx)**2)))
            
        else:
            intT[i] = ((intT[i-1] + TE + Tair*hp*((dx)**2))/(2+hp*((dx)**2)))
    
    prevT = intT
    intT = lamb*intT + (1-lamb)*prevT     #Over-relaxiation factor
    iterT[j,:] = intT

    
print(iterT)
