import cv2 as cv
import numpy as np


def resize_and_display(images, scale_factor=0.5, direction='horizontal'):
    # Resize each image in the list using the specified scale factor
    resized_images = [cv.resize(img, (300, 200), fx=scale_factor, fy=scale_factor) for img in images]

    # Combine images either horizontally or vertically based on the specified direction
    if direction == 'horizontal':
        combined = np.hstack(resized_images)
    elif direction == 'vertical':
        combined = np.vstack(resized_images)
    else:
        raise ValueError("Invalid direction. Use 'horizontal' or 'vertical'.")

    # Display the combined image and wait for a key press
    cv.imshow(direction.capitalize(), combined)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    # Read the original images
    img1 = cv.imread('resources/pexels-carolin-wenske-19135988.jpg')
    img2 = cv.imread('resources/pexels-moose-photos-1586996.jpg')

    print("Original Shape:", img1.shape)
    print("Original Shape:", img2.shape)

    # Display the resized and combined images horizontally
    resize_and_display([img1, img2], scale_factor=0.5, direction='horizontal')
    resize_and_display([img1, img2], scale_factor=0.5, direction='vertical')
