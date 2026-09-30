import numpy as np
import matplotlib.pyplot as plt

x = np.array([3,4,5,7,8,9,11,12])
y = np.array([1.6,3.6,4.4,3.4,2.2,2.8,3.8,4.6])
xm = np.linspace(3,12,150)
def polyRegression(x,y,o):
    A = np.zeros((o+1,o+1))
    sumx = np.zeros((2*o+1))
    for i in range(0,2*o+1):
        sumx[i] = np.sum(x**i)
    sumxy = np.zeros((o+1))
    for i in range(0,o+1):
        sumxy[i] = np.sum(y*x**i)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            A[i,j] = sumx[j+i]
    
    b = sumxy
    aS = np.linalg.solve(A,b)
    return aS


cubic = polyRegression(x,y,3)
quartic = polyRegression(x,y,4)
fifth = polyRegression(x,y,5)
tenth = polyRegression(x,y,8)

fits = [cubic,quartic,fifth,tenth]
yfits = np.zeros((len(fits),len(x)))
yfitsCurve = np.zeros((len(fits),len(xm)))
for i in range(len(fits)):
    for j in range(len(fits[i])):
        yfits[i] += fits[i][j]*(x**j)
        yfitsCurve[i] += fits[i][j]*(xm**j)

Sr = np.zeros(len(fits))
St = np.zeros(len(fits))
R2 = np.zeros(len(fits))
syx = np.zeros(len(fits))
m = [3,4,5,8]
ymean = np.sum(y)/len(y)
for i in range(yfits.shape[0]):
    for j in range(len(yfits[i])):
        Sr[i] += (y[j] - yfits[i][j])**2
        St[i] += (ymean - yfits[i][j])**2
    if len(x) > m[i]+1:
        syx[i] = np.sqrt(Sr[i]/(len(x)-(m[i]+1)))
    R2[i] = (St[i] - Sr[i])/St[i]



fig, ax = plt.subplots(2,2,figsize=(8, 5))
for a in ax.flatten():
    a.set_ylim((1,5.5))

ax[0,0].plot(x, y, color='crimson', lw=0,marker='o',label='Actual Data')
ax[0,0].plot(xm, yfitsCurve[0], color='blue', label='Cubic')
ax[0,0].set_ylabel('y') 
ax[0,0].text(3.5, 5, f'R2={R2[0]:.3f},  Sy/x={syx[0]:.3f}', style='italic', fontsize=6,
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 3,'zorder':-1})

ax[0,1].plot(x, y, color='crimson', lw=0,marker='o')
ax[0,1].plot(xm, yfitsCurve[1], color='green', label='Quartic')
ax[0,1].text(3.5, 5, f'R2={R2[1]:.3f},  Sy/x={syx[1]:.3f}', style='italic', fontsize=6,
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 3,'zorder':-1})

ax[1,0].plot(x, y, color='crimson', lw=0,marker='o')
ax[1,0].plot(xm, yfitsCurve[2], color='orange', label='Fifth-Order Polynomial')
ax[1,0].set_ylabel('y')
ax[1,0].text(3.5, 5, f'R2={R2[2]:.3f},  Sy/x={syx[2]:.3f}', style='italic', fontsize=6,
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 3,'zorder':-1})

ax[1,1].plot(x, y, color='crimson', lw=0,marker='o')
ax[1,1].plot(xm, yfitsCurve[3], color='purple', label='Eight-Order Polynomial')
ax[1,1].text(3.5, 5, f'R2={R2[3]:.3f},  Sy/x={syx[3]:.3f}', style='italic', fontsize=6,
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 3,'zorder':-1})
fig.subplots_adjust(bottom=0.2)
fig.legend( loc='lower center', ncol=2)

fig.suptitle('Polynomial Regression for a Data Set', fontsize=16, fontweight='bold')

plt.show()