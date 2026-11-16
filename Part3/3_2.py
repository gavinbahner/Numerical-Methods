import numpy as np
import matplotlib.pyplot as plt

H = 10
W = H*4/3

nx = 10
ny = 6

dx = W/(nx-1)
dy = H/(ny-1)
mesh = np.zeros((nx+2,ny)) #need 2 extra rows for ghost points

for i in range(1,len(mesh)-1):
    intNodes = len(mesh)-3
    dT = 120/intNodes
    mesh[i,0] = dT*(i-1)


print(mesh)
print(dx,dy)