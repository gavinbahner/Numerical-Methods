import numpy as np
import matplotlib.pyplot as plt 

def f(x):
    return -1 + 5.5*x - 4*x**2 + 0.5*x**3

def df(x):
    return 5.5 - 8*x + 1.5*x**2 

def d2f(x):
    return -8 + 3*x

def g(x):
    return f(x)+x

def NR(x0, tol,maxIter):
    x = np.zeros((maxIter))
    x[0] = x0
    for i in range(len(x)-1):
        x[i+1] = x[i] - f(x[i])/df(x[i])
        if ( abs(f(x[i+1]) - f(x[i])) ) < tol or (i == maxIter):
            return x[0:i+1], i
        else:
            continue

x = np.zeros(100)
x0 = 1
x[0]=x0
x, i = NR(x0,1e-5,100)
y = f(x)

x02 = 0
x2 = np.zeros((100))
x2[0] = x02
for i in range(1,100):
    
    for j in range(len(x2)-1):
        x2[j+1] = x2[j] - f(x2[j])/df(x2[j])
        if (f(x2[j+1]) - f(x2[j])) < 1e-5 or (j == 99):
            break
        else:
            continue
    # print(f"Initial guess: {x02}, Root: {x2[j+1]:.5f}, f(Root): {f(x2[j+1]):.5f}")

y2 = f(x2)
print(x)
print(y)
plt.plot(np.linspace(0,5,100),f(np.linspace(0,5,100)),label='f(x)',color='blue')
plt.plot(x,y,'go--',label="NR with x0=1")
plt.plot(x2,y2,'o--',label="NR with x0=0")
plt.axhline(0, color='black', lw=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title("Finding roots for f(x)=0.5x^3 -4x^2 +5.5x -1")
plt.show()