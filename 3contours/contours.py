import numpy as np
import cv2

img = cv2.imread('image/DSC00001_mask.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
image,contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0,0,255),3)



cv2.namedWindow('original image',0)
cv2.resizeWindow('original image', 1200, 900)
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite('DSC00001_1.png',a) 