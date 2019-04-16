import matplotlib.pyplot as plt
import numpy as np
from math import pi

plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rc('text',usetex=True)
plt.rc('font',family='times new roman',size=14)


N=100
xs=np.linspace(0,2*pi,N)
ys=np.exp(-1*xs)

plt.plot(xs,ys,color="black",linestyle="-.")
plt.title("Demonstrating Latex Annotations",fontsize=16)
plt.xlabel(r"$x$")
plt.ylabel(r"$e^{-x}$")
plt.grid()