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
    CD[i]*(np.pi/8)*p*(D**2)*((windU[i]-vx)**2)

def fyD(i,vy,D):
    p = 1.225
    CD[i]*(np.pi/8)*p*(D**2)*((windV[i]-vy)**2)

FSb = np.zeros((nb,s))
FSa = np.zeros((nb,s))
FDb = np.zeros((nb,s))
FDa = np.zeros((nb,s))
kS = 20
kD = 20
for j in range(2,s-1):
    for i in range(2,nb-1):
        [xb,yb] = [x[i,0,j] - x[i-1,0,j],x[i,1,j] - x[i-1,1,j]]
        [xa,ya] = [x[i,0,j] - x[i+1,0,j],x[i,1,j] - x[i+1,1,j]]
        a1 = np.arctan(yb/xb)
        a2 = np.arctan(ya/xa)
        [vxb,vyb] = [v[i,0,j] - v[i-1,0,j],v[i,1,j] - v[i-1,1,j]]
        [vxa,vya] = [v[i,0,j] - v[i+1,0,j],v[i,1,j] - v[i+1,1,j]]
        a3 = np.arctan(vyb/vxb)
        a4 = np.arctan(vya/vxa)

        FSb[i,j] = -1*kS* (np.sqrt( (xb)^2 + (yb)^2 ) - lr)
        FSa[i,j] = -1*kS* (np.sqrt( (xa)^2 + (ya)^2 ) - lr)
        FDb[i,j] = -1*kD* (np.sqrt( (vxb)^2 + (vyb)^2 ))
        FDa[i,j] = -1*kD* (np.sqrt( (vxa)^2 + (vya)^2 ))

        x[i,0,j+1] = x[i,0,j] + v[i,0,j]*dt
        v[i,0,j+1] = fxD(j,v[i,0,j],D) + FSb(i,j)*np.cos(a1) + FDb(i,j)*np.cos(a3)
        x[i,1,j+1] = x[i,1,j] + v[i,1,j]*dt
        v[i,1,j+1] = fyD(j,v[i,1,j],D) + FSb(i,j)*np.sin(a2) + FDb(i,j)*np.sin(a4)
    