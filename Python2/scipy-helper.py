
#broadcasting scalars, so need to supply shape
D = scipy.sparse.diags([-1/(2*h),0,1/(2*h)], [-1,0,1], shape=(n,n))

  #Scipy special library 

    #grab our weights and nodes
    ell = sps.legendre(n).weights
    nodes = ell[:,0]
    weights = ell[:,1]
