#this file illustrates basic plotting functionalities using matplotlib

import numpy as np
from matplotlib import pyplot as plt


#plot the graph of f(x)=x² and set the axes ticks
x_data=np.linspace(0,2*np.pi,100)
y_data=np.square(x_data)

fig=plt.figure()
axes=fig.gca()
axes.set_xticks(np.linspace(0,2*np.pi,10))
axes.set_yticks(np.linspace(0,(2*np.pi)**2,10))
axes.set_xlabel("x value")
axes.set_ylabel("y=f(x) value")
plt.plot(x_data,y_data)
plt.grid()
plt.show()

#plot a histogram of values
values=np.random.rand(100)
fig=plt.figure()
plt.hist(values,np.linspace(0,1,6))
axes=fig.gca()
axes.set_xlabel("value range")
axes.set_ylabel("# of occurences")
axes.set_title("test of a histogram")
plt.grid()