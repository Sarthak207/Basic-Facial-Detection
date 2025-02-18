import cv2

cap=cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()

    if ret:
        gray_scale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 1.1 is the scale value and 4 represnts the minimum neighbours
        faces = faceCascade.detectMultiScale(gray_scale_frame, 1.1, 4)

        for x,y,w,h in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)
        cv2.imshow("Output Stream", frame)
        if cv2.waitKey(1) & 0xFF==ord('1'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
