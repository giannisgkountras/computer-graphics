import cv2
import numpy as np

from render_img import render_img

# Load the data
data = np.load("hw1.npy", allow_pickle=True).item()

# Use the function to create an image
img = render_img(data["faces"], data["vertices"], data["vcolors"], data["depth"], "g")

# Make the RGB values range from [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)

# Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Save the image as jpg
cv2.imwrite("gouraud_shading_image.jpg", rgb_img)

# Show the image
cv2.imshow("Image with Gouraud Shading", rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
