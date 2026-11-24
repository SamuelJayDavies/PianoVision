import cv2 as cv
import numpy as np

test_image = cv.imread('data/screenshots/test_smb_photo.png')
print(test_image.shape)

cv.imshow('Test Image', test_image)
cv.waitKey(0)
cv.destroyAllWindows()

cropped_image = test_image[0:905]
cv.imshow('Cropped Image', cropped_image)
cv.waitKey(0)
cv.destroyAllWindows()


# Testing Edge Detection
test_image_grey = cv.cvtColor(test_image, cv.COLOR_BGR2GRAY)

cv.imshow('Grey Image', test_image_grey)
cv.waitKey(0)
cv.destroyAllWindows()

edges = cv.Canny(test_image_grey, 100, 200)
cv.imshow('Edges', edges)
cv.waitKey(0)
cv.destroyAllWindows()

