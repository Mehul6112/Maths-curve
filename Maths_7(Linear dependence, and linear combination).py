import numpy as np

def check_linear_dependence(vectors):
    # Create a matrix from the vectors
    matrix = np.array(vectors).T
    
    rank = np.linalg.matrix_rank(matrix)
    # Check if the columns are linearly dependent
    if rank < matrix.shape[1]:
        print("The columns of the matrix are linearly dependent.\n")
    else:
        print("The columns of the matrix are linearly independent.\n")

# Example usage
vectors = [[1, 2, 3], [2, 4, 6], [3, 5, 7]]
check_linear_dependence(vectors)  # The vectors are linearly dependent.

vectors = [[1, 2, 3]]
check_linear_dependence(vectors)  # The vectors are linearly independent.

# define the vectors as numpy arrays
v1 = np.array([[1, 2, 3], [2, -4, -9], [5, 9, -7]])
v2 = np.array([[4, 5, 6], [1, 4, 6], [-9, -1, 0]])

# define the coefficients
a = int(input("Enter a coefficient for v1: "))
b = int(input("Enter another coefficient for v2: "))

# calculate the linear combination
linear_combination = a*v1 + b*v2

print("Linear combination of ({} \n and \n {}) is: \n \n".format(v1, v2), linear_combination)