import numpy as np
import cv2

# 图片转成灰度图
im = cv2.imread('image/DSC00001.JPG')
g = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,g = cv2.threshold(g,127,255,cv2.THRESH_BINARY)


a,b,c = cv2.findContours(g,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
i = cv2.drawContours(im,b, -1, (0,0,255),3)



cv2.imshow('image/DSC00001',a)
cv2.waitKey(1000)
cv2.destroyAllWindows()
cv2.imwrite('image/DSC00001_1.png',a)
# cv2.imwrite('DSC00001_contours.png')
print(b)