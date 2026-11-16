import numpy as np

Nx = 20
Ny = 12

slice = np.full((4,Nx,Ny),30.)
slice[0,:,:] = 25
slice[-1,:,:] = 35
slice[:,4,5] = (15+20)/2
slice[:,5:,5] = 15
slice[:,4,6:] = 20
slice[:,5:,6:] = np.nan
print(slice)
