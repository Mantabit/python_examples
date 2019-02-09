from symutils import C,lambdifyVector,norm
import numpy as np
from sympy.vector import Del
from sympy import init_printing, simplify, symbols
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

'''
This file plots the field of a magnetic dipole in a two and three dimensional coordinate system
'''

#initializations
#################################################
#initialize printing
init_printing()
#define some symbols
m1,m2,m3=symbols("m_1 m_2 m_3")
m=m1*C.i+m2*C.j+m3*C.k
#nabla operator
nabla=Del()
#location vector
r=C.x*C.i+C.y*C.j+C.z*C.k
#################################################

B=m.dot(r)*3*r/(norm(r)**5)-m/(norm(r)**3)
B=B.subs([(m1,0),(m2,0),(m3,1)])
B_dir=simplify(B/norm(B))
B_dir_lam=lambdifyVector(B_dir)
B_lam=lambdifyVector(B)

xs,ys,zs,Bxs,Bys,Bzs=[],[],[],[],[],[]
#grid=np.linspace(-5,5,5)
#for px in grid:
#    for py in grid:
#        for pz in grid:
#            xs.append(px)
#            ys.append(py)
#            zs.append(pz)
#            Bc=B_dir_lam(px,py,pz)
#            Bxs.append(Bc[0])
#            Bys.append(Bc[1])
#            Bzs.append(Bc[2])
            
grid=np.linspace(-10,10,20)
for pz in grid:
    for py in grid:
        ys.append(py)
        zs.append(pz)
        Bc=B_dir_lam(0,py,pz)
        Bys.append(Bc[1])
        Bzs.append(Bc[2])
            
fig=plt.figure()
#ax=Axes3D(fig)
#ax.quiver(xs,ys,zs,Bxs,Bys,Bzs,length=0.5)
plt.quiver(ys,zs,Bys,Bzs)