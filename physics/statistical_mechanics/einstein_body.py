from pyncomb.combfuncs import binom
import matplotlib.pyplot as plt
from math import log

'''
NA:         # of harmonic oscillators in body A
Nb:         # of harmonic oscillators in body B
q:          total energy in the system q=qA+qB
qA:         energy in body A
qB:         energy in body B

This script computes the number of microstates in a given macrostate qA
For large values of N and q, the multiplicity function Omega(qA) has a very sharp peak
making deviations from the maximum value very unlikely
'''

Na=1000  #number of oscillators in first solid body
Nb=1500  #number of oscillators in second solid body
q=800   #total energy in both bodies

def omega_body_a(qa):
    return binom(qa+Na-1,qa)
    
def omega_body_b(qb):
    return binom(qb+Nb-1,qb)

omega_totals=[]    
for i in range(0,q+1):
    omega_totals.append(log(omega_body_a(i)*omega_body_a(q-i)))
    
plt.plot(omega_totals)
plt.ylim([max(omega_totals)-3,max(omega_totals)])
plt.grid()
plt.xlabel("q_A: Total energy in the first solid body")
plt.ylabel("# microstates in macrostate q_A")
plt.title("# microstates Omega as a function of macrostate qA (energy of solid body A)")