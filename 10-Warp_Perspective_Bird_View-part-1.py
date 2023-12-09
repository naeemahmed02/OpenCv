# Import Library
import cv2 as cv
import numpy as np

# Loading image
image = cv.imread("resources/cards.jpg")

# Check if the image is successfully loaded
if image is None:
    print("Failed to load the image.")
else:
    # Resize the image
    resized_image = cv.resize(image, (300, 200))

    # Define the target height and width
    height, width = 400, 300

    # Define the source and destination points for perspective transformation
    pts1 = np.float32([[1650, 1785], [2440, 1704], [1761, 3116], [2552, 2944]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # Get the perspective transformation matrix
    matrix = cv.getPerspectiveTransform(pts1, pts2)

    # Apply perspective transformation to the original image
    output_image = cv.warpPerspective(image, matrix, (width, height))

    # Draw circles on the original image at the source points
    for x in range(0, 4):
        cv.circle(image, (int(pts1[x][0]), int(pts1[x][1])), 100, (0, 0, 255), -1)
        # cv.circle(image, (pts1[x][0], pts1[x][1]), 5, (0, 0, 255), cv.FILLED)

    # Display the original and transformed images
    cv.imshow("Original Image", image)
    cv.imshow("Transformed Image", output_image)

    # Wait for a key press indefinitely
    cv.waitKey(0)

    # Close all windows and release resources
    cv.destroyAllWindows()
