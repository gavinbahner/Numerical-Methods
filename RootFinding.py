import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x**3 -11.7*x**2+17.7*x-5

def df(x):
    return 6*x**2 - 23.4*x + 17.7

def d2f(x):
    return 12*x - 23.4

def altNR(x0, tol,maxIter):
    x = np.zeros((maxIter))
    x[0] = x0
    for i in range(len(x)-1):
        x[i+1] = x[i] - (f(x[i])*df(x[i])) / ((df(x[i]))**2 - f(x[i])*d2f(x[i]))
        if ( abs(f(x[i+1]) - f(x[i])) ) < tol or (i == maxIter):
            return x[0:i+1], i
        else:
            continue
def NR(x0, tol,maxIter):
    x = np.zeros((maxIter))
    x[0] = x0
    for i in range(len(x)-1):
        x[i+1] = x[i] - f(x[i])/df(x[i])
        if ( abs(f(x[i+1]) - f(x[i])) ) < tol or (i == maxIter):
            return x[0:i+1], i
        else:
            continue

iter = 10
x,g = altNR(3,1e-5,iter) 
y = f(x)
yp = df(x)
ydp = d2f(x)

x2,g2 = NR(3,1e-5,iter)
y2 = f(x2)
yp2 = df(x2)
ydp2 = d2f(x2)

x3 = np.zeros((iter))
x3[0] = 3.1
g3 = np.zeros((iter))
c = 0
for i in range(len(x3)-1):
    x3[i+1] = -1*(2*(x3[i])**3 - 11.7*(x3[i]**2) - 5)/17.7
    c=i

y3 = f(x3)

plt.figure(figsize=(10,5))
plt.plot(np.linspace(0,5.5,120),f(np.linspace(0,5.5,120)),label='f(x)',color='blue')
plt.plot(x,y,'o',label='Alternative Newton Raphson in '+str(g) + ' Guesses')
plt.plot(x2,y2,'o',label='Newton Raphson in '+str(g2) + ' Guesses')  
plt.plot(x3,y3,'o',label='FP in '+str(c) + ' Guesses') 
plt.axhline(0, color='black', lw=0.5)
plt.xlabel('x') 
plt.ylabel('f(x)')
plt.title('Roots of f(x) = 2x^3 - 11.7x^2 + 17.7x - 5 using Newton-Raphson Methods')                                  
plt.legend()
plt.show()

# print("x\t\tf(x)\t\tf'(x)\t\tf''(x)")
# for i in range(len(x)):
#     print(f"{x[i]:.5f}\t\t{y[i]:.5f}\t\t{yp[i]:.5f}\t\t{ydp[i]:.5f}")

# print("x\t\tf(x)\t\tf'(x)\t\tf''(x)")
# for i in range(len(x2)):
#     print(f"{x2[i]:.5f}\t\t{y2[i]:.5f}\t\t{yp2[i]:.5f}\t\t{ydp2[i]:.5f}")

    # print("x\t\tf(x)\t\tf'(x)\t\tf''(x)")
for i in range(len(x3)):
    print(f"{x3[i]:.5f}\t\t{g3[i]:.5f}\t")