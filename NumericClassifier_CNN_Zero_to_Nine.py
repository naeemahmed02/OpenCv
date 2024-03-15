import cv2 as cv
import numpy as np
import os
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from keras.layers import Conv2D, Flatten, Dropout, Dense, MaxPooling2D
from keras.models import Sequential
from keras.optimizers import Adam
import pickle

# Define constants
path = "myData"
test_ratio = 0.2
val_ratio = 0.2
img_dim = (32, 32, 3)
Batch_Size = 50
Epochs = 30

# Function to load and preprocess images
def load_and_preprocess_images(path, img_dim):
    images = []
    labels = []
    classes = os.listdir(path)
    num_classes = len(classes)
    
    for i, cls in enumerate(classes):
        cls_path = os.path.join(path, cls)
        for img_name in os.listdir(cls_path):
            img_path = os.path.join(cls_path, img_name)
            img = cv.imread(img_path)
            img = cv.resize(img, (img_dim[0], img_dim[1]))
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            img = cv.equalizeHist(img)
            img = img / 255
            images.append(img)
            labels.append(i)
    
    images = np.array(images)
    labels = np.array(labels)
    return images, labels, num_classes

# Load and preprocess images
X, y, num_classes = load_and_preprocess_images(path, img_dim)

# Split data into train, test, and validation sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val_ratio, random_state=42)

# Add depth to images
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1)
X_val = X_val.reshape(X_val.shape[0], X_val.shape[1], X_val.shape[2], 1)

# Data augmentation
data_gen = ImageDataGenerator(
    width_shift_range=0.1,
    height_shift_range=0.1,
    rotation_range=10,
    shear_range=0.1,
    zoom_range=0.20
)
data_gen.fit(X_train)

# One-hot encode labels
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)
y_val = to_categorical(y_val, num_classes)

# Define the model
model = Sequential([
    Conv2D(32, (5,5), input_shape=(img_dim[0], img_dim[1], 1), activation='relu'),
    Conv2D(32, (5,5), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(60, (3,3), activation='relu'),
    Conv2D(120, (3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.5),
    Flatten(),
    Dense(550, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])
model.compile(Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit_generator(
    data_gen.flow(X_train, y_train, batch_size=Batch_Size),
    epochs=Epochs,
    validation_data=(X_val, y_val),
    shuffle=True
)

# Evaluate the model
score = model.evaluate(X_test, y_test, verbose=0)
print('Test Score:', score[0])
print('Test Accuracy:', score[1])

# Plot accuracy and loss
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

# Saving the model
model_out = open('trained_model.p', 'wb')
pickle.dump(model, model_out)
model_out.close()
