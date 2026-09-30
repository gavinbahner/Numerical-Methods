import numpy as np
import matplotlib.pyplot as plt
def regression(x,y):
    sumx = np.sum(x, axis=0)
    sumy = np.sum(y, axis=0)
    sumxy = np.sum(x*y)
    sumx2 = np.sum(x**2)
    n = len(x)
    a1 = (n*sumxy - sumx*sumy) / (n*sumx2 - (sumx)**2)
    a0 = sumy/n - a1*(sumx/n)
    return a0,a1