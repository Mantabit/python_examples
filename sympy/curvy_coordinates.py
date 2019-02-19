from symutils import C,lambdifyVector,norm,nablaVec,tensMul,nabla
from sympy.vector import CoordSys3D, express
from sympy import cos,sin,symbols
import sympy as sym

'''
This script illustrates the usage of curvy coordinate systems in sympy
'''

'''
Define a spherical coordinate system
The unit vector are denoted as (S.i,S.j,S.k) (e.g. e_phi, e_rho, e_r)
'''
S=C.create_new("S",transformation="spherical")
r,theta,phi,er,etheta,ephi=symbols(r"r,\vartheta,\varphi,\vec{e}_r,\vec{e}_{\vartheta},\vec{e}_{\varphi}")

def print_spherical(vec):
    return vec.subs([(S.r,r),(S.theta,theta),(S.phi,phi)])