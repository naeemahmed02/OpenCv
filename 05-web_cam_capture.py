# Import libraries
import cv2 as cv

# Define frame
frame_width = 640
frame_height = 360

# Capture the video using webcam
cap = cv.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)

# Loop the video
while True:
    success, img = cap.read()

    # Displaying the captured frame
    cv.imshow("Web Cam", img)

    # Introduce a delay to control the frame rate
    if cv.waitKey(33) & 0xFF == ord('q'):
        break

# Release the capture object and close the window
cap.release()
cv.destroyAllWindows()
