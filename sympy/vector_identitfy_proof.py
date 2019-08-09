from sympy import Matrix,det,symbols,simplify
from sympy.abc import a,b,c,d,e,f

"""
This script is used to proove vector identities
"""

#generate symbols for matrix entries and vector entries
u,v,A=[],[],[]
for i in range(1,4):
    v.append(symbols("u%d"%i))
    u.append(symbols("v%d"%i))
u,v=Matrix(u),Matrix(v)
for i in range(1,4):
    row=[]
    for j in range(1,4):
        row.append(symbols("A%d%d"%(i,j)))
    A.append(row)
A=Matrix(A)

#we want to reject that A*(uxv)=(A*u)xv
    
lhs=(A*u).cross(v)
rhs=A*(u.cross(v))

diff=simplify(rhs-lhs)