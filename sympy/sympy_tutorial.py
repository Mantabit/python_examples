import sympy as sym
from sympy import *

#define spatial coordinates
x,y,z=sym.symbols("x y z")
coords=[x,y,z]

#compute laplacian of scalar or vector
def laplace(a):
    return diff(a,x,2)+diff(a,y,2)+diff(a,z,2)

#compute gradient of vector
def grad_vec(a):
    mat=[[0 for i in range(0,3)] for j in range(0,3)]
    for i in range(0,3):
        for j in range(0,3):
            mat[i][j]=diff(a[i],coords[j])
    mat=Matrix(mat)
    return mat

#compute the inner product of two matrices
def inner_mat(A,B):
    res=0
    for i in range(0,3):
        for j in range(0,3):
            res=res+A[i,j]*B[i,j]
    return Matrix([res])

#compute the divergence of a vector
def div(a):
    res=0
    for i in range(0,3):
        res=res+diff(a[i],coords[i])
    return Matrix([res])
    
u=[sym.Function("u"+str(i))(x,y,z) for i in range(1,4)]
v=[sym.Function("v"+str(i))(x,y,z) for i in range(1,4)]

u=sym.Matrix([u[0],u[1],u[2]])
v=sym.Matrix([v[0],v[1],v[2]])

rhs=laplace(u).T*v+inner_mat(grad_vec(u),grad_vec(v))
lhs=div(grad_vec(u)*v)

#substitutions
expr=x+y*sin(x)
expr=expr.subs([(x,1),(y,1)])