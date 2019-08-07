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

#positions of the 4 dipoles
ds=[-R.k+R.i,-R.k+R.j,-R.k-R.i,-R.k-R.j]
#dipole moment of dipole 1
ps=[R.k-R.i,R.k-R.j,R.k+R.i,R.k+R.j]
#positional vectors for dipole centric coordinate systems and corresponding unit vectors
r0s=[r-d for d in ds]
r0us=[r0/(sqrt(r0.dot(r0))) for r0 in r0s]
#magnetic fields of the dipoles
B=[(3*ps[k].dot(r0us[k])*r0us[k]-ps[k])/(sqrt(r0s[k].dot(r0s[k]))**3) for k in range(0,4)]
B=B[0]+B[1]+B[2]+B[3]
B_num=lambdifyVector(B)
#force on a magnetic particle
delop=Del()
F=-alpha*delop.gradient(-B.dot(B),doit=True)
F_num=lambdifyVector(F)

#[X,Z]=np.meshgrid(np.linspace(-2,2,20),np.linspace(3,10,20))
[X,Y]=np.meshgrid(np.linspace(-2,2,40),np.linspace(-2,2,40))
Bu,Bv=np.zeros(X.shape),np.zeros(X.shape)
Fu,Fv=np.zeros(X.shape),np.zeros(X.shape)

for i in range(0,X.shape[0]):
    for j in range(0,X.shape[1]):
        """
        field=B_num([X[i,j],0,Z[i,j]])
        force=F_num([X[i,j],0,Z[i,j]])
        Bu[i,j],Bv[i,j]=field[0],field[2]
        Fu[i,j],Fv[i,j]=force[0],force[2]
        """
        field=B_num([X[i,j],Y[i,j],0])
        force=F_num([X[i,j],Y[i,j],0])
        Bu[i,j],Bv[i,j]=field[0],field[1]
        Fu[i,j],Fv[i,j]=force[0],force[1]

"""
Plotting & Visualizing Fields
"""
#scale the magnitude of vectors logarithmically
scaleLog=False
if scaleLog:
    Bmag=np.sqrt(Bu**2+Bv**2)
    Bu=Bu/(Bmag)*np.log10(10*Bmag/Bmag.min())
    Bv=Bv/(Bmag)*np.log10(10*Bmag/Bmag.min())
    Fmag=np.sqrt(Fu**2+Fv**2)
    Fu=Fu/(Fmag)*np.log10(10*Fmag/Fmag.min())
    Fv=Fv/(Fmag)*np.log10(10*Fmag/Fmag.min())
#plot regular field
plt.subplot(211)
plt.quiver(X,Y,Bu,Bv,color="blue")
plt.title("$\mathbf{B}(\mathbf{r})$")
plt.xlabel("x")
plt.ylabel("z")
plt.subplot(212)
plt.quiver(X,Y,Fu,Fv,color="orange")
plt.title("$\mathbf{F}(\mathbf{r})$")
plt.xlabel("x")
plt.ylabel("z")
plt.gcf().set_size_inches((8,12))

#plot normalized field        
#plt.quiver(X,Y,U/(np.sqrt(U**2+V**2)),V/(np.sqrt(U**2+V**2)))