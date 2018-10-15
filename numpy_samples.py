#this file illustrates basic operations with narray objects
import numpy as np

N=5

#create various matrices
mat_ones=np.ones((N,N))
mat_zeros=np.zeros((N,N))
mat_unity=np.diag([1 for i in range(N,1)])

#concatenate matrices
mat_onesconchor=np.concatenate((mat_ones,mat_ones),axis=1)
mat_onesconcver=np.concatenate((mat_ones,mat_ones),axis=0)

for i in range(0,mat_ones.shape[0]):
    for j in range(0,mat_ones.shape[1]):
        print(mat_ones[i,j])
        
#get the largest and smallest element of an 2array
mat_rand=np.random.rand(N,N)
maxindex1d=np.argmax(mat_rand)
minindex1d=np.argmin(mat_rand)
maxindex2d=np.unravel_index(maxindex1d,mat_rand.shape)
minindex2d=np.unravel_index(minindex1d,mat_rand.shape)