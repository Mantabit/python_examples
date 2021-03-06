import numpy as np
import matplotlib.pyplot as plt
import time
from math import log2
from quicksort_partition import partition

N=20
numbers=np.random.rand(2**N)

"""
This function implements the merge sort algorithm
"""
def mergeSort(array,i,N):
    if(N==1):
        return
    #divide the subarray into two smaller sub arrays and sort them
    mergeSort(array,i,N/2)
    mergeSort(array,i+N/2,N/2)
    #combine the two sorted subarrays
    sortedarr=[]
    ind1,ind2=0,0
    while(ind1<N/2 and ind2<N/2):
        if(array[int(i+ind1)]>array[int(i+N/2+ind2)]):
            sortedarr.append(array[int(i+ind1)])
            ind1+=1
        else:
            sortedarr.append(array[int(i+N/2+ind2)])
            ind2+=1
    if(ind1==N/2):
        while(ind2<N/2):
            sortedarr.append(array[int(i+N/2+ind2)])
            ind2+=1
    else:
        while(ind1<N/2):
            sortedarr.append(array[int(i+ind1)])
            ind1+=1
    array[int(i):int(i+N)]=np.array(sortedarr)

"""
This function implements the quicksort algorithm
"""
def quickSort(arr,lo,hi):
    #partition the array in two subarrays whose elements are smaller or larger than the pivot arr[hi]
    #i is the separation index which divided the two subarrays
    if(hi<=lo):
        return
    partIndex=partition(arr,lo,hi)
#    print((hi,lo,partIndex))
#    print(arr)
#    time.sleep(0.4)
    quickSort(arr,lo,partIndex-1)
    quickSort(arr,partIndex+1,hi)
     
"""
Plot an analyze the run time of a certain algorithm
"""

#choose the sorting algorithm to analyse
sortingAlgo=lambda arr : quickSort(arr,0,len(arr)-1)
#sortingAlgo=lambda arr : mergeSort(arr,0,len(arr))

ns=[2**i for i in range(10+1,20+1)]
times=[]
for n in ns:
    numbers=np.random.rand(n)
    start=time.time()
    sortingAlgo(numbers)
    stop=time.time()
    times.append(stop-start)

#double logarithmic plot
xs=[log2(n) for n in ns]
ys=[log2(time) for time in times]
coeffs=np.polyfit(xs,ys,1)
ysfitted=[coeffs[1]+coeffs[0]*x for x in xs]
plt.plot(xs,ys,color="red")
plt.plot(xs,ysfitted,color="blue",linestyle="--")
plt.grid()
plt.xlabel("$N=2^{n}$")
plt.ylabel("$T(N)$")
plt.title("Asymptotic Complexity: x**(%1.2f)+%1.2f"%(coeffs[0],coeffs[1]))