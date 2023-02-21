import numpy as np

print("\n -----GAUSS ELIMINATION METHOD-----\n")

A = np.matrix(input("Write elements separated by spaces and separate rows with semi-colon: \n"))
print("Matrix 1 is: \n", A)
#Example_A = 1 1 1;2 -3 4;3 4 5

B = np.matrix(input("\n Write elements separated by semi-colon: \n"))
print("Matrix 2 is: \n", B)  
#Example_B = 9;13;40

# Applying Gauss Elimination

# Solve the system of linear equations using Gaussian elimination method in NumPy
x = np.linalg.solve(A, B)
#Augmented_A:B = 1 1 1 9;2 -3 4 13;3 4 5 40

# Print the solution vector
print("\n Solution vector: \n")
print(x)
#Solution_X = 1;3;5

