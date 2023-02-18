import numpy as np
from sympy import Matrix
from sympy import *

#5.Solve a System of Homogeneous Equations Using The Gauss Jordan method:
def gauss_jordan(A):
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
        # Normalize the current row
        A[i, :] = A[i, :] / A[i, i]
        # Eliminate all elements above and below the pivot element
        for k in range(n):
            if k != i:
                c = A[k, i]
                A[k, :] = A[k, :] - c * A[i, :]
    return A

print("\n GAUSS JORDAN OF THE MATRIX\n")

# Example Homogeneous Equation:
A = np.array([[1, 2, 3], [4, 5, 2], [5, 7, 0]])
print("Given matrix: ", A)
A = gauss_jordan(A)
print("\n Reduced row-echelon form of The Given Matrix is:\n",A)
