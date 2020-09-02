import cv2
import numpy as np
img = cv2.imread("lamboghini.jpg") #loading the test img
print(img.shape) #printing dimensions of img


imgResize = cv2.resize(img,(200,150)) #resizing img with width=200 and height 150
print(imgResize.shape) #printing dimensions of resized img

imgCropped = img[65:160,5:220] #used lists #Cropping #!! here the first argument is height and then width unlike in the case of resizing!

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)