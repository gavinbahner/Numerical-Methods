import numpy as np
from tabulate import tabulate

x = np.linspace(0,0.3,4)
h = x[1] - x[0]
y = np.zeros(len(x))
y[0] = 1
def f(x,y):
    return np.cos(x)*y - np.sin(x)
for i in range(len(x)-1):
    y2 = y[i] + (h/2)*(f(x[i],y[i]))
    y[i+1] = y[i] + h*f(x[i]+h/2,y2)

print(y)
data = np.column_stack((x,y))
headers = ["x pos","y pos"]
print(tabulate(data,headers=headers,tablefmt='github'))