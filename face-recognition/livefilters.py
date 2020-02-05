import cv2
import numpy as np

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('frontalEyes35x16.xml')

glasses = cv2.imread('./images/glasses.png', -1)

while True:
    ret, frame = cap.read()
    if ret == False:
        continue

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for face in faces:
        x, y, w, h = face
        face_section = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(face_section, 1.2, 5)
        for eye in eyes:
            ex, ey, ew, eh = eye
            eye_section = face_section[ey-10: ey+eh, ex-10: ex+ew]
            # print(ew, eh)
            
            # glasses
            glasses = cv2.resize(glasses, (ew, eh))
            glass = glasses[:, :, :3]
            gw, gh, gc = glasses.shape
            for i in range(gw):
                for j in range(gh):
                    if glasses[i, j][3] != 0:
                        face_section[ey+i, ex+j] = glass[i, j]

    cv2.imshow('Live Filters', frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()