# Import Libraries
import cv2 as cv

# Define frame
frame_width = 640
frame_height = 480

# Capture the video
cap = cv.VideoCapture("resources/test_video.mp4")

# Check if video is successfully opened
if not cap.isOpened():
    print("Error: Could not open the video.")
    exit()

# Loop the video
while True:
    success, img = cap.read()

    if not success:
        print("Error: Failed to capture frame.")
        break

    cv.imshow("Test Video", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv.destroyAllWindows()
