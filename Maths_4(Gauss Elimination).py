import numpy as np

print("-----GAUSS ELIMINATION METHOD-----")

A = np.matrix(input("Write elements separated by spaces and separate rows with semi-colon: \n"))
print("Matrix 1 is: \n", A)

B = np.matrix(input("\n Write elements separated by spaces and separate rows with semi-colon: \n"))
print("Matrix 2 is: \n", B)  
  
# Applying Gauss Elimination

# Solve the system of linear equations using Gaussian elimination method in NumPy
x = np.linalg.solve(A, B)

# Print the solution vector
print("\n Solution vector: \n")
print(x)

