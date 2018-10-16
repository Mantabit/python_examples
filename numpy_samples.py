#this file illustrates basic operations with narray objects
import numpy as np

N=3

#create various matrices
mat_ones=np.ones((N,N))
mat_zeros=np.zeros((N,N))
mat_unity=np.diag([1 for i in range(N,1)])

#create matrix using iterations
mat_it=np.zeros((5,5))
for i in range(0,5):
    for j in range(0,5):
        mat_it[i,j]=5*(i+1)+(j+1)
        
#create diagional matrices
diag_elements=[1 for i in range(0,3)]
mat_unity3=np.diag(diag_elements)
        
#transpose matrix
mat_it_transposed=mat_it.T

#concatenate matrices
mat_onesconchor=np.concatenate((mat_ones,mat_ones),axis=1)
mat_onesconcver=np.concatenate((mat_ones,mat_ones),axis=0)
        
#get the largest and smallest element of an 2array
mat_rand=np.random.rand(N,N)
maxindex1d=np.argmax(mat_rand)
minindex1d=np.argmin(mat_rand)
maxindex2d=np.unravel_index(maxindex1d,mat_rand.shape)
minindex2d=np.unravel_index(minindex1d,mat_rand.shape)

#cross product and dot product of 3d vectors
vec1=np.array([1,2,3])
vec2=np.array([2,3,4])
cross_prodcut=np.cross(vec1,vec2)
dot_product=np.dot(vec1,vec2)

#operations: ndarray-scalar
mat1=np.zeros((5,5))+1
mat2=np.ones((5,5))*5

#operations: matrix product vs ndarray product
mat1=np.ones((5,5))*5
mat2=np.ones((5,5))*2
elementwise_product=mat_unity3*mat_ones
matrix_product=np.dot(mat_unity3,mat_ones)