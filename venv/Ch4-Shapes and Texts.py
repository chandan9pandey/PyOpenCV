import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[:]=255,0,0 #color=blue
print(img.shape) #to check the dimensionality of a matrix

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,255,255),cv2.FILLED)
cv2.circle(img,(256,256),50,(255,0,255),5)
cv2.putText(img," OPENCV ",(300,300),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,255),3)
cv2.imshow("Image",img)
cv2.waitKey(0)