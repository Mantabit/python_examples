import numpy as np
import matplotlib.pyplot as plt

testnums=np.random.rand(2**10)

"""
This function takes an array of numbers arr and it will partition the array in a subarray whose elements are larger than arr[hi] and a subarray whose elements are smaller than arr[hi]
"""
def partition(arr,lo,hi):
    def swap(arr,a,b):
        cache=arr[a]
        arr[a]=arr[b]
        arr[b]=cache
    pivot=arr[hi]
    #this variable indicates the start of the part of the sorted subarray which is larger than the pivot
    i=lo
    for j in range(lo,hi,1):
        #if the current element is smaller than the pivot, swap it with the first element of the subarray which is larger than the pivot and increase the i by 1
        if(arr[j]<pivot):
            swap(arr,i,j)
            i+=1
    swap(arr,i,hi)
    return i

if __name__=="__main__":           
    print(partition(testnums,0,len(testnums)-1))
    plt.plot(testnums,"o")