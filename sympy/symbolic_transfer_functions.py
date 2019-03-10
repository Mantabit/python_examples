import sympy as sym
from sympy import *

#define spatial coordinates
x,y,z,kp,Ti,s,Ts=sym.symbols("x y z k_p T_i s T_s")
coords=[x,y,z]

init_printing()

#define the transfer function in continuous time
T_s=kp*(1+1/(s*Ts))
tustin=2/Ti*((1-z)/(1+z))

#compute the symbolic transfer function in disccrete time using tustin approximation
T_d=T_s.subs(s,tustin)
(num,den)=fraction(T_d.simplify())

#collect the powers in the numerator and denominator
num=collect(num.expand(),z)
den=collect(den.expand(),z)
#define polynomials to get the coefficient arrays
#use these arrays to implement a discrete version of the controller
numpoly=Poly(num,z)
numcoeffs=numpoly.coeffs()
denpoly=Poly(den,z)
dencoeffs=denpoly.coeffs()