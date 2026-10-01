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
    print(len(x))
    h = (b-a)/n
    innerSum = 0
    if len(x)%2 == 1:
            for i in range(1,len(x)):
                if i%2==1:
                    innerSum += 4*f(x[i])
                elif i%2 == 0:
                    innerSum += 2*f(x[i])
            return (h/3)*(f(x[0]) + innerSum + f(x[-1]))
    else:
        i=1
        while i < len(x)-2:  
            if i%2==1:
                innerSum += 4*f(x[i])
            elif i%2 == 0:
                innerSum += 2*f(x[i])
            i += 1
        return (h/3)*(f(x[0]) + innerSum + f(x[i])) + ((h/2)*(f(x[i+1])-f(x[i])))
        
def simp38(a,b,f,n):
    x = np.linspace(a,b,n+1)
    print(len(x))
    h = (b-a)/n
    innerSum = 0
    fi = 0
    for i in range(0,len(x),3):
       
        if (len(x)-1) - i >= 3:
            innerSum +=  f(x[i]) + 3*f(x[i+1]) + 3*f(x[i+2]) + f(x[i+3])
        else:
            fi = i
            break
    TSum = 0
    for i in range(n-1-fi):
        TSum += (h/2)*(f(x[fi+i]) + f(x[fi+i+1]))
    I = (3*h/8)*(innerSum) + TSum
    return I

def foi(x):
    return 5 + 3*np.cos(x)

a = 0
b = 3
n=8
intervals = np.linspace(1,100,100)

trapApp = np.zeros(len(intervals))
simp13App = np.zeros(len(intervals))
simp38App = np.zeros(len(intervals))
true = 5*(b-a)+3*(np.sin(b)-np.sin(a))

for i in range(1,len(intervals)-1):
    trapApp[i] = trap(a,b,foi,int(intervals[i]))
    simp13App[i] = simp13(a,b,foi,int(intervals[i]))
    simp38App[i] = simp38(a,b,foi,int(intervals[i]))

plt.plot(intervals,trapApp,'red',label="Trapezoidal")
plt.plot(intervals,simp13App,'blue',label="Simpson's 1/3")
plt.plot(intervals,simp38App,'orange',label="Simpson's 3/8")
plt.plot([0,100],[true,true],'black','--',label='True Value')
plt.xlabel("Number of Intervals")
plt.ylabel("Integral Value")
plt.title('Comparing Integral Approximations with Different Number of Intervals over a Set Distance',fontsize=9)
plt.xlim(2,60)
plt.ylim(10,20)
plt.legend()
plt.show()



simpx = np.linspace(a,b,int(intervals[n]))
simpf = foi(simpx)

xapp = np.linspace(a,b,int(intervals[n]))
fapp = foi(xapp)

x = np.linspace(a-1/5,b+b/5,30)
f = foi(x)

# print('Simpson1/3: '+str(simp13App))
# print('Simpson3/8: '+str(simp38App))
# print('Trap: '+str(trapApp))
# print('True: '+str(true))
fig, ax = plt.subplots(figsize=(6,4))
l, = ax.plot(xapp,fapp,'o-',lw=2,color='black')
t = ax.vlines(xapp[1:-1], ymin=0, ymax=fapp[1:-1], colors='black', linewidths=1, linestyle='-')
ax.plot(x,f,'r',label='f(x) = 5+3cos(x)',lw=1.5)
ax.plot([a,a],[0,10],'--',color='black')
ax.plot([b,b],[0,10],'--',color='black')
ax.set_xlim(a-1/5,b+b/5)
ax.set_ylim(0,8.6)
ax.set_xlabel('x')
ax.set_title('Trapeozidal')
TrapText = ax.text(1.2,7.7, f'True Value: {true:.4f}', fontsize=10, va='bottom',bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 3})
TrapText = ax.text(1.2,7, f'Trap. App: {trapApp[n]:.4f}', fontsize=10, va='bottom',bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 3})



fig.subplots_adjust(bottom=0.25)
axstep = fig.add_axes((0.25, 0.1, 0.65, 0.03))
step_slider = Slider(
    ax=axstep,
    label='Trap Intervals',
    valmin=1,
    valmax=50,
    valstep=1,
    valinit=int(intervals[n]),
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

