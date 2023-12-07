import cv2 as cv

def display_image(window_name, image):
    cv.imshow(window_name, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def main():
    # Path of the Image
    path = 'resources/pexels-moose-photos-1586996.jpg'
    img = cv.imread(path)

    # Resize the image
    width, height = 400, 400
    resized_img = cv.resize(img, (width, height))
    display_image("Resized Image", resized_img)

    # Crop the image
    cropped_img = resized_img[0:250, 0:400]
    display_image("Cropped Image", cropped_img)

if __name__ == "__main__":
    main()
