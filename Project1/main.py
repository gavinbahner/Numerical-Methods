import numpy as np

import matplotlib.pyplot as plt
tS = 0 #Start Time
tF = 10 #Final Time
s = 6  #Time Steps
t = np.linspace(start=tS,stop=tF,num=s+1)
dt = t[1] - t[0]

nb = 3 #Number of Beads
lr = 0.08 #Unstretched Distance Between Beads Outside
D =0.001  #Dimater of Bead [m]
x = np.zeros((nb,2,s+1))

for i in range(len(x)): #Bead initial positions
  x[i,0,0] = (i+1)*lr

v = np.zeros((nb,2,s+1))

a = 1
b = 1
w = 1
windU = -a*t
# print(type(windU))
windV = b*np.sin(w*t)
windMag = (windU**2+windV**2)**0.5 #Elementise Magnitude
print(windMag)
def Re(v,D):
    p = 1.225 # (kg/m3)
    µ = 1.86*10**-5 #(Pa s)
    return (p*v*D)/µ

R = Re(windMag,D)

def CD (Re):
    Cd = np.full(len(t),np.nan)
    for i in range(0,len(Re)-1):
        if Re[i] == 0:
            Cd[i] = 0
        else:
            Cd[i] = (24/Re[i]) * (1+0.15*(Re[i]**0.687))
    return Cd

Cd = CD(R)

def fxD(i,vx,D):
    p = 1.225
    F = Cd[i]*(np.pi/8)*p*(D**2)*((windU[i]-vx)**2)
    return F

def fyD(i,vy,D):
    p = 1.225
    F = Cd[i]*(np.pi/8)*p*(D**2)*((windV[i]-vy)**2)
    return F

FSb = np.zeros((nb,s))
FSa = np.zeros((nb,s))
FDb = np.zeros((nb,s))
FDa = np.zeros((nb,s))
kS = 100
kD = 10
for j in range(0,s): #Time For Loop
    print(f"j:{j:2f}")
    for i in range(0,nb-1): #Particle Left to Right For Loop
        if i == 0: #At first particle
          xb = x[i,0,j] - 0
          yb = x[i,1,j] - 0
        else: 
          xb = x[i,0,j] - x[i-1,0,j]
          yb = x[i,1,j] - x[i-1,1,j]
      
        xa = x[i,0,j] - x[i+1,0,j]
        ya = x[i,1,j] - x[i+1,1,j]
        
        if xb == 0:
            a1 = 90
        else:
            a1 = np.arctan(yb/xb)
        if xa == 0:
            a2 = 90
        else:
            a2 = np.arctan(ya/xa)
          
        if i == 0: #At first particle
          vxb  = v[i,0,j] - 0
          vyb = v[i,1,j] - 0
        else: 
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
        print(f'xb: {xb:2f}')
      
        FSb[i,j] = -1*kS* (np.sqrt( (xb)**2 + (yb)**2 ) - lr)
        FSa[i,j] = -1*kS* (np.sqrt( (xa)**2 + (ya)**2 ) - lr)
        FDb[i,j] = -1*kD* (np.sqrt( (vxb)**2 + (vyb)**2 ))
        FDa[i,j] = -1*kD* (np.sqrt( (vxa)**2 + (vya)**2 ))
        print(fxD(j,v[i,0,j],D))
        x[i,0,j+1] = x[i,0,j] + v[i,0,j]*dt
        v[i,0,j+1] = v[i,0,j] + (FSb[i,j]*np.cos(a1) + FSa[i,j]*np.cos(a2) + FDb[i,j]*np.cos(a3) + FDb[i,j]*np.cos(a4)+ fxD(j,v[i,0,j],D))*dt
        x[i,1,j+1] = x[i,1,j] + v[i,1,j]*dt
        v[i,1,j+1] = v[i,1,j] + (FSb[i,j]*np.sin(a1) + FSa[i,j]*np.sin(a2) + FDb[i,j]*np.sin(a3) + FDb[i,j]*np.sin(a4)+ fxD(j,v[i,0,j],D))*dt
    

# print(x)
# plt.plot(t,x[2,1,:],'o--')
# plt.show()
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(t,x[0],'o')
ax[0].plot(t,x,'-')
# ax[0].set_title("Temperature dist. with BC: T(0) = 240, T(10) = 150",fontsize=9,style='oblique')
# ax[0].set_xlim(0,10)
# ax[0].set_ylim(45,250)
# ax[0].legend()


