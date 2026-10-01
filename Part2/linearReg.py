import numpy as np
import matplotlib.pyplot as plt
from regression import regression

c = np.array([0.5,0.8,1.5,2.5,4])
cm = np.linspace(0.4,5,20)
k = np.array([1.1,2.4,5.3,7.6,8.9])
invk = 1/k
invc2 = 1/(c**2)
invcm2 = 1/(cm**2)
a0,a1 = regression(invc2,invk)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

link = a1*(invcm2) + a0
axs[0].plot(invc2,invk,'o',invcm2,link,'-')
axs[0].set_title('Linearized')
axs[0].set_xlabel('1/c^2')
axs[0].set_ylabel('1/k')
axs[0].set_xlim(0,5)
axs[0].set_ylim(0,1)
axs[0].text(1.2, 0.15, f'Form: y = a1*x + a0 with a1={a1:.2f}, a0={a0:.2f}', fontsize=8, va='bottom',bbox={'facecolor': 'blue', 'alpha': 0.3, 'pad': 3})

def kmodel(c):
     return ((1/a0)*(c**2))/(a1/a0 + (c**2))

axs[1].plot(c,k,'o',cm,kmodel(cm),'-')
axs[1].set_title('c vs. k with Known Model')
axs[1].set_xlabel('c [mg/L]')
axs[1].set_ylabel('k')
axs[1].set_xlim(0,5)
axs[1].set_ylim(0,10)
axs[1].plot([2,2],[0,kmodel(2)],'-*')
axs[1].plot([2,0],[kmodel(2),kmodel(2)],'-*')
axs[1].text(2.2, 1.6, 'c=2', fontsize=10, va='bottom',bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 3})
axs[1].text(0.25, 7, f'k(c=2) = {kmodel(2):.2f}', fontsize=10, va='bottom',bbox={'facecolor': 'red', 'alpha': 0.8, 'pad': 3})
plt.show()



