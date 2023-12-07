# import libraries
import cv2 as cv
import numpy as np

# load the image
img = cv.imread('naeem.jpg')

# Function 1: Resize the image
resized_img = cv.resize(img, (300, 200))

# Funtion 2: Change to Grayscale
gray_img = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)

# Function 3: Adding Blur
blurred_img = cv.GaussianBlur(resized_img, (7, 7), 0)

# Function 4: Edges of the image
canny_img = cv.Canny(gray_img, 100, 200)

# Set the kernel
kernel = np.ones((3, 3), np.uint8)

# Function 5: Dilation
img_dilation = cv.dilate(canny_img, kernel=kernel, iterations=1)

# Function 6: Erosion
erosion_img = cv.erode(img_dilation, kernel, iterations=1)

# Display the images
cv.imshow("Original Image", img)
cv.imshow("Resized Image", resized_img)
cv.imshow("Gray Image", gray_img)
cv.imshow("Blurred Image", blurred_img)
cv.imshow("Canny Image", canny_img)
cv.imshow("Dilated Image", img_dilation)
cv.imshow("Erosion Image", erosion_img)

# Wait
cv.waitKey(0)
cv.destroyAllWindows()
