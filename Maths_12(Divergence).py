import numpy as np
import sympy
#12.>Compute Divergence of a vector field

print("\n DIVERGENCE  OF THE MATRIX\n")

def divergence(F):
    # Computing the partial derivatives of the vector field components
    dPdx = sympy.diff(F[0], x)
    dQdy = sympy.diff(F[1], y)
    dRdz = sympy.diff(F[2], z)
    
    #Computing the divergence of the vector field
    divF = dPdx + dQdy + dRdz
    return divF
x, y, z = sympy.symbols('x y z')
F = sympy.Matrix([(x**2)*z, (-2)*(y**3)*(z**2), x*(y**2)*z])

# Computing the divergence of F
divF = divergence(F)

print("The divergence of the vector field {} is: \n".format(F))
print(divF.simplify())
