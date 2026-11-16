import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = 0.2 #[m]
N = 5 #Number of Beads
d = 0.001 #[m]
m = .1 #[kg]
ro = 1.223 #[kg/m^3] Fluid Density
mu = 1.81e-5 #[Nm s] Fluid Viscosity
lr = (L - N*d)/N #Unstretched Length
ks = 100 #Spring Constant [N/mkg]
kd = 10 #Damping constant [Ns/mkg]

def wall(t):
    On = 1
    A = 0.5
    W = 0.1
    return A*np.sin(W*t)*On

def CD(U):
    Re = (ro*np.abs(U)*d)/mu
    print("Re: "+str(Re))
    if Re == 0: CD = 0 
    else: CD = (24/Re)*(1+0.15*(Re**0.687))
    return CD

def Fd(curT,u,v):
    a,b,w = 25,20,1
    Uwind = -1*a*curT
    Vwind = b*np.sin(w*curT)
    Urel_speed = np.abs(u-Uwind)
    Urel_vel = Uwind - u
    Vrel_speed = np.abs(v-Vwind)
    Vrel_vel = Vwind - v
    mag = np.hypot(Urel_speed,Vrel_speed)
    Cd = CD(mag)
    Fdx = Cd*(np.pi/8)*ro*(d**2)*(Urel_speed*Urel_vel)
    Fdy = Cd*(np.pi/8)*ro*(d**2)*(Vrel_speed*Vrel_vel)
    return Fdx,Fdy

def acc(curT,x,y,vx,vy):
    xDrag,yDrag = Fd(curT,vx,vy)

    mag = ((y-wall(curT))**2+(x-0)**2)**0.5
    theta = np.arctan2((y-wall(curT)),(x-0))

    xSpring = -ks*(mag-lr)*np.cos(theta)
    ySpring = -ks*(mag-lr)*np.sin(theta)

    xDamp = -kd*vx
    yDamp = -kd*vy

    Fx = xSpring + xDamp + xDrag/m
    Fy = ySpring + yDamp + yDrag/m
    return Fx, Fy

finalT = 50
timeSteps = 2000
dt = finalT/timeSteps
t = np.linspace(0,finalT,timeSteps+1)

#Pre-allocated
x = np.zeros(len(t))
vx = np.zeros(len(t))
y = np.zeros(len(t))
vy = np.zeros(len(t))

#Initial Condition
x[0] = lr+d/2

for ti in range(0,len(t)-1):
    ct = ti*dt
    xAcc, yAcc = acc(ct,x[ti],y[ti],vx[ti],vy[ti])
    x[ti+1] = x[ti] + vx[ti]*dt
    y[ti+1] = y[ti] + vy[ti]*dt
    vx[ti+1] = vx[ti] + xAcc*dt
    vy[ti+1] = vy[ti] + yAcc*dt

fig,ax = plt.subplots(1,2)
ax[0] = fig.add_subplot(autoscale_on=False, xlim=(-4*L, 4*L), ylim=(-4*L, 4*L))
ax[1] = fig.add_subplot(autoscale_on=False, xlim=(-4*L, 4*L), ylim=(-4*L, 4*L))
anchor, = ax[0].plot([0], [0], "ks", ms=2)
ax[0].grid()

line, = ax[0].plot([], [], 'o-', lw=2)


time_template = 'time = %.1fs'
time_text = ax[0].text(0.05, 0.9, '', transform=ax[0].transAxes)


def animate(i):
    anchor.set_data([0],[wall(i*dt)])
    line.set_data([x[i]],[y[i]])
    time_text.set_text(time_template % (i*dt))
    return line, time_text, anchor


ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*500, blit=True)
plt.show()
    
    


