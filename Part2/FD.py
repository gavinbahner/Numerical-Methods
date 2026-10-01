import numpy as np
import matplotlib.pyplot as plt

l = 10
dx=1

A = np.zeros((9,9))
for i in range(A.shape[0]):
    if i>0:
        A[i,i-1] = 1
    A[i,i] = -2 - 0.15 * (dx**2)
    if i<8:
        A[i,i+1] = 1

t = np.zeros(9)
t[0] = -240
t[-1] = -150

T = np.linalg.solve(A,t)
TFinal = np.concatenate(([240],T,[150]))
x = np.linspace(0,l,11)

N = np.zeros((10,10))
for i in range(N.shape[0]):
    if i>0:
        N[i,i-1] = 1
    N[i,i] = - 2 - 0.15*(dx**2)
    if i<9:
        N[i,i+1] = 1
N[0,1] = 2
tN = np.zeros(10)
tN[0] = 0
tN[-1] = -150
N = np.linalg.solve(N,tN)
NFinal = np.concatenate((N,[150]))

print("Matrix,A")
print(N)
print("b")
print(tN)
print("Solution, x")
print(NFinal)

def T(x):
    return 3.017*np.exp(x*np.sqrt(0.15))+236.98*np.exp(x*-1*np.sqrt(0.15))
xt = np.linspace(0,l,50)
Ttrue = T(xt)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(x,TFinal,'o',zorder=1,label='2nd Order FD Approximation')
ax[0].plot(xt,Ttrue,'-',zorder=-1,label='Analytical Solution')
ax[0].set_title("Temperature dist. with BC: T(0) = 240, T(10) = 150",fontsize=9,style='oblique')
ax[0].set_xlim(0,10)
ax[0].set_ylim(45,250)
ax[0].legend()

ax[1].plot(x,NFinal,'o',zorder=1,label='2nd Order FD Approximation')
# ax[1].plot(xt,Ttrue,'-',zorder=-1,label='Analytical Solution')
ax[1].set_title("Temperature dist. with Insulated BC: T'(0) = 0, T(10) = 150",fontsize=9,style='oblique')
ax[1].set_xlim(0,10)
ax[1].set_ylim(0,250)
ax[1].legend()

plt.show()

 

