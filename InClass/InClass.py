
import numpy as np
dx = 5
dy = 5
fact = -2*(1/(dx**2)) - 2*(1/(dy**2))
nonUniGrid = [
    [fact,1/(dx**2),0],
    [1/(dx**2),fact,1/(dx**2)],
    [0,1/(dx**2),fact]
]


Grid = [
    [-4,1,0],
    [1,-4,1],
    [0,1,-4]
]

RHS = [
    [0],
    [0],
    [-100]
]
A = np.array(Grid)
b = np.array(RHS)
x = np.linalg.solve(A,b)
print(x)
