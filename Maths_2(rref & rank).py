import numpy as np
from sympy import Matrix
from sympy import *

#2.Generate The Matrix into Echelon Form and Find its Rank.

# Creating a Matrix

matrix= Matrix([[3, 7, 9,],[5, 2, 1,],[-2, -9, 8]])

print("Matrix is: \n ")
print(np.array(matrix).astype(np.float64))

#Finding Reduced Row Echelon Form of The Matrix

def echelon_form(matrix):
    print("\n ROW REDUCED ECHELON FORM OF THE MATRIX\n")
    print("Reduced Row Echelon Form is: \n ")
    return (np.array(matrix.rref()[0]).astype(np.float64))

print(echelon_form(matrix))

#Finding Rank of The Matrix

def rank_matrix(matrix):
    print("\n RANK OF THE MATRIX\n")
    print("Rank of matrix is: \n ")
    return np.linalg.matrix_rank(np.array(matrix).astype(np.float64))

print(rank_matrix(matrix))
