import numpy as np
#8. Finding the orthonormal basis of a given vector space using
#Gram-Schmidt Orthogonalization process.


#Declaring sub-spaces:
v1 = [1,1,1,1]
print("Sub-space v1 is: ", v1)
v2 = [1,1,-1,-1]
print("Sub-space v2 is: ", v2)
v3 = [0,-1,2,1]
print("Sub-space v3 is: ", v3, "\n")

#Declaring Vector-space:
v = np.array([v1,v2,v3])
print("Vector-space V is: \n", v, "\n")

#Converting sub-spaces to their orthonormal form:
u1 = v1/np.linalg.norm(v1)
print("Orthonormal sub-space of v1 is: ", u1)

e2 = v2 - np.dot(np.dot(u1,v2),u1)
u2 = e2/np.linalg.norm(e2)
print("Orthonormal sub-space of v2 is: ", u2)

e3 = v3 - (np.dot(np.dot(u1,v3),u1) + np.dot(np.dot(u2,v3),u2))
u3 = e3/np.linalg.norm(e3)
print("Orthonormal sub-space of v3 is: ", u3, "\n")

#Testing for orthonormality: Dot product of any 2 vetor 
#should be zero and they should be unit vector. 
print("Testing if the generated vectors are orthonormal: \n")
test1 = np.dot(u1,u2)
print("Dot product of u1 & u2 is {} and norm of u is {}".format(test1, np.linalg.norm(u1)))
test2 = np.dot(u1,u3)
print("Dot product of u1 & u3 is {} and norm of u is {}".format(test2, np.linalg.norm(u2)))
test3 = np.dot(u2,u3)
print("Dot product of u2 & u3 is {} and norm of u is {}".format(test3, np.linalg.norm(u3)), "\n")

#Finally, outputing the generated Orthonormal Vector-space:
u = np.array([u1,u2,u3])
print("Orthonormalised Vector-space V is: \n", u)
