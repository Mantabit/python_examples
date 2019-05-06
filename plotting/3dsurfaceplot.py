'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import colors,cm
from math import pi

# Generate torus mesh
N=50
phis=np.linspace(0,2*pi,N)
thetas=np.linspace(0,pi,N)
THETA,PHI=np.meshgrid(thetas,phis)
r, R = .25, 1.
X = np.sin(THETA)*np.cos(PHI)
Y = np.sin(THETA)*np.sin(PHI)
Z = np.cos(THETA)

colorfunction=(X**2+Y**2)
norm=colors.Normalize(colorfunction.min(),colorfunction.max())

# Display the mesh
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
mapble=ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, facecolors=cm.jet(norm(colorfunction)),cmap="jet")
plt.show()