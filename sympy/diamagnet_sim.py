from sympy.vector import CoordSys3D, divergence,gradient,Del
from sympy import diff,sqrt,lambdify
from sympy.abc import x,y,z
import numpy as np
import matplotlib.pyplot as plt

"""
Definitions
"""

R=CoordSys3D("R")
#positional vector of base coordinate system
r=R.x*R.i+R.y*R.j+R.z*R.k
#magnetizability coefficient
alpha=-0.1

def toUnit(vec):
    return vec/(sqrt(vec.dot(vec)))

def lambdifyVector(symvec):
    symvec=symvec.subs([(R.x,x),(R.y,y),(R.z,z)])
    x_lam=lambdify((x,y,z),symvec.dot(R.i))
    y_lam=lambdify((x,y,z),symvec.dot(R.j))
    z_lam=lambdify((x,y,z),symvec.dot(R.k))
    return lambda rr:np.array([x_lam(rr[0],rr[1],rr[2]),y_lam(rr[0],rr[1],rr[2]),z_lam(rr[0],rr[1],rr[2])])

"""
Symbolic Computations
"""

#position of dipole 0
###d_0=-R.i-R.j-R.k
d_0=-1*R.k
#dipole moment of dipole 1
###p_0=R.i+R.k
p_0=R.k
#positional vector from coordinate system of dipole 0
r_0=r-d_0
r_0_u=toUnit(r_0)
#magnetic field of dipole 0
B=(3*p_0.dot(r_0_u)*r_0_u-p_0)/(sqrt(r_0.dot(r_0))**3)
B_num=lambdifyVector(B)
#force on a magnetic particle
delop=Del()
F=-alpha*delop.gradient(-B.dot(B),doit=True)
F_num=lambdifyVector(F)

[X,Z]=np.meshgrid(np.linspace(-5,5,20),np.linspace(3,10,20))
Bu,Bv=np.zeros(X.shape),np.zeros(X.shape)
Fu,Fv=np.zeros(X.shape),np.zeros(X.shape)

for i in range(0,X.shape[0]):
    for j in range(0,X.shape[1]):
        field=B_num([X[i,j],0,Z[i,j]])
        force=F_num([X[i,j],0,Z[i,j]])
        Bu[i,j],Bv[i,j]=field[0],field[2]
        Fu[i,j],Fv[i,j]=force[0],force[2]


"""
Plotting & Visualizing Fields
"""
#scale the magnitude of vectors logarithmically
scaleLog=True
if scaleLog:
    Bmag=np.sqrt(Bu**2+Bv**2)
    Bu=Bu/(Bmag)*np.log10(10*Bmag/Bmag.min())
    Bv=Bv/(Bmag)*np.log10(10*Bmag/Bmag.min())
    Fmag=np.sqrt(Fu**2+Fv**2)
    Fu=Fu/(Fmag)*np.log10(10*Fmag/Fmag.min())
    Fv=Fv/(Fmag)*np.log10(10*Fmag/Fmag.min())
#plot regular field
plt.subplot(211)
plt.quiver(X,Z,Bu,Bv,color="blue")
plt.title("$\mathbf{B}(\mathbf{r})$")
plt.xlabel("x")
plt.ylabel("z")
plt.subplot(212)
plt.quiver(X,Z,Fu,Fv,color="orange")
plt.title("$\mathbf{F}(\mathbf{r})$")
plt.xlabel("x")
plt.ylabel("z")
plt.gcf().set_size_inches((8,12))

#plot normalized field        
#plt.quiver(X,Y,U/(np.sqrt(U**2+V**2)),V/(np.sqrt(U**2+V**2)))