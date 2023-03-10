import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4) #all faces in the image

    for (x, y, w, h) in faces: #rectangles for faces

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 4) #draw a rectangle

        roi_gray = gray[y:y+w, x:x+w] #region of interest - storing face from the rectangle into roi
        roi_color = frame[y:y+h, x:x+w] #it's a reference to the original frame
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 4) #looking for eyes in the region

        for (ex, ey, ew, eh) in eyes: #draw rectangles for eyes
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 4)

            cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

