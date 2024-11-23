import cv2
import numpy as np

def warp_image(image_path, save_path):
    img = cv2.imread(image_path)

    # Get image dimensions
    rows, cols, _ = img.shape

    # Define warp points (for fun distortion)
    src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
    dst_points = np.float32([[0, rows * 0.33], [cols * 0.85, rows * 0.25], [cols * 0.15, rows * 0.7]])

    # Compute the transformation matrix
    matrix = cv2.getAffineTransform(src_points, dst_points)

    # Apply warp
    warped_img = cv2.warpAffine(img, matrix, (cols, rows))

    # Save the warped image
    cv2.imwrite(save_path, warped_img)
    return save_path
