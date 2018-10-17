from matplotlib import pyplot as plt
import numpy as np

#make a scatter plot and annotate each point

N=10
randmat=np.random.rand(2,10)

plt.figure(1)
plt.scatter(randmat[0,:],randmat[1,:],marker="x")
plt.grid()
for i in range(0,N):
    plt.text(randmat[0,i],randmat[1,i],"("+"%.2f"%randmat[0,i]+","+"%.2f"%randmat[1,i]+")")
    
#plot a random matrix and its entries on a color map
randmat=np.random.rand(10,10)
fig=plt.figure(2)
fig.set_size_inches(w=8,h=8)
plt.imshow(randmat)
for i in range(0,N):
    for j in range(0,N):
        plt.text(j-0.25,N-1-i+0.1,"%.2f"%randmat[i,j])
plt.colorbar()



#create a subplot

plt.figure(2)
x=np.linspace(-5,5,100)
y1=np.square(x)
y2=np.sinc(x)

plt.subplot(2,1,1)
plt.plot(x,y1,"-")
plt.grid()
plt.ylabel("$y_{1}$")

plt.subplot(2,1,2)
plt.plot(x,y2,"-")
plt.grid()
plt.xlabel("$x$")
plt.ylabel("$y_{2}$")