import numpy as np
import numpy.linalg as la

# @ operator for numpy arrays
A @ B = np.dot(A,B)
X = la.solve(A.T @ A, A.T @ b)

# print is a function
print(A)

# range(0,100) is no longer a list

