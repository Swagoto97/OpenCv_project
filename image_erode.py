import cv2 as cv
import numpy as np

img = cv.imread("image1.png")
k = np.ones((7, 10), np.uint8)
m_img = cv.erode(img, k)
cv.imshow('disply window', m_img)
cv.waitKey(0)
