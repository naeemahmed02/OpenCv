##### Import Library
import cv2 as cv

##### Loading image
image = cv.imread("naeem.jpg")

##### Check if the image is successfully loaded
if image is not None:
    ##### Display the image in a window titled "Test Image"
    cv.imshow("Test Image", image)

    ##### Wait for a key press indefinitely
    cv.waitKey(0)

    ##### Close the window and release resources
    cv.destroyAllWindows()
else:
    ##### Print a message if the image loading failed
    print("Failed to load the image.")
