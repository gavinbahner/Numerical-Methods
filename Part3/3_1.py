import numpy as np
import matplotlib.pyplot as plt

dx = 2
S = 1
n = 10 #Number of points in domain
A = np.zeros((n-2,n-2))
A[0,0] = -3/2
A[0,1] = 3/2
for i in range(1,n-3):
    A[i,i-1] = 1 - 1/(2*(i+1))
    A[i,i] = -2
    A[i,i+1] = 1 + 1/(2*(i+1))
A[n-3,n-3] = -2
A[n-3,n-3] = -2
A[n-3,n-4] = 1 - 1/(2*(n-2))

b = np.full((n-2),1)
b[-1] = (1 + 1/(2*(n-2)))/(S*(dx)**2) + 1
b = -1*(S*(dx)**2)*b

x = np.linalg.solve(A,b)

with np.printoptions(precision=2, floatmode="fixed"):
    print(x)