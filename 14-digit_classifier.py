import cv2 as cv
import numpy as np
from keras.models import load_model

# Settings
frame_width = 640
frame_height = 480
threshold = 0.8

# Capture the img
cap = cv.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)

# Load the model
model = load_model('trained.h5', compile=False)

# Define class names (replace with your own classes)
class_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

# Image preprocessing
def preprocessing(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.equalizeHist(img)
    img = img / 255
    return img

while True:
    _, original = cap.read()
    img = cv.resize(original, (32, 32))
    img = preprocessing(img)
    img = img.reshape(1, 32, 32, 1)

    predictions = model.predict(img)
    prob = np.amax(predictions)
    class_index = np.argmax(predictions)

    if prob > threshold:
        class_name = class_names[class_index]
        text = f"{class_name}: {prob:.2f}"
        cv.putText(original, text, (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    cv.imshow("Demo", original)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()