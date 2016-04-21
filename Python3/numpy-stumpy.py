V = np.ones((rows_monte, 2))
V[:,1] = np.log(h_monte) #second column = log(h)
b = np.log(monte_carlo_filtered_errors) #b = log(error(h))
#linear least squares
monte_EOC = la.solve(V.T @ V, V.T @ b)
