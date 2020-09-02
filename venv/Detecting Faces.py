import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# img = cv2.imread("lena.jpg")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)
#
# for (x,y,w,h) in faces:
#     cv2.rectangle (img,(x,y),(x+w,y+h),(255,0,0),2)
# cv2.imshow("Result",img)
# cv2.waitKey(0)
###########.........For Webcam.........#########
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle (img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff ##for breaking out of the loop after pressing ESC key
    if k==27:
        break
cap.release()


