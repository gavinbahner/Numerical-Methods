import numpy as np
import matplotlib.pyplot as plt

def f(y,t):
    return y*(t**2)-1.1*y

#vi+1 = vi + ai * dt
t = np.arange(0, 2, 0.01)
t1 = np.arange(0, 2.5, 0.5)
t2 = np.arange(0, 2.25, 0.25)

y = np.exp(-1.1*t + (t**3)/3)
y1 = np.zeros(len(t1))
y1[0]=1
y2 = np.zeros(len(t2)) 
y2[0]=1
y3 = np.zeros(len(t1))
y3[0]=1
y4 = np.zeros(len(t1))
y4[0]=1

for i in range(len(t1)-1):
    y1[i+1] = y1[i] + f(y1[i],t1[i]) * 0.5

for i in range(len(t2)-1):
    y2[i+1] = y2[i] + f(y2[i],t2[i]) * 0.25

for i in range(len(t1)-1):
    k2 = f( y3[i]+0.5/2*f(y3[i],t1[i]), t1[i]+0.5/2)
    y3[i+1] = y3[i] + k2*0.5

for i in range(len(t1)-1):
    k1 = f(y4[i],t1[i])
    k2 = f(y4[i]+0.5*k1*0.5, t1[i] + 0.5/2)
    k3 = f(y4[i]+(0.5/2)*k2, t1[i] + 0.5/2)
    k4 = f(y4[i]+0.5*k3, t1[i]+0.5)
    y4[i+1] = y4[i] + 1/6*(k1+2*k2+2*k3+k4)*0.5

for i in range(len(t1)):
    print(f"t1: {t1[i]}, y1: {y1[i]}")  
for i in range(len(t2)):
    print(f"t2: {t2[i]}, y2: {y2[i]}") 

plt.figure(figsize= (10,5))
plt.plot(t,y,label='Exact', color='green')
plt.plot(t1,y1,'o',label='Euler: ∆t=0.5', color='blue')
plt.plot(t2,y2,'x',label='Euler: ∆t=0.25', color='red')
plt.plot(t1,y3,'s',label='Midpoint', color='cyan')
plt.plot(t1,y4,'d',label='RK4', color='black')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.title('Comparison of Numerical Methods for dy/dt=y(t^2)-1.1')
plt.show()

