import cv2                                               
import numpy as np
 
cap = cv2.imread('image/DSC00001.JPG')
#将颜色转换为HSV
hsv = cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)
 
#hsv的上下限
lower_red = np.array([26,40,70]) 
upper_red = np.array([84,255,132])
 
mask = cv2.inRange(hsv,lower_red,upper_red)
res = cv2.bitwise_and(cap,cap,mask=mask)

cv2.imwrite('image/DSC00001_mask.png',mask)
cv2.imwrite('image/DSC00001_res.png',res)


cv2.namedWindow('processed',0)
cv2.resizeWindow('processed', 640, 480)
cv2.imshow('processed',res)
cv2.namedWindow('original image',0)
cv2.resizeWindow('original image', 640, 480)
cv2.imshow('original image',cap)
 
cv2.waitKey(0)
cv2.destroyAllWindows()