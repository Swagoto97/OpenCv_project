import cv2 as cv
img = cv.imread("image1.png")
B, G, R = cv.split(img)
cv.imshow('disply window', img)
cv.waitKey(0)
cv.imshow('disply window', B)
cv.waitKey(0)
cv.imshow('disply window', G)
cv.waitKey(0)
cv.imshow('disply window', R)
cv.waitKey(0)
cv.destroyAllWindows()