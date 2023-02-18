import numpy as np
from sympy import Matrix
from sympy import *

#6.Generate Basis of Column Space, Null Space, Row Space and Left Null Space of a Matrix Space

matrix = Matrix([[1, 2, -1], [-2, -4, 2], [3, 6, -3]])
print("Matrix is:\n", matrix)

#To Find The Column Space of The Matrix:

print("\n COLUMN SPACE OF THE MATRIX\n")
matrix_columnspace=matrix.columnspace()
print("\nThe Column Space of the Matrix is:\n",matrix_columnspace, "\n")

#To Find The Row Space of The Matrix:

print("\n ROW SPACE OF THE MATRIX\n")
matrix_rowspace=matrix.rowspace()
print("\nThe Row Space of the Matrix is:\n",matrix_rowspace)

#To Find The Null Space of The Matrix:

print("\n NULL SPACE OF THE MATRIX\n")
matrix_nullspace=matrix.nullspace()
print("\nThe Null Space of the Matrix is:\n",matrix_nullspace)


#To Find The Left Null Space of The Matrix:

print("\n LEFT NULL SPACE OF THE MATRIX\n")
AB = matrix.T
matrix_leftnullspace = AB.nullspace()  
      
print("\nMatrix Transpose is :\n ")
print(AB)

print("\nLeft Null Space of the Matrix is: \n")
print(matrix_leftnullspace)
