import numpy as np
from scipy import ndimage

"""
This script computes a 3 dimensional kernel which can be used to spatially low-pass filter
a three dimensional data set by convoluting that data set with the kernel
"""

width=3                         #number of averaging layers around point
weight = lambda r : 1/r         #the weighting function determines the weight of a node as a function of distance from the center
centerweight = 1/2              #relative weight of the center point

kernel=np.zeros((1+2*width,1+2*width,1+2*width))
weightsum=0                     #we keep track of the sum of weight in order to normalize later

#iterate over all points of the kernel
for x in range(0,2*width+1):
    for y in range(0,2*width+1):
        for z in range(0,2*width+1):
            (symx,symy,symz)=(x-width,y-width,z-width) #symmetric indices, the center point has symmetric index (0,0,0)
            if(symx==0 and symy==0 and symz==0):
                print("(%d,%d,%d"%(x,y,z))
                continue
            layern=max([abs(ind) for ind in (symx,symy,symz)]) #determine the layer of the current node
            currentweight=weight(layern) #weighting factor for the current node, depends only on the distance from the center
            kernel[x,y,z]=currentweight
            weightsum+=currentweight
kernel=(kernel/weightsum)*(1-centerweight)
kernel[width,width,width]=centerweight

#generate some three dimensional test data
N=20
toRealCoordinate = lambda index: np.array([-N/2+index[k] for k in range(0,3)])
testdata=np.zeros((N,N,N))
for x in range(0,N):
    for y in range(0,N):
        for z in range(0,N):
            realCoords=toRealCoordinate((x,y,z))
            testdata[x,y,z]=np.sin(realCoords[0])*realCoords[1]+np.cos(realCoords[2]*5)
            
#convolute the testdata with the kernel
ndimage.convolve(testdata, kernel, mode='nearest')