import numpy as np
from tabulate import tabulate
L = 0.2 #[m]
N = 5 #Number of Beads
d = 0.001 #[m]

lr = (L - N*d)/N

ks = 100
kd = 10
x0 = np.linspace(lr+d/2,L,N)
y0 = np.zeros(N)

ro = 1.223

def CD (U,D):
    ro = 1.223 #[kg/m^3] Fluid Density
    mu = 1.81e-5 #[Nm s] Fluid Viscosity
    Re = (ro*np.abs(U)*D)/mu #Re will have same shape as U
    # print("Velocity:" + str(U))
    # print("Reynolds:" + str(Re))
    cd = np.full((2,len(x0)),0.0) #MUST BE initialized as float
    for i in range(len(Re)):
        for j in range(len(Re[i])):
            if Re[i,j] == 0:
                cd[i,j] = 0
            else:
                cd[i,j] = (24/Re[i,j])*(1+0.15*(Re[i,j])**0.687)
    return cd

finalT = 50
timeSteps = 500
dt = finalT/timeSteps
t = np.linspace(0,finalT,timeSteps+1)

alpha = 1
beta = 1
omega = 1
windU = -1*alpha*t  #Index of time and Wind Velocities Match - directly reference with index in time for loop
windV = -1*beta*np.sin(omega*t)
windVel = np.array((windU,windV))
relW = np.zeros((2,len(x0),len(t)))

xy = np.zeros((len(x0),2,len(t)))
xy[:,0,0] = x0
xy[:,1,0] = y0 

vxvy = np.zeros((len(x0),2,len(t)))

relx = np.zeros(len(x0))
rely = np.zeros(len(x0))
posVect = np.zeros((2,len(x0)))


relVel = np.zeros((2,len(x0)))

fDrag = np.zeros((2,len(x0)))
for ti in range(0,len(t)-1):

    for i in range(0,len(x0)):
        #Velocity Calculation Based on Current and Previous Time Step
        if ti == 0:
            vxvy[i,:,ti] = 0 #Velocity at ti=0 is zero
        else:
            vxvy[i,:,ti] = (xy[i,:,ti] - xy[i,:,ti-1])/dt #Velocity at current time is each particle current position minus prev position
        #Relative Positions of Each Consecutive Particle
        if i == 0: #Leftmost particle is reference to the wall location
            relx[i] = xy[i,0,ti] - 0 #Origin Location
            rely[i] = xy[i,1,ti] - 0 #Origin Location
        else:
            relx[i] = xy[i,0,ti] - xy[i-1,0,ti] #Each value in array stores the relative position of part and previous part in chain
            rely[i] = xy[i,1,ti] - xy[i-1,1,ti]
    dist = (relx**2 + rely**2)**0.5
    #Relative Velocities of Each Particles
    for i in range(len(x0)):
        relVel[:,i] = vxvy[i,:,ti] - vxvy[i-1,:,ti]
        relW[:,i,ti] = relVel[:,i] - windVel[:,ti]
    vel = (relVel[0,:]**2 + relVel[1,:]**2)**0.5
    #Drag force on each particle Based on Time and Particle Velocity
    cd = CD(relW[:,:,ti],d)
    # print(cd)
    for i in range(len(x0)):
        fDrag[:,i] = cd[:,i] * (np.pi/8)*ro*(d**2)*(relW[:,i,ti]**2)
        print(fDrag)
    #Next Position of the Particles with Second Order Accurate Central Finite Difference for Acceleration
    for i in range(len(x0)-1):
        if ti == 0: #Second order time scheme - has no way of going from t=0 to t=dt
            xy[i,:,ti+1] = 2*xy[i,:,ti] + 0 + (dt**2)*(-ks*(dist[i]-lr) + ks*(dist[i+1]-lr) - kd*relVel[:,i] + kd*relVel[:,i+1] + fDrag[:,i])
        else:
            xy[i,:,ti+1] = 2*xy[i,:,ti] - 1*xy[i,:,ti-1] + (dt**2)*(ks*(dist[i]-lr) + ks*(dist[i+1]-lr) - kd*relVel[:,i] - kd*relVel[:,i+1] + fDrag[:,i])*0.001
    


# print(xy[0,1,:])
# print(vxvy)
dx1 = np.full(len(t),0.0)
for time in range(len(t)):
    print(time)
    if time > 0:
        dx1[time] = xy[0,1,time]-  xy[0,1,time-1]
data = np.column_stack((windU,windV,relW[0,1,:],relW[1,1,:]))
headers = ["U Wind Vel","V Wind Vel","First Parti. Rel U Vel","First Parti. Rel V Vel"]
print(tabulate(data,headers=headers,tablefmt='github'))

posdata = np.column_stack((t,xy[0,0,:],dx1,xy[0,1,:],vxvy[0,0,:],vxvy[0,1,:]))
posHeaders = ["Time","1st Part. X Pos","dx","1st Part. Y Pos","1st Part. U Vel","1st Part. V Vel"]
print(tabulate(posdata,headers=posHeaders,tablefmt='github'))