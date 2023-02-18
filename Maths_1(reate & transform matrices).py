import numpy as np
from sympy import Matrix
from sympy import *


#1.Create and transform vectors and matrices and transpose them:

#Creating a Vector
vector = np.matrix([9, 8, 7])
print("Vector is:\n", vector )


# Transpose the Vector
print("\nTRANSPOSE THE VECTOR\n")

vector_transpose = vector.T
print("Transpose of The Given Vector is:\n", vector_transpose)

# Creating a Matrix
mat1 = np.matrix([[6, 7, 9], [5, 7, 1], [2, 0, 4]])
print("Matrix is:\n",mat1)

# Transpose of Matrix
print("\nTRANSPOSE THE MATRIX\n")
matrix_transpose = np.transpose(mat1)
print("Transpose of The Given  Matrix is:\n", matrix_transpose)

# Conjugate Transpose of The Matrix

print("\n CONJUGATE TRANSPOSE THE MATRIX \n")
matrix_conjugate_transpose = np.conj(mat1)
print("Conjugate Transpose of The Given matrix is:\n", matrix_conjugate_transpose)
