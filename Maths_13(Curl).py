import numpy as np
from sympy import Matrix
from sympy import *

#13.>Compute Curl of a vector field.
 
print("\n CURL OF THE VECTOR FIELD\n")

# Define the vector field as a NumPy array
# For example, the vector field F = (y^2*z, x*z^2, x*y^2)
def F(x, y, z):
    return np.array([y**2*z, x*z**2, x*y**2])

# Define the curl of the vector field as a function of x, y, z
# The curl is given by the cross product of the gradient with the vector field
def curl_F(x, y, z):
    curl_x = (F(x + 0.01, y, z)[2] - F(x - 0.01, y, z)[2] - F(x, y + 0.01, z)[1] + F(x, y - 0.01, z)[1]) / 0.02
    curl_y = (F(x, y + 0.01, z)[0] - F(x, y - 0.01, z)[0] - F(x, y, z + 0.01)[2] + F(x, y, z - 0.01)[2]) / 0.02
    curl_z = (F(x, y, z + 0.01)[1] - F(x, y, z - 0.01)[1] - F(x + 0.01, y, z)[0] + F(x - 0.01, y, z)[0]) / 0.02
    return np.array([curl_x, curl_y, curl_z])

# Test the function with an example
x, y, z = 1, 2, 3
print("The curl of F at ({},{},{}) is: {}".format(x, y, z, curl_F(x, y, z)))
