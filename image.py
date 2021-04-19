import cv2 as cv
img = cv.imread("image1.png", cv.IMREAD_GRAYSCALE)
cv.imshow('disply window', img)
cv.waitKey(0)
