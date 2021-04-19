import cv2 as cv
img = cv.imread("image1.png")
big_img = cv.resize(img, (720, 640))
cv.imshow('disply window', big_img)
cv.waitKey(0)
