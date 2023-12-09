import cv2 as cv
import numpy as np

# Define the array to store the values of the clicks
circles = np.zeros((4, 2), dtype=int)
# Counter
counter = 0


# Function for detecting mouse clicks
def mouse_points(event, x, y, flags, params):
    global counter
    if event == cv.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        print(f"Point {counter + 1}: ({x}, {y})")
        counter += 1


# Reading Image
img = cv.imread("resources/book2.jpg")

# Main loop
while True:
    # Check if four points have been collected
    if counter == 4:
        # Define the target height and width
        height, width = 400, 300
        # Define the source and destination points for perspective transformation
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

        # Print collected points for debugging
        print("Collected Points:")
        for i, point in enumerate(pts1):
            print(f"Point {i + 1}: ({point[0]}, {point[1]})")

        # Get the perspective transformation matrix
        matrix = cv.getPerspectiveTransform(pts1, pts2)
        # Apply perspective transformation to the image
        output_image = cv.warpPerspective(img, matrix, (width, height))
        # Display the transformed image
        cv.imshow("Bird's Eye View", output_image)

    # Draw circles on the image at the clicked points
    for x in range(0, counter):
        cv.circle(img, (circles[x][0], circles[x][1]), 30, (0, 255, 0), cv.FILLED)

    # Display the image with circles
    cv.imshow("Image", img)

    # Set Mouse Callback
    cv.setMouseCallback("Image", mouse_points)

    # Wait for a key press (1 millisecond delay)
    key=cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Close all OpenCV windows
cv.destroyAllWindows()
