import numpy as np
import matplotlib.pyplot as plt

h=0.1
t= np.arange(0,0.4+h,h)

y = np.zeros(len(t))
y[0] = 2
z = np.zeros(len(t))
z[0] = 4

def f1(y,z,t):
    return -2*y + 5*np.exp(-t)
def f2(y,z,t):
    return -(y * (z**2) )/2
#Euler

for i in range(len(t)-1):
    y[i+1] = y[i] + f1(y[i],z[i],t[i])*h
    z[i+1] = z[i] + f2(y[i],z[i],t[i])*h

#RK4
ry = np.zeros(len(t))
ry[0] = 2
rz = np.zeros(len(t))
rz[0] = 4

for i in range(len(t)-1):
    k1 = f1(ry[i],rz[i],t[i])
    l1 = f2(ry[i],rz[i],t[i])

    k2 = f1(ry[i]+0.5*h*k1,rz[i]+0.5*h*l1,t[i]+0.5*h)
    l2 = f2(ry[i]+0.5*h*k1,rz[i]+0.5*h*l1,t[i]+0.5*h)

    k3 = f1(ry[i]+0.5*h*k2,rz[i]+0.5*h*l2,t[i]+0.5*h)
    l3 = f2(ry[i]+0.5*h*k2,rz[i]+0.5*h*l2,t[i]+0.5*h)

    k4 = f1(ry[i]+h*k3,rz[i]+h*l3,t[i]+h)
    l4 = f2(ry[i]+h*k3,rz[i]+h*l3,t[i]+h)

    ry[i+1] = ry[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    rz[i+1] = rz[i] + (h/6)*(l1 + 2*l2 + 2*l3 + l4)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  

ax1.plot(t,y,'s-',label='Euler: y')
ax1.plot(t,ry,'o--',label='RK4: y')
ax1.set_ylabel('y')
ax1.set_xlabel('t')
ax1.set_title("y vs. t")
ax1.legend()


ax2.plot(t,z,'x-',label='Euler: z')
ax2.plot(t,rz,'d--',label='RK4: z')
ax2.set_ylabel('z')
ax2.set_xlabel('t') 
ax2.legend()
ax2.set_title("z vs. t")
plt.show()

plt.plot(figsize=(10, 4))
plt.plot(z,y,'-')
# plt.show()
print("t\t\ty\t\tz")
for i in range(len(t)):
    print(f"{t[i]:.2f}\t\t{y[i]:.2f}\t\t{z[i]:.2f}")
