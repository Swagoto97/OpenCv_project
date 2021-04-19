import cv2 as cv
img = cv.imread("image1.png")
cv.imshow('disply window', img)
cv.waitKey(0)
# Gaussian Blur
# Gaussian = cv.GaussianBlur(img, (7, 7), 0)
# cv.imshow('Gaussian Blurring', Gaussian)
# cv.waitKey(0)
# Median Blur
# median = cv.medianBlur(img, 5)
# cv.imshow('Median Blurring', median)
# cv.waitKey(0)


# Bilateral Blur
bilateral = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral Blurring', bilateral)
cv.waitKey(0)
cv.destroyAllWindows()
