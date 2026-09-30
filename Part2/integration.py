import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def trap(a,b,f,n):
    h = (b-a)/n
    loc = a+h
    interiorSum = 0
    while loc <= b:
        interiorSum += 2 * f(loc)
        loc = loc+h
    I = (h/2)*(f(a) + interiorSum + f(b))
    return I

def simp13(a,b,f,n):
    x = np.linspace(a,b,n+1)
    h = (b-a)/n
    innerSum = 0
    for i in range(1,len(x)):
        if i%2==1:
            innerSum += 4*f(x[i])
        elif i%2 == 0:
            innerSum += 2*f(x[i])
    I = (h/(3))*(f(x[0]) +innerSum+ f(x[-1]))
    return I       

def foi(x):
    return 5 + 3*np.cos(x)

a = 0
b = 3
intervals = 10

trapApp = trap(a,b,foi,intervals)
simp13App = simp13(a,b,foi,intervals)

true = 5*(b-a)+3*(np.sin(b)-np.sin(a))


xapp = np.linspace(a,b,intervals)
fapp = foi(xapp)

x = np.linspace(a-1/5,b+b/5,30)
f = foi(x)

fig, ax = plt.subplots(1,2,figsize=(10,4))
l, = ax[0].plot(xapp,fapp,'o-',lw=2,color='black')
t = ax[0].vlines(xapp[1:-1], ymin=0, ymax=fapp[1:-1], colors='black', linewidths=1, linestyle='-')
ax[0].plot(x,f,'r',label='f(x) = 5+3cos(x)',lw=1.5)
ax[0].plot([a,a],[0,10],'--',color='black')
ax[0].plot([b,b],[0,10],'--',color='black')
ax[0].set_xlim(a-1/5,b+b/5)
ax[0].set_ylim(0,8.6)
ax[0].set_xlabel('x')
TrapText = ax[0].text(1.7,7.7, f'True Value: {true:.4f}', fontsize=10, va='bottom',bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 3})
TrapText = ax[0].text(1.7,7, f'Trap. App: {trapApp:.4f}', fontsize=10, va='bottom',bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 3})

fig.subplots_adjust(bottom=0.25)
axstep = fig.add_axes((0.25, 0.1, 0.65, 0.03))
step_slider = Slider(
    ax=axstep,
    label='Trap Intervals',
    valmin=1,
    valmax=50,
    valstep=1,
    valinit=intervals,
)

def update(val,trap,foi):
    steps = step_slider.val
    xapp = np.linspace(a,b,steps+1)
    fapp = foi(xapp)
    l.set_xdata(xapp)
    l.set_ydata(fapp)
    new_segments = [np.array([[x, 0], [x, y]]) for x, y in zip(xapp[1:-1], fapp[1:-1])] #Purely Gemini
    t.set_segments(new_segments)
    fig.canvas.draw_idle()
    I = trap(a,b,foi,val)
    TrapText.set_text(f'Trap. App: {I:.4f}')

   

step_slider.on_changed(lambda val: update(val, trap, foi)) #Lambda function also from Gemini

fig.legend()
plt.show()

