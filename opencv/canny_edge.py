import cv2
import numpy as np

img=cv2.imread("edge_detection.png")

testFilter2D=False
testCanny=False
testBilateral=False
testSobel=True

(par0name,par1name)=("Lower Canny Threshold","Upper Canny Threshold")
(par0,par1)=(100,200)
(par0min,par0max)=(100,400)
(par1min,par1max)=(300,600)

def trackbar0_event(val):
    global img,par0
    par0=val
    updateImage()
    
def trackbar1_event(val):
    global img,par1
    par1=val
    updateImage()
    
def updateImage():
    global par0,par1
    if testFilter2D:
        N=par0
        kernel=1.0/N**2.0*np.ones((N,N))
        newimg=cv2.filter2D(img,-1,kernel)
        cv2.imshow("Filtered Image",newimg)
    elif testCanny:
        lowerThres=par0
        upperThres=par1
        edges=cv2.Canny(img,lowerThres,upperThres)
        cv2.imshow("Canny Edge Detection",edges)
    elif testBilateral:
        newimg=cv2.bilateralFilter(img,10,par0,par1)
        cv2.imshow("Bilateral Filter",newimg)
    elif testSobel:
        #newimg = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
        newimg=cv2.Laplacian(img,cv2.CV_64F)
        #kernel=np.ones((2,2))
        #newimg=cv2.erode(newimg,kernel)
        cv2.imshow("Sobel X",newimg)
#img=cv2.bilateralFilter(img,9,200,200)
#edges=cv2.Canny(img,250,500)

title_window="Edge Detection"
cv2.namedWindow(title_window, cv2.WINDOW_NORMAL)

trackbar_0=cv2.createTrackbar(par0name+" trackbar",title_window,par0min,par0max,trackbar0_event)
trackbar_1=cv2.createTrackbar(par1name+" trackbar",title_window,par1min,par1max,trackbar1_event)
updateImage()

k = cv2.waitKey()