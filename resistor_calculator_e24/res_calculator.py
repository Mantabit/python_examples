# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:18:14 2020

This scipts computes the closest value actR to desR of the form

actR = 10^[(j/24)+i]    where j in [0..23] and i in N

@author: dvarx
"""

from math import log10,floor

n=2
desR=58375

actRs=[]

current_desR=desR
for k in range(1,n+1):
    i=floor(log10(current_desR))
    desR_norm=current_desR/(10**i)
    j=floor(24*log10(desR_norm))
    actR=10**(j/24+i)
    actRs.append(actR)
    current_desR=current_desR-actR

actR=0
for k in range(1,n+1):
    actR+=actRs[k-1]

print("Resistance Values to be used:")
for r in actRs:
    print("%f"%(r))
print("\n%-40s%f\n%-40s%f\n%-40s%f%%"%("Desired Resistance desR:",desR,"Actual Resistance actR:",actR,"Relative Error:",100*(actR-desR)/desR))