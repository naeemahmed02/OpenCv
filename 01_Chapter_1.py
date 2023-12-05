# Import Library
import cv2 as cv

# Loading image
image = cv.imread("naeem.jpg")

# Display the image in a window titled "Test Image"
cv.imshow("Test Image", image)

# Wait for a key press indefinitely
cv.waitKey(0)
