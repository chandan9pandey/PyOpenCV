import cv2
import numpy as np

img = cv2.imread("lena.jpg") #for reading the image
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting from color to graysacle
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #blurring the gray img
imgCanny = cv2.Canny(img,100,100) #edge detection of the image
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1) #thicking the edges
imgEroded = cv2.erode(imgDilation,kernel,iterations=1) #thining the edges

cv2.imshow("GrayOutput",imgGray)
cv2.imshow("BlurOutput",imgBlur)
cv2.imshow("CannyOutput",imgCanny)
cv2.imshow("DilationOutput",imgDilation)
cv2.imshow("ErodedOutput",imgEroded)
cv2.waitKey(0) #displaying the image for certain time