import cv2

img = cv2.imread('dog.jpg')
gray = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog Image', img)
cv2.imshow('Gray Dog Image', gray)
# cv2.imshow reads image as BGR, hence no need to convert
# first argument is title

cv2.waitKey(0)
# wait means to wait before the window is destroyed
# 0 means wait infinitely
# 250 would mean wait for 250ms
 
cv2.destroyAllWindows()