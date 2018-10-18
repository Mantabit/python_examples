from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

N=10
tstart=0
tend=0.1
nt=100
y0=[i for i in range(0,N)]
k=[1 for i in range(0,N)]

t=np.linspace(tstart,tend,nt)

def derY(y,t):
    n=len(y)
    dery=[np.array(np.array(y)).sum()*k[i]*y[i] for i in range(0,n)]
    return dery
    
y=odeint(derY,y0,t)

plt.plot(t,y)
plt.grid()