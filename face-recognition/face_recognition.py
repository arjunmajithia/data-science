import cv2
import numpy as np
import os

def dist(x1, x2):
    return np.sqrt(sum((x1-x2)**2))

def KNN(X_train, Y_train, queryPoint, k = 5):
    vals = []
    m = X_train.shape[0]

    for i in range(m):
        d = dist(X_train[i], queryPoint)
        vals.append((d, Y_train[i]))

    vals.sort()
    vals = vals[:k]

    vals = np.array(vals)

    new_vals = np.unique(vals[:, 1], return_counts = True)

    index = new_vals[1].argmax()
    return new_vals[0][index]

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

skip = 0
dataset_path = './data/'

face_data = []
labels = []

class_id = 0
names = {}

for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        names[class_id] = fx[:-4]
        data_item = np.load(dataset_path+fx)

        face_data.append(data_item)

        target = class_id * np.ones((data_item.shape[0], ))
        class_id += 1
        labels.append(target)

face_dataset = np.concatenate(face_data, axis = 0)
face_labels = np.concatenate(labels, axis = 0)

# print(face_dataset.shape)
# print(face_labels.shape)

while True:
    ret, frame = cap.read()
    if ret == False:
        continue

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    if len(faces) > 0:
        for face in faces:
            x, y, w, h = face

            offset = 10
            face_section = frame[y-offset: y+h+offset, x-offset:x+w+offset]
            face_section = cv2.resize(face_section, (100, 100))

            out = KNN(face_dataset, face_labels, face_section.flatten())

            if int(out) < len(names):
                pred_name = names[int(out)]
                cv2.putText(frame, pred_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    cv2.imshow('Faces', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()