import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
stream = cv2.VideoCapture(0)

while(True):
    (ret,frame) = stream.read()
    if not ret:
        break
        print("Webcam not able to capture Frame")

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.3,minNeighbors = 5)

    for(c,r,w,h) in faces:
        color = (0,114,4)
        stroke = 3
        cv2.rectangle(frame,(c,r),(c+w,r+h),color,stroke)

    cv2.imshow("Image",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()
cv2.waitKey(1)