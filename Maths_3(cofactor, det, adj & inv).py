import numpy as np

#3.Find Cofactors, Determinant, Adjoint and Inverse of a Matrix.

# Creating a Matrix
matrix = np.array([[5,3,4], [3,1,-2], [-2,0,-3]])
print("Matrix is: \n", matrix)

#Determinant of a Matrix:
determinant_matrix=np.linalg.det(matrix)
print("\n Determinant of The Given Matrix is:\n" , determinant_matrix)

#Inverse of a Matrix:
inverse_matrix=np.linalg.inv(matrix)
print("\n Inverse of The Given Matrix is: \n",inverse_matrix)

#Adjoint of a matrix:
adjoint_matrix = inverse_matrix*determinant_matrix
print("\n Adjoint of The Given Matrix is: \n" , adjoint_matrix)

#Cofactor of a matrix:
cofactor_matrix = np.transpose(adjoint_matrix)
print("\n Cofactor of The Given Matrix is: \n", cofactor_matrix)
