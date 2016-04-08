import numpy as np
#B[[i,j]] = B[[j,i]] # swaps row i with row 
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

A = np.random.randn(2, 2)
v = np.random.randn(n)

#testing numpy's dimensionality with arithmetic)
C = np.array([2,3])
D = C - 5
print C
print D

#numpy elementwise flexibility
plot_image_freq = np.abs(plot_image_freq) #element absolute value
plot_image_freq = plot_image_freq + 1.0e-12 #elementwise scalar addition

#column/row wise
jac = np.zeros((5,5))
first_row = np.array([1,2,3,4,5])
jac[:,0] = first_row

#allocating to sub-matrix
DFT = np.array([[ 1,2,3,4],
               [ 5,6,7,8],
               [ 9,10,11,12]])
small =DFT[0:2,0:3] #2 x 3-> rows 0,1 & cols 0,1,2
zeroes = np.zeros((5,5))
print(zeroes)
zeroes[0:2,0:3] = small
print(zeroes)
