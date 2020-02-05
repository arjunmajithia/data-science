import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('frontalEyes35x16.xml')
mouth_cascade = cv2.CascadeClassifier('Nose18x15.xml')

glasses = cv2.imread('./images/glasses.png', -1)
mouth = cv2.imread('./images/mustache.png', -1)

while True:
    frame = cv2.imread('./images/Before.png')
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    # face
    for face in faces:
        x, y, w, h = face
        face_section = frame[y: y+h, x: x+w]
        
        # eyes
        eyes = eye_cascade.detectMultiScale(face_section, 1.3, 5)
        for eye in eyes:
            ex, ey, ew, eh = eye
            eye_section = face_section[ey: ey+eh, ex: ex+ew]
            # print(ew, eh)
            
            # glasses
            glasses = cv2.resize(glasses, (ew, eh))
            gw, gh, gc = glasses.shape
            for i in range(gw):
                for j in range(gh):
                    if glasses[i, j][3] != 0:
                        face_section[ey+i, ex+j] = glasses[i, j]

        # mustaches
        nose = mouth_cascade.detectMultiScale(face_section, 1.3, 5)
        for n in nose:
            nx, ny, nw, nh = n
            nose_section = face_section[ny: ny+nh, nx: nx+nw]

            # mustaches
            mw, mh, mc = mouth.shape
            mouth = cv2.resize(mouth, (nw, nh))

            mw, mh, mc = mouth.shape
            for i in range(mw):
                for j in range(mh):
                    if mouth[i, j][3] != 0:
                        face_section[ny+int(25)+i, nx+j] = mouth[i, j]


    # print(glasses.shape)
    # cv2.imshow('mustaches', mouth)
    # cv2.imshow('nose', nose_section)
    cv2.imshow('image', frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
print(frame.shape)
frame = frame.reshape((-1, 3))
import csv
with open('answer.csv', 'w') as f:
    f.write('Channel 1,Channel 2,Channel 3' + '\n')
    for i in range(frame.shape[0]):
        data = str(frame[i][0]) + ',' + str(frame[i][1]) + ',' + str(frame[i][2]) + '\n'
        f.write(data)

cv2.destroyAllWindows()