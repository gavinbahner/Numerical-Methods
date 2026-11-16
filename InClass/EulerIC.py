import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

t = np.linspace(0,4,9)
h = t[1] - t[0]

y1 = np.zeros(len(t))
y2 = np.zeros(len(t))
y3 = np.zeros(len(t))

y1[0] = 0
y2[0] = -1
y3[0] = 2

for i in range(len(t)-1):
    y1[i+1] = y1[i] + h*y2[i]
    y2[i+1] = y2[i] + h*y3[i]
    y3[i+1] = y3[i] + h*(5*y3[i]-y2[i]-y1[i]+np.sin(t[i]))

print(y1)
plt.plot(y1,t)
data = np.column_stack((t,y1,y2,y3))
print(tabulate(data,tablefmt='github'))
# plt.show()
