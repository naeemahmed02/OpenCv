# Import Library
import cv2 as cv

# Loading image
image = cv.imread("naeem.jpg")

# Resize the image
resized_image = cv.resize(image, (500,300))

# Display the image in a window titled "Test Image"
cv.imshow("Test Image", resized_image)

# Wait for a key press indefinitely
cv.waitKey(0)
cv.destroyAllWindows()