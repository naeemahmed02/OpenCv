# Import Library
import cv2 as cv

# Loading image
image = cv.imread("OpenCv-code\resources\naeem.jpg")

# Resize the image
resized_image = cv.resize(image, (800,600))

# Display the image in a window titled "Test Image"
cv.imshow("Test Image", image)

# Wait for a key press indefinitely
cv.waitKey(0)
cv.destroyAllWindows()