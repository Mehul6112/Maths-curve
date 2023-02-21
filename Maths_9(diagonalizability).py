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
    print("\n The matrix is diagonalizable.")
else:
    print("\n The matrix is not diagonalizable. \n")
    
# Checking if the given matrix satisfies CHT
B = np.array([[2, -1, 0], [1, 4, -1], [0, 1, 3]])
bp = np.poly(B)
print("\n Characteristic polynomial of B: ", bp, "\n")
subs_b = np.dot(np.dot(B, B), B) -9*(np.dot(B, B)) +28*B -29*np.eye(3)

#substituting the matrix B into the characteristic polynomial bp 
# and checking if the resulting expression is equivalent to zero.

if np.allclose(subs_b, np.zeros((3, 3))):
    print("The matrix B satisfies Cayley-Hamilton Theorem.")
else:
    print("The matrix B doesn't satisfy Cayley-Hamilton Theorem.")
