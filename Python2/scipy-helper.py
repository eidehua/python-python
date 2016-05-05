
#broadcasting scalars, so need to supply shape
D = scipy.sparse.diags([-1/(2*h),0,1/(2*h)], [-1,0,1], shape=(n,n))
