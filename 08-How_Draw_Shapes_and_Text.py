import cv2 as cv
import numpy as np

# Create a black image
image = np.zeros((250, 250, 3), np.uint8)
image[:] = 255, 0, 0  # Blue background

# Draw a green line on the image
line_start = (10, 10)
line_end = (240, 240)
line_color = (0, 255, 0)  # Green color
line_thickness = 2
cv.line(image, line_start, line_end, line_color, line_thickness)

# Draw a green rectangle on the image
rectangle_top_left = (50, 50)
rectangle_bottom_right = (200, 150)
rectangle_color = (0, 255, 0)  # Green color
rectangle_thickness = 3
cv.rectangle(image, rectangle_top_left, rectangle_bottom_right, rectangle_color, rectangle_thickness)

# Draw a blue circle on the image at the top-left corner
circle_center = (50, 50)
circle_radius = 50
line_color = (0, 0, 255) # Blue color
circle_thickness = 1
cv.circle(image, circle_center, circle_radius, line_color, circle_thickness)

# Write text on the image
text_position = (75, 200)
font = cv.FONT_HERSHEY_COMPLEX
font_scale = 0.5
text_color = (0, 15, 0)
text_thickness = 1
cv.putText(image, "Drawing Shapes on the image", text_position, font, font_scale, text_color, text_thickness)

# Show the final image
cv.imshow("Image with Shapes", image)

# Window Wait
cv.waitKey(0)
