import numpy as np
import matplotlib.pyplot as plt

x = np.array([-2,0,2,4,6,8,10])
f = np.array([35, 5, -10, 2, 5, 3, 20])

def trap(x,f):
    a = x[0]
    b = x[-1]
    n = len(x) - 1
    h = (b-a)/n
    interiorSum = 0
    for i in range(1,n):
        interiorSum += 2 * f[i]
    I = (h/2)*(f[0] + interiorSum + f[-1])
    return I

def simp38(x,f):
    iS = 0
    for i in range(0,(len(f)-3),3):
        iS += f[i] + 3*f[i+1] + 3*f[i+2] + f[i+3]
    I = (3*(x[1]-x[0])/8)*(iS)
    return I


def simp13(x,f):
    iS =0 
    for i in range(1,(len(f)-2),2):
        iS += 4*f[i] + 2*f[i+1]
    I = ((x[1]-x[0])/3)*(f[0] + iS + f[-1])
    return I

print("Simpson's 3/8: "+str(simp38(x,f)))
print("Simpson's 1/3: "+str(simp13(x,f)))
print("Trapezoidal: "+str(trap(x,f)))