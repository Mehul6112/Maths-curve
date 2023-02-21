import numpy as np

# Defining a matrix
A = np.array([[1, 2], [3, 4]])

# Finding the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Matrix A is: \n", A)
print("\n Eigenvalues are: \n", eigenvalues)
print("\n Eigenvectors are: \n", eigenvectors)

diag_eigval = np.diag(eigenvalues)
p_inv = np.linalg.inv(eigenvectors)
p = eigenvectors
    
# Checking if the matrix is diagonalizable
if np.allclose(diag_eigval, np.dot(p_inv, np.dot(A, p))):
    print("The matrix is diagonalizable.")
else:
    print("The matrix is not diagonalizable.")
    

