# Import library
import cv2 as cv

# Load image
img = cv.imread('naeem.jpg')

# Resize the image
resized_image = cv.resize(img, (500, 300))

# Convert to grayscale
gray_image = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)

# display image
cv.imshow('Gray Image', gray_image)

# Time
cv.waitKey(0)
cv.destroyAllWindows()