import cv2
print("package imported")

# img =cv2.imread("lena.jpg", 1) #...........For Capturing Images###
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)
# waitKey(0)

# cap=cv2.VideoCapture("tree.avi") #...........For Capturing Videos###
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

cap=cv2.VideoCapture(0) #...........For Capturing Webcam###
cap.set(3,640)  ##id-no3 for width
cap.set(4,480)  ##id-no3 for hight
cap.set(10,100) ##id-no10 for brightness
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break