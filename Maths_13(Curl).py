import sympy as sp
print("\n CURL OF THE MATRIX\n")

# Define the symbols
x, y, z = sp.symbols('x y z')

# Define the vector field
A = sp.Matrix([x*z**3, -2*x**2*y*z, 2*y*z**4])

# Compute the curl of the vector field
curl_A = sp.Matrix([sp.diff(A[2], y) - sp.diff(A[1], z),
                    sp.diff(A[0], z) - sp.diff(A[2], x),
                    sp.diff(A[1], x) - sp.diff(A[0], y)])

curl_A.simplify()
print("The curl of the vector field {} is: \n".format(A))
print(curl_A)
