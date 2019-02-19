import sympy as sym
from sympy import *

#define spatial coordinates
x,y,z,kp,Ti,s,Ts=sym.symbols("x y z k_p T_i s T_s")
coords=[x,y,z]

init_printing()

T_s=kp*(1+1/(s*Ts))
tustin=2/Ti*((1-z)/(1+z))

T_d=T_s.subs(s,tustin)
(num,den)=fraction(T_d.simplify())

num=collect(num.expand(),z)
den=collect(den.expand(),z)
numpoly=Poly(num,z)
numcoeffs=numpoly.coeffs()
denpoly=Poly(den,z)
dencoeffs=denpoly.coeffs()