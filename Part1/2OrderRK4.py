import numpy as np
import matplotlib.pyplot as plt

xt = np.arange(0,5.5,0.01)
c1 = 4
c2 = (0.3*4) / np.sqrt(7.91)
exp = np.exp(-0.3 * xt)
trig = (c1 * np.cos(np.sqrt(7.91) * xt)) + (c2 * np.sin(np.sqrt(7.91) * xt))
sol = exp * trig

h=0.25
x = np.arange(0,5.5,h)
h2=0.5
x2 = np.arange(0,5.5,h2)
def f1(v2):
    return v2

def f2(v1,v2):
    return -0.6*v2 - 8*v1

y1 = np.zeros(len(x))
y1[0] = 4
y2 = np.zeros(len(x))
y2[0] = 0
y3 = np.zeros(len(x2))
y3[0] = 4
y4 = np.zeros(len(x2))
y4[0] = 0

def RK(h,x,y1,y2):
    for i in range(len(x)-1):
        k1 = f1(y2[i])
        o1 = f2(y1[i],y2[i])

        k2 = f1(y2[i]+(h/2)*o1)
        o2 = f2(y1[i]+(h/2)*k1,y2[i]+(h/2)*o1)
        
        k3 = f1(y2[i]+(h/2)*o2)
        o3 = f2(y1[i]+(h/2)*k2,y2[i]+(h/2)*o2)

        k4 = f1(y2[i]+(h)*o3)
        o4 = f2(y1[i]+(h)*k3,y2[i]+(h)*o3)

        y1[i+1] = y1[i] + (h/6)*(k1+2*k2+2*k3+k4)
        y2[i+1] = y2[i] + (h/6)*(o1+2*o2+2*o3+o4)
    return y1,y2

y1,y2 = RK(h,x,y1,y2)
y3,y4 = RK(h2,x2,y3,y4)

for i in range(len(x)):
    print(f"x: {x[i]}, y1: {y1[i]}")  
for i in range(len(x)):
    print(f"x: {x[i]}, y2: {y2[i]}")  
for i in range(len(xt)):
    print(f"x: {xt[i]}, sol: {sol[i]}") 

plt.figure(figsize=(10,5))
plt.plot(x,y1,'o',label='y, h=0.25')
plt.plot(x2,y3,'o',label='y, h=0.5')
# plt.plot(x,y2,'x',label='y \'')
plt.plot(xt,sol,label='Exact Solution',color='green')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Runge-Kutta 4th Order Method for y"+0.6y\'+8y=0')
plt.grid()
plt.show()
