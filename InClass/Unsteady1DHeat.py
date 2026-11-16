import numpy as np
#EXPLICIT
# lamba = (k*dt)/(dx**2)
lamb = 0.0875
T0 = 100
TE = 50
arr = [
    [1-2*lamb,lamb,0,0],
    [lamb,1-2*lamb,lamb,0],
    [0,lamb,1-2*lamb,lamb],
    [0,0,lamb,1-2*lamb]
]
#sol of form: x = [T1 T2 T3 T4]
RHS = [
    [-T0],
    [0],
    [0],
    [-TE]
]
A = np.array(arr)
b = np.array(RHS)
x = np.linalg.solve(A,b)
print(x)

#IMPLICIT
