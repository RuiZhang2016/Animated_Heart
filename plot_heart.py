# This program creates an animated heart
# Author: Rui Zhang
# Date: 2018/08/12

import matplotlib
matplotlib.use("TkAgg")
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot as plt
import numpy as np
from skimage import measure

def set_up_mesh():
    n = 100
    x = np.linspace(-3,3,n)
    y = np.linspace(-3,3,n)
    z = np.linspace(-3,3,n)
    X, Y, Z =  np.meshgrid(x, y, z)
    return X, Y, Z

# Create cardioid function
def f_heart(x,y,z):
    F = 320 * ((-x**2 * z**3 -9*y**2 * z**3/80) +
               (x**2 + 9*y**2/4 + z**2-1)**3)
    return F

# Obtain value to at every point in mesh
X, Y, Z = set_up_mesh()
vol = f_heart(X,Y,Z)

# Extract a 2D surface mesh from a 3D volume (F=0)
verts, faces ,_ ,_ = measure.marching_cubes_lewiner(vol, 0, spacing=(0.1, 0.1, 0.1))

# Create a 3D figure
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_trisurf(verts[:, 0], verts[:,1], faces, verts[:, 2],
                cmap='Spectral', lw=1)

# Change the angle of view to make an animation
ax.set_title(u"Made with ❤ (show my love)", fontsize=15)
for angle in range(0, 360*10):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)
    if not plt.fignum_exists(fig.number):
        break

