from sympy import diff
from sympy.abc import x,y,z

coords=[x,y,z]

def nabla(u):
    if len(u)==1:
        return [diff(u,coord) for coord in coords]
    if len(u)==3:
        return [[diff(comp,coord) for coord in coords] for comp in u]
    
def dot(u,v):
    if len(u)==3 and len(v)==3:
        return u(0)*v(0)+u(1)*v(1)+u(2)*v(2)
#    if len(u)==9 and len(v)==3:
#        return []