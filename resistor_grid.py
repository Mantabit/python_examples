# -*- coding: utf-8 -*-
#code used to compute resistance between two points in an arbitrary grid of equivalent resistors
#the length of the cube contains 2n nodes
#there are (2n)²=4n² nodes in total
#the adjacence matrix has (4n²)²=16n⁴ entries
#note that the potential at a given node is the mean of the potentials of the surrounding nodes
import numpy as np

n=2
l=2*n

givenPotentials={(1,1),(2,2)}

def getDegree(point):
    global n
    if point==(0,0) or point==(l-1,0) or point==(0,l-1) or point==(l-1,l-1):
        return 2
    elif point[0]==0 or point[0]==l-1 or point[1]==0 or point[1]==l-1:
        return 3
    else:
        return 4

#A is the adjacence matrix; b is the solution vector; x are the unknown potentials
A=np.zeros((4*n**2,4*n**2))
b=np.zeros((4*n**2,1))

#set given potentials

#set edge nodes

#set inner nodes and side nodes
for i in range(0,l):
    for j in range(0,l):
        #given potentials and edges have already been set
        if (i,j) in givenPotentials or getDegree((i,j))==2:
            continue
        else:
            deg=getDegree((i,j))
            if (i,j)==(1,3):
                print("x")
            A[l*i+j,l*i+j]=-deg
            #if inner node...
            if deg==4:
                A[l*i+j,l*(i+1)+j]=1
                A[l*i+j,l*(i-1)+j]=1
                A[l*i+j,l*i+j+1]=1
                A[l*i+j,l*i+j-1]=1
            #if side node...
            else:
                #left side
                if j==0:
                    A[l*i+j,l*(i+1)+j]=1
                    A[l*i+j,l*(i-1)+j]=1
                    A[l*i+j,l*i+j+1]=1
                #right side
                elif j==l-1:
                    A[l*i+j,l*(i+1)+j]=1
                    A[l*i+j,l*(i-1)+j]=1
                    A[l*i+j,l*i+j-1]=1
                #top
                elif i==0:
                    A[l*i+j,l*i+j-1]=1
                    A[l*i+j,l*i+j+1]=1
                    A[l*i+j,l*(i+1)+j]=1
                #bottom
                else:
                    A[l*i+j,l*i+j-1]=1
                    A[l*i+j,l*i+j+1]=1
                    A[l*i+j,l*(i-1)+j]=1

