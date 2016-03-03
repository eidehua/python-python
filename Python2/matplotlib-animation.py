import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt
from matplotlib import animation

W = np.array([ [1,2,3],[1,2,3]]) # some 2d array, sparse
height = 1
width = 1 # less than W
_, evects = la.eigh(W)
fig = pt.figure()
v = evects[:,0]
plot_array = np.zeros((height, width))
plot_array[is_in_domain] = 1/(1e-2+np.abs(v))
im = pt.imshow(plot_array, cmap="gray", animated=True)

def update_eig_plot(i):
    v = evects[:, i]
    print("t")
    if nvariables != v.shape[0]:
        print ("Fail to plot: shape of vector not correct.")
        return im

    plot_array = np.zeros((height, width))
    plot_array[is_in_domain] = 1/(1e-2+np.abs(v))
    im.set_array(plot_array)
    return im,
    #pt.imshow(plot_array, cmap="gray")

anim = animation.FuncAnimation(fig, update_eig_plot,frames=200, interval=20, blit=True)
