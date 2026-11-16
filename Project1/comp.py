import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2.5,100)

d = 0.01 #[m]
m = 0.01 #[kg]
ro = 1.223 #[kg/m^3] Fluid Density
mu = 1.81e-5 #[Nm s] Fluid Viscosity
a,b,w = 1,1,1
ks = 100 #Spring Constant per unit mass [N/mkg]
kd = 10 #Damping constant per unit mass [Ns/mkg]
L = 0.2 #[m]
N = 5 #Number of Beads
lr = (L - N*d)/N

app_U_vel = -a*t
app_V_vel = b*np.sin(w*t)

app_vel = ((app_U_vel)**2 + (app_V_vel)**2)**0.5

Re = (ro*np.abs(app_vel)*d)/mu
CD = np.full(len(Re),np.nan)
for i in range(len(Re)):
    if Re[i]!=0: CD[i] = (24/Re[i])*(1+0.15*(Re[i]**0.687))
    else: CD[i] = 0

xDrag = CD*(np.pi/8)*ro*(d**2)*(app_U_vel)
yDrag = CD*(np.pi/8)*ro*(d**2)*(app_V_vel)
tDrag = np.hypot(xDrag,yDrag)


dx = np.linspace(0,5*lr,25)
RestoF = m * ks * ((lr+dx) - lr)

fig,ax = plt.subplots(3, 2, figsize=(10, 10))
ax[0,0].plot(t,Re)
ax[0,0].set_title("Expected Reynolds Range")
ax[0,0].set_ylabel("Re")
ax[0,1].plot(t,CD)
ax[0,1].set_title("Expected CD Range")

ax[1,0].plot(t,tDrag)
ax[1,0].set_title("Approximate Drag ")
ax[1,0].set_ylabel("Drag [N]")

ax[1,1].plot(dx,RestoF)
ax[1,1].set_title("Restoring Force")
ax[1,1].set_ylabel("Restor. Force [N]")
ax[1,1].set_xlabel("Distance from Unstretched Length [m]")


plt.show()