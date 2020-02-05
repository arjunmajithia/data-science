import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# face-detection
# haar-cascade is pretrained model for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

skip = 0
face_data = []
dataset_path = './data/'

file_name = input('Enter name of person: ')

while True:
    ret, frame = cap.read()

    if ret == False:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    # faces is a list of tuple storing (x, y, w, h)
    # x, y top left coordinates and w, h: width, height
    # 1.3 is scaling factor
    # 5 is minimum neighbours
    faces = sorted(faces, key = lambda f: f[2]*f[3])
    # sorted on basis of area w*h

    # pick the last face (because it is the largest face)
    for face in faces[-1:]:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

        # extract (crop out the reuired face): region of interest
        offset = 10             # padding of 10pixel

        # frame is in the form frame[y-axis][x-axis]
        face_section = frame[y-offset: y+h+offset, x-offset: x+w+offset]
        face_section = cv2.resize(face_section, (100, 100))

        skip += 1
        if skip%10 == 0:
            face_data.append(face_section)
            print(len(face_data))

    cv2.imshow('frame', frame)
    cv2.imshow('face section', face_section)
    
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

# convert our face list into numpy array
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0], -1))
# print(face_data)

# save this data into file system, data is saved as rgb values
np.save(dataset_path+file_name+'.npy', face_data)
print("Data saved successfully")

cap.release()
cv2.destroyAllWindows()
