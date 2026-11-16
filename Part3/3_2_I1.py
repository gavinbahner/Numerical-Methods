import numpy as np
import matplotlib.pyplot as plt

mesh = np.zeros((9,9))
dx = 1
dy = 1
h = (dx**2 + dy**2)/((dx**2)*(dy**2))
nRows = len(mesh[:,0])
nCols = len(mesh[0,:])
#Boundary Conditions
for i in range(1,nRows-1):
    mesh[i,0] = (i-1)*20

#Ghost Node Temperature Assignment

for i in range (1,nCols-1):
    mesh[0,i] = mesh[2,i] #Due to Zero heat flux
    mesh[nRows-1,i] = mesh[nRows-1-2,i]

r = 1
while r<=4:
    for j in range(1,nCols-1):
        mesh[r,j] = 0.25*(mesh[r-1,j] + mesh[r+1,j] + mesh[r,j-1] + mesh[r,j+1])
    r+=1
while r<=7:
    for j in range(1,int((nCols-1)/2)):
        mesh[r,j] = 0.25*(mesh[r-1,j] + mesh[r+1,j] + mesh[r,j-1] + mesh[r,j+1])  
    r+=1

np.set_printoptions(
    precision=2,
    suppress=True,
    linewidth=100,
    edgeitems=5
)

plt.imshow(mesh, cmap='inferno',interpolation='nearest')
plt.show()