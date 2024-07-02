import numpy as np
import cv2


def prepareImgForOpenCV(img):
    # Make the RGB values range [0,255] instead of [0,1]
    img *= 255
    img = img.astype(np.uint8)
    # Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
    rgb_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # Flip the image vertically to match the original data
    img_flipped = cv2.flip(rgb_img, 0)
    return img_flipped
