import cv2

image = cv2.imread("../Images/face.png")
faceCascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")

gray_scale_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 1.1 is the scale value and 4 represnts the minimum neighbours
faces = faceCascade.detectMultiScale(gray_scale_frame, 1.1, 4)

for x,y,w,h in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 3)
cv2.imshow("Output Stream", image)

cv2.waitKey(0)

