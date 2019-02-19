from symutils import C,lambdifyVector,lambdifyVectorTime,norm,nablaVec,tensMul,r,C
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import numpy as np
from sympy.vector import Del
from sympy import init_printing, simplify, symbols, sin, cos, pi
from sympy.abc import x,y,z,t
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

'''
This script computes and simulated the force exerted by a constant dipole on a spinning dipole
located at a distance d
'''

#############################
#SYMBOLIC COMPUTATIONS
#############################

#rotational speed and distance
w,d=symbols("w,d")
r=r-d*C.j
#magneti dipole moment of permanent magnet
mp1,mp2,mp3=symbols("m_p1 m_p2 m_p3")
mp=mp1*C.i+mp2*C.j+mp3*C.k
#magnetic dipole moment of spinning magnet
m=symbols("m")
ms=m*(C.j*cos(w*t)+C.k*sin(w*t))

#compute B and nabla_B using sympy
B=mp.dot(r)*3*r/(norm(r)**5)-mp/(norm(r)**3)
nabla_B=nablaVec(B)
F=tensMul(nabla_B,ms).simplify()
F_subs=F.subs([(m,1),(mp1,0),(mp2,0),(mp3,0.01),(w,2*0*pi),(d,1)])

F_subs_lam=lambdifyVectorTime(F_subs)

#############################
#NUMERICAL SIMULATION
#############################

pos0=[0,0,0]
ts=np.linspace(0,1,100)
sol=odeint(F_subs_lam,pos0,ts)
plt.subplot(1,2,2)

labels=["Rx","Ry","Rz"]
styles=["-","--",":"]
for i in range(0,3):
    plt.plot(ts,sol[:,i],label=labels[i],linestyle=styles[i],color="blue")
plt.legend()
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Position [m]")