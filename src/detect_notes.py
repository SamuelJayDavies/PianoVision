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