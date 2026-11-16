import numpy as np
def RK4(h,x,y1,y2):
    for i in range(len(x)-1):
        k1 = f1(y2[i])
        o1 = f2(y1[i],y2[i],t[i])

        k2 = f1(y2[i]+(h/2)*o1)
        o2 = f2(y1[i]+(h/2)*k1,y2[i]+(h/2)*o1,t[i])
        
        k3 = f1(y2[i]+(h/2)*o2)
        o3 = f2(y1[i]+(h/2)*k2,y2[i]+(h/2)*o2,t[i])

        k4 = f1(y2[i]+(h)*o3)
        o4 = f2(y1[i]+(h)*k3,y2[i]+(h)*o3,t[i])

        y1[i+1] = y1[i] + (h/6)*(k1+2*k2+2*k3+k4)
        y2[i+1] = y2[i] + (h/6)*(o1+2*o2+2*o3+o4)
    return y1,y2


def f1(x2):
    return x2
def f2(x1,x2,t):
    x2-t*x1+np.cos(t)
h = np.pi/4
t = np.linspace(0,np.pi,4)
x1 = np.zeros(len(t))
x2 = np.zeros(len(t))
x1[0],x2[0] = -1*np.pi()
out = RK4(h,t,x1,x2)