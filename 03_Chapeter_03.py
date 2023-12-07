# Import library
import cv2 as cv

# Load image
img = cv.imread('naeem.jpg')

# Check if the image is successfully loaded
if img is not None:
    # Resize the image
    resized_image = cv.resize(img, (500, 300))

    # Convert to grayscale
    gray_image = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv.imshow('Gray Image', gray_image)

    # Wait for a key press indefinitely
    cv.waitKey(0)

    # Close the window and release resources
    cv.destroyAllWindows()
else:
    print("Failed to load the image.")
