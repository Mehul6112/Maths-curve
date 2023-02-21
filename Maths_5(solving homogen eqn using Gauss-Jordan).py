import numpy as np
print("\n-----GAUSS-JORDAN METHOD-----\n")

A = np.matrix(input("Write elements separated by spaces and separate rows with semi-colon: "))
print("Matrix A is \n: ", A, "\n")
#Example_A = 1 1 1;2 -3 4;3 4 5

B = np.matrix(input("\n Write elements separated by semi-colon: "))
print("Matrix B is: \n", B, "\n") 
#Example_B = 9;13;40

#Computing the inverse of A using numpy.linalg.inv()
A_inv = np.linalg.inv(A)
print("\n Inverse of Matrix A is: \n {}".format(A_inv))

#Computing the solution vector x using the Gauss-Jordan method
x = np.dot(A_inv, B)

# Printing the solution vector
print("\n Solution vector: \n")
print(x)
#Solution_X = 1;3;5
