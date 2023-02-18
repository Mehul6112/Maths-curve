import numpy as np
#12.>Compute Divergence of a vector field

print("\n DIVERGENCE  OF THE MATRIX\n")
#Creating a Matrix

matrix= np.array([6, 4, 9, 13, 22, 69], dtype=float)

#Finding Divergence of a Matrix

def divergence(F):
    return np.ufunc.reduce(np.add,np.gradient(F))

print("Input  :\n ", matrix)

print("Divergence :\n ",divergence(matrix))