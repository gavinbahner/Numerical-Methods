import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.75,2,3,4,6,8,8.5])
y = np.array([1.2,1.95,2,2.4,2.4,2.7,2.6])
xm = np.linspace(0.75,8.5,25)
logx = np.log(x)
logy = np.log(y)
invx = 1/x
invy = 1/y
p = x*x

def regression(x,y):
    sumx = np.sum(x, axis=0)
    sumy = np.sum(y, axis=0)
    sumxy = np.sum(x*y)
    sumx2 = np.sum(x**2)
    n = len(x)
    a1 = (n*sumxy - sumx*sumy) / (n*sumx2 - (sumx)**2)
    a0 = sumy/n - a1*(sumx/n)
    return a0,a1

def polyRegression(x,y):
    sumx = np.sum(x, axis=0)
    sumx2 = np.sum(x**2)
    sumx3 = np.sum(x**3)
    sumx4 = np.sum(x**4)
    sumy = np.sum(y, axis=0)
    sumxy = np.sum(x*y)
    sumx2y = np.sum((x**2)*y)
    n = len(x)
    A = np.array([[n,sumx,sumx2],[sumx,sumx2,sumx3],[sumx2,sumx3,sumx4]])
    b = np.array([sumy,sumxy,sumx2y])
    aS = np.linalg.solve(A,b)
    return aS


fig, axs = plt.subplots(3, 2, figsize=(10, 8))
PLa0,PLa1 = regression(logx,logy)
Rlogy = PLa0 + PLa1*logx
axs[0,0].plot(logx,Rlogy,'-',logx,logy,'o')
axs[0,0].set_title('Linearized')
axs[0,0].set_xlabel('log(x)')
axs[0,0].set_ylabel('log(y)')

Ry = np.exp(PLa0) * xm**PLa1
axs[0,1].plot(x,y,'o',xm,Ry,'-')
axs[0,1].set_title('x vs. y with Power Law Model')
axs[0,1].set_xlabel('x')
axs[0,1].set_ylabel('y')

SGa0, SGa1 = regression(invx,invy)
SGy = SGa0 + SGa1*invx
axs[1,0].plot(invx,SGy,'-',invx,invy,'o')
axs[1,0].set_title('Linearized')
axs[1,0].set_xlabel('1/x')
axs[1,0].set_ylabel('1/y')

R2y = 1/SGa0 * (xm/(xm+SGa1*(1/SGa0)))
axs[1,1].plot(x,y,'o',xm,R2y,'-')
axs[1,1].set_title('x vs. y with Saturation/Growth Model')
axs[1,1].set_xlabel('x')
axs[1,1].set_ylabel('y')


a = polyRegression(x,y)

R3y = a[0] + a[1]*xm + a[2]*(xm**2)
axs[2,1].plot(x,y,'o',xm,R3y,'-')
axs[2,1].set_title('Parabolic Regression')
axs[2,1].set_xlabel('x')
axs[2,1].set_ylabel('y')

plt.tight_layout()
plt.show()