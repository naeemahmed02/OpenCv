# Import Library
import cv2 as cv

# Loading image
image = cv.imread("naeem.jpg")

# Check if the image is successfully loaded
if image is not None:
    # Resize the image
    resized_image = cv.resize(image, (500, 300))

    # Display the resized image in a window titled "Test Image"
    cv.imshow("Test Image", resized_image)

    # Wait for a key press indefinitely
    cv.waitKey(0)

    # Close the window and release resources
    cv.destroyAllWindows()
else:
    print("Failed to load the image.")
