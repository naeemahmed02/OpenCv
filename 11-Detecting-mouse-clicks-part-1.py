# Import libraries
import cv2 as cv
import numpy as np


# Function for detecting mouse clicks
def mouse_points(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)


# Loading Images
img = cv.imread("resources/cards.jpg")
cv.imshow("Original Image", img)
cv.setMouseCallback("Original Image", mouse_points)

# Wait key
cv.waitKey(0)
cv.destroyAllWindows()
