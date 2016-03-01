import numpy as np
#B[[i,j]] = B[[j,i]] # swaps row i with row j
A  = np.array([[1,2,3],[4,5,6],[7,8,9]])
A[[0, 1]] = A[[1,0]]

# Backward substitution Ux = y
U = A.copy()
x = np.array([1,3,2])
y = np.array([10,32,2])
for j in range(U.shape[1]-1, -1, -1):
  if U[j,j] == 0: # stop if singular
    break
  x[j] = y[j]/U[j,j]
  for i in range(0, j):
    y[i] = y[i] - U[i,j]*x[j]
