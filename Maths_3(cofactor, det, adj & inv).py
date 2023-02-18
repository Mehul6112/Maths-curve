import numpy as np

#3.Find Cofactors, Determinant, Adjoint and Inverse of a Matrix.

# Creating a Matrix

matrix = np.array([[5,3,4], [3,1,-2], [-2,0,-3]])
print("Matrix is:\n", matrix)

#Cofactors of a Matrix:

def cofactor(matrix):
    n = matrix.shape[0]
    cofactor_matrix = np.zeros(matrix.shape)
    for i in range(n):
        for j in range(n):
            sub_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            sign = (-1) ** (i + j)
            cofactor_matrix[i, j] = sign * np.linalg.det(sub_matrix)
    return cofactor_matrix

cofactor_matrix = cofactor(matrix)
print("Cofactors of The Given Matrix is:")
print(cofactor_matrix)

#Adjoint of a Matrix:

def adjoint(matrix):
    return np.transpose(cofactor(matrix))

adjoint_matrix = adjoint(matrix)
print("Adjoint of The Given Matrix is:\n",adjoint_matrix)

#Determinant of a Matrix:

def determinant(matrix):
    determinant_matrix=np.linalg.det(matrix)
    return 'Determinant of The Given Matrix is:' , determinant_matrix

print(determinant(matrix))

#Inverse of a Matrix:

inverse_matrix=np.linalg.inv(matrix)
print("Inverse of The Given Matrix is:\n",inverse_matrix)
