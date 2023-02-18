import numpy as np
from sympy import Matrix
from sympy import *

#4.Solve a system of Homogeneous and non-homogeneous equations using Gauss elimination method.
def gauss_elimination(A, b):
    n = A.shape[0]
    for i in range(n):
        # Find the pivot element
        max_element = np.abs(A[i, i])
        max_row = i
        for k in range(i + 1, n):
            if np.abs(A[k, i]) > max_element:
                max_element = np.abs(A[k, i])
                max_row = k
        # Swap the current row with the pivot row
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        # Eliminate all elements below the pivot element
        for k in range(i + 1, n):
            c = -A[k, i] / A[i, i]
            A[k, i:] = A[k, i:] + c * A[i, i:]
            b[k] = b[k] + c * b[i]
    # Back-substitution to find the solution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x

print("\n GAUSS ELIMINATION OF THE MATRIX\n")

# Example system of equations for a Homogeneous case
A = np.array([[1, 2, 6], [0, 1, 4], [5, 6, 0]])
b = np.array([2, 2, 4])
x = gauss_elimination(A, b)
print("Homogeneous solution of given Equations is:")
print(x)

# Example System of Equations For a Non-Homogeneous Case
A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
b = np.array([2, 7, -20])
x = gauss_elimination(A, b)
print("\n Non-homogeneous solution of given Equations is:")
print(x)
