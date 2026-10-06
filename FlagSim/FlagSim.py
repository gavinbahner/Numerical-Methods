import numpy as np

import matplotlib.pyplot as plt
tS = 0 #Start Time
tF = 10 #Final Time
s = 20  #Time Steps
t = np.linspace(start=tS,stop=tF,num=s+1)
dt = t[1] - t[0]

nb = 5 #Number of Beads
lr = 0.08 #Unstretched Distance Between Beads
D = lr * nb #Length of Bead Chain
x = np.zeros((nb,2,s))
v = np.zeros((nb,2,s))

a = 1
b = 1
w = 1
windU = -a*t
print(type(windU))
windV = b*np.sin(w*t)
windMag = (windU**2+windV**2)**0.5 #Elementise Magnitude

def Re(v,D):
    p = 1.225 # (kg/m3)
    µ = 1.86*10**-5 #(Pa s)
    return (p*v*D)/µ

Re = Re(windMag,D)

def CD (Re):
    return(24/Re) * (1+0.15*(Re**0.687))

CD = CD(Re)

def fxD(i,vx,D):
    p = 1.225
    F = CD[i]*(np.pi/8)*p*(D**2)*((windU[i]-vx)**2)
    return F

def fyD(i,vy,D):
    p = 1.225
    F = CD[i]*(np.pi/8)*p*(D**2)*((windV[i]-vy)**2)
    return F

FSb = np.zeros((nb,s))
FSa = np.zeros((nb,s))
FDb = np.zeros((nb,s))
FDa = np.zeros((nb,s))
kS = 20
kD = 20
for j in range(1,s-1): #Time For Loop
    for i in range(1,nb-1): #Particle Left to Right For Loop
        xb = x[i,0,j] - x[i-1,0,j]
        yb = x[i,1,j] - x[i-1,1,j]
        xa = x[i,0,j] - x[i+1,0,j]
        ya = x[i,1,j] - x[i+1,1,j]
        
        if xb == 0:
            a1 = 0
        else:
            a1 = np.arctan(yb/xb)
        if xa == 0:
            a2 = 0
        else:
            a2 = np.arctan(ya/xa)

        vxb  = v[i,0,j] - v[i-1,0,j]
        vyb = v[i,1,j] - v[i-1,1,j]
        vxa = v[i,0,j] - v[i+1,0,j]
        vya = v[i,1,j] - v[i+1,1,j]
        if vxb == 0:
            a3 = 0
        else:
            a3 = np.arctan(vyb/vxb)
        if vxa == 0:
            a4 = 0
        else:
            a4 = np.arctan(vya/vxa)

        FSb[i,j] = -1*kS* (np.sqrt( (xb)**2 + (yb)**2 ) - lr)
        FSa[i,j] = -1*kS* (np.sqrt( (xa)**2 + (ya)**2 ) - lr)
        FDb[i,j] = -1*kD* (np.sqrt( (vxb)**2 + (vyb)**2 ))
        FDa[i,j] = -1*kD* (np.sqrt( (vxa)**2 + (vya)**2 ))
   
        x[i,0,j+1] = x[i,0,j] + v[i,0,j]*dt
        v[i,0,j+1] = FSb[i,j]*np.cos(a1) + FDb[i,j]*np.cos(a3) + fxD(j,v[i,0,j],D)
        x[i,1,j+1] = x[i,1,j] + v[i,1,j]*dt
        v[i,1,j+1] = FSb[i,j]*np.sin(a2) + FDb[i,j]*np.sin(a4) + fyD(j,v[i,1,j],D)
    
print(x)

plt.plot(x[:,0,1],x[:,1,1])
plt.show()