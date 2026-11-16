import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = 0.2 #[m]
N = 25 #Number of Beads
d = 0.001 #[m]
bp = 15e3 #[kg/m^3] bead density
m = bp * (4/3)*np.pi*(d/2)**3
ro = 1.223 #[kg/m^3] Fluid Density
mu = 1.81e-5 #[Nm s] Fluid Viscosity
lr = L/N #Unstretched Length
ks = 15000 #Spring Constant [N/mkg]
kd = 45 #Damping constant [Ns/mkg]

def wall(t):
    On = 1
    A = 0.25
    W = 1
    return A*np.sin(W*t)*On
def wallV(t):
    On = 1
    A = 0.25
    W = 1
    return A*W*np.cos(W*t)*On

def CD(U):
    Re = (ro*U*d)/mu
    # print("Re: "+str(Re))
    if Re < 0.00001: CD = 0 
    else: CD = (24/Re)*(1+0.15*(Re**0.687))
    return CD

def wind(t):
    a,b,w = 0,0,2
    Uwind = 1*a*t
    Vwind = b*np.sin(w*t)
    return Uwind,Vwind

def Fd(curT,u,v):
    Uwind, Vwind = wind(curT)
    Urel_vel = Uwind - u #Net velocity felt by bead
    Vrel_vel = Vwind - v
    mag = np.hypot(Urel_vel,Vrel_vel)
    Cd = CD(mag)
    Fdx = Cd*(np.pi/8)*ro*(d**2)*(Urel_vel)*mag
    Fdy = Cd*(np.pi/8)*ro*(d**2)*(Vrel_vel)*mag
    return Fdx,Fdy

def acc(curT,x,y,vx,vy,px,py,pvx,pvy,nx,ny,nvx,nvy):
    xDrag,yDrag = Fd(curT,vx,vy)

    pmag = ((y-py)**2+(x-px)**2)**0.5
    ptheta = np.arctan2((y-py),(x-px))
    nmag = ((y-ny)**2+(x-nx)**2)**0.5
    ntheta = np.arctan2((y-ny),(x-nx))

    xSpring = -ks*(pmag-lr)*np.cos(ptheta) -ks*(nmag-lr)*np.cos(ntheta)
    ySpring = -ks*(pmag-lr)*np.sin(ptheta) -ks*(nmag-lr)*np.sin(ntheta)

    xDamp = -kd*(vx-pvx) - kd*(vx-nvx)
    yDamp = -kd*(vy-pvy) - kd*(vy-nvy)

    Fx = xSpring + xDamp + xDrag/m
    Fy = ySpring + yDamp + yDrag/m 
    D = np.hypot(xDrag,yDrag)
    return Fx, Fy, D

def acc2(curT,x,y,vx,vy,px,py,pvx,pvy):
    xDrag,yDrag = Fd(curT,vx,vy)

    pmag = ((y-py)**2+(x-px)**2)**0.5
    ptheta = np.arctan2((y-py),(x-px))

    xSpring = -ks*(pmag-lr)*np.cos(ptheta)
    ySpring = -ks*(pmag-lr)*np.sin(ptheta) 

    xDamp = -kd*(vx-pvx)
    yDamp = -kd*(vy-pvy) 

    Fx = xSpring + xDamp + xDrag/m
    Fy = ySpring + yDamp + yDrag/m 
    D = np.hypot(xDrag,yDrag)
    return Fx, Fy, D

finalT = 25
timeSteps = 4500
dt = finalT/timeSteps
print(dt)
t = np.linspace(0,finalT,timeSteps+1)

#Pre-allocated
x = np.zeros((len(t),N))
vx = np.zeros((len(t),N))
y = np.zeros((len(t),N))
vy = np.zeros((len(t),N))
drag = np.zeros(len(t))

#Initial Condition

for i in range(0,N):
    x[0,i] = lr*(5*i+1)
    y[0,i] = np.sin(x[0,i])

for ti in range(0,len(t)-1):
    ct = ti*dt
    xAcc, yAcc, Drag = acc(ct,x[ti,0],y[ti,0],vx[ti,0],vy[ti,0],0,wall(ct),0,wallV(ct),x[ti,0+1],y[ti,0+1],vx[ti,0+1],vy[ti,0+1])
    drag[ti] = Drag
    vx[ti+1,0] = vx[ti,0] + xAcc*dt
    vy[ti+1,0] = vy[ti,0] + yAcc*dt
    x[ti+1,0] = x[ti,0] + vx[ti+1,0]*dt
    y[ti+1,0] = y[ti,0] + vy[ti+1,0]*dt

    for i in range(1,N-1):
        xAcc, yAcc, Drag = acc(ct,x[ti,i],y[ti,i],vx[ti,i],vy[ti,i],x[ti,i-1],y[ti,i-1],vx[ti,i-1],vy[ti,i-1],x[ti,i+1],y[ti,i+1],vx[ti,i+1],vy[ti,i+1])
        
        vx[ti+1,i] = vx[ti,i] + xAcc*dt
        vy[ti+1,i] = vy[ti,i] + yAcc*dt
        x[ti+1,i] = x[ti,i] + vx[ti+1,i]*dt
        y[ti+1,i] = y[ti,i] + vy[ti+1,i]*dt

    xAcc, yAcc, Drag = acc2(ct,x[ti,N-1],y[ti,N-1],vx[ti,N-1],vy[ti,N-1],x[ti,N-2],y[ti,N-2],vx[ti,N-2],vy[ti,N-2])
    vx[ti+1,N-1] = vx[ti,N-1] + xAcc*dt
    vy[ti+1,N-1] = vy[ti,N-1] + yAcc*dt
    x[ti+1,N-1] = x[ti,N-1] + vx[ti+1,N-1]*dt
    y[ti+1,N-1] = y[ti,N-1] + vy[ti+1,N-1]*dt

fig = plt.figure(num=1, figsize=(7, 5))
xmin = -3*L
xmax = -2*xmin
ymin = -2.5*L
ymax = -1*ymin
xm = np.linspace(xmin,xmax,5)
ym = np.linspace(1.5*ymin, 1.5*ymax,30)
X,Y = np.meshgrid(xm,ym)
z = np.zeros((len(xm),len(ym)))

ax = fig.add_subplot(autoscale_on=False, xlim=(xmin,xmax), ylim=(ymin,ymax))
anchor, = ax.plot([0], [0], "ks", ms=2)
field = ax.quiver(X, Y, z, z, color='skyblue', alpha=0.75, scale=100, width=0.006)
sphereSize = 3+ 7*m
first, = ax.plot([], [], 'b-', lw=1,ms=sphereSize)
line, = ax.plot([], [], 'bo-', lw=1,ms=sphereSize)
ax.set_xlabel("X Position [m]")
ax.set_ylabel("Y Position [m]")
title = ax.set_title("Cord in Wind with Velocity Magnitude: V = 0 m/s")
ax.set_title("Cord in Wind with Velocity Magnitude, V = ")
time_text = ax.text(0.45*xmax, 0.75*ymax, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor': 'Blue', 'alpha': 0.6, 'pad': 5})
time_template = 'Time = %.1fs'

def animate(i):
    first.set_data([0,x[i,0]],[wall(i*dt),y[i,0]])
    anchor.set_data([0],[wall(i*dt)])
    line.set_data(x[i,:],y[i,:])
    time_text.set_text(time_template % (i*dt))
    u,v = wind(i*dt)
    U = np.full_like(X,u)
    V = np.full_like(Y,v)
    field.set_UVC(U,V)
    mag = np.hypot(u,v)
    ax.set_title(f"Velocity Magnitude: {mag:.0f} m/s")
    return line, time_text, anchor,field, first, ax

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
fig.tight_layout()
ani = animation.FuncAnimation(
    fig, animate, frames=range(0, len(t), 10), interval=18, blit=False)
plt.show()

# ani.save("Project1_StretchedIC.mp4", writer='ffmpeg', fps=30)
data = np.column_stack((x[:,0],y[:,0],vx[:,0],vx[:,0]))
headers = ["x","y","vx","vy"]

# print(tabulate(data,headers=headers,tablefmt='github'))
print("DT = "+str(dt))
plt.figure(2)
plt.plot(t[0:-1],drag[0:-1])
# plt.show()