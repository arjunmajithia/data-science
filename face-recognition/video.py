import cv2

# read a video stream from camera (frame by frame)
cap = cv2.VideoCapture(0)
# 0 means default webcam

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ret = false means image not captured, hence continue
    if ret == False:
        continue

    cv2.imshow('Video Frame', frame)
    cv2.imshow('Gray Video Frame', gray)

    # returns ascii value, & with 0xFF gives 8 bit number (ord('q') gives 8 bit ascii value of q)
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

# release the use of webcam
cap.release()
cv2.destroyAllWindows()