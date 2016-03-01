  import numpy as np
  #B[[i,j]] = B[[j,i]] # swaps row i with row j
  A  = np.array([[1,2,3],[4,5,6],[7,8,9]])
  A[[0, 1]] = A[[1,0]]
  
