import matplotlib.pyplot as plt
from numpy.random import rand

xs=rand(100,1)

plt.hist(xs,bins=10)
plt.grid()

plt.title("A Histogram")
plt.xlabel("# Occurences")
plt.ylabel("Value of x")
ax=plt.gca()
#normal annotation
ax.annotate("An annotation",
            xy=(0.5, 5), xycoords='data',
            xytext=(0.7, 1), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
#annotation with a curved arrow
ax.annotate("An annotation (curved)",
            xy=(0.1, 8), xycoords='data',
            xytext=(0.1, 5), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=0.2"),
            )
            
#insert some text
plt.text(0.3,0.75,r"$e^{jx}=\sum_{k=0}^{\infty}\frac{(jx)^k}{k!}$")