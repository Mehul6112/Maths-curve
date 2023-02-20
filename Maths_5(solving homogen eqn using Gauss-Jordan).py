import numpy as np

print("-----GAUSS-JORDAN METHOD-----")

A = np.matrix(input("Write elements separated by spaces and separate rows with semi-colon: \n"))
print("Matrix A is: \n", A)

B = np.matrix(input("\n Write elements separated by spaces and separate rows with semi-colon: \n"))
print("Matrix B is: \n", B) 

# Compute the inverse of A using numpy.linalg.inv()
A_inv = np.linalg.inv(A)
print("/n Inverse of Matrix A is: \n {}".format(A_inv))

# Compute the solution vector x using the Gauss-Jordan method
x = np.dot(A_inv, B)

# Print the solution vector
print("\n Solution vector: \n")
print(x)
