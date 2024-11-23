import cv2

def cartoonify_image(image_path, save_path):
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # Edge detection
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )

    # Bilateral filter for smoothing
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Combine edges and smoothed image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Save the cartoonified image
    cv2.imwrite(save_path, cartoon)
    return save_path
