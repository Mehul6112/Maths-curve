import numpy as np
import math
mat1 = np.matrix(input("Write elements separated by spaces and separate rows with semi-colon: "))
print("Matrix 1 is: ", "\n", mat1)
mat2 = np.matrix(input("Write elements separated by spaces and separate rows with semi-colon: "))
print("Matrix 2 is: ", "\n", mat2)    
print("Transpose of Matrix 1 is: ", "\n", mat1.T)
print("Transpose of Matrix 2 is: ", "\n", mat2.T)
mat3 = mat1 * mat2
print("Product of Matrix 1 & Maatrix 2 is: ", "\n", mat3)
