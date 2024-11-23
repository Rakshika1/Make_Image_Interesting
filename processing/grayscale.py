import cv2

def grayscale_image(image_path, save_path):
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite(save_path, gray_img)
    return save_path
