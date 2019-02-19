from symutils import C,lambdifyVector,lambdifyVectorTime,norm,nablaVec,tensMul,r,C
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import numpy as np
from sympy.vector import Del
from sympy import init_printing, simplify, symbols, sin, cos, pi
from sympy.abc import x,y,z,t
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#initializations
#################################################
#initialize printing
init_printing()
#define some symbols
m1,m2,m3=symbols("m_1 m_2 m_3")
B1,B2,B3=symbols("B_1 B_2 B_3")
m=m1*C.i+m2*C.j+m3*C.k
B=B1*C.i+B2*C.j+B3*C.k
#nabla operator
nabla=Del()
#location vector
r=C.x*C.i+C.y*C.j+C.z*C.k
#################################################

#directional derivative
B_test=C.x*C.y*C.i+C.x**2*C.i+C.z**2*C.y*C.j
dirder_B=(m.dot(nabla))(B_test)