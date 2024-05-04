import cv2
import numpy as np
import time
from render_object import render_object

# Load the data
data = np.load("hw2.npy", allow_pickle=True).item()

# Track before time to calculate render time
before = time.time()

# Use the function to create an image
img = render_object(
    data["v_pos"],
    data["v_clr"],
    data["t_pos_idx"],
    data["plane_h"],
    data["plane_w"],
    data["res_h"],
    data["res_w"],
    data["focal"],
    data["eye"],
    data["up"],
    data["target"],
)
# img = render_img(data["faces"], data["vertices"], data["vcolors"], data["depth"], "f")

# Track after time to calculate render time
after = time.time()
print("Finished rendering in ", round(after - before, 2), "seconds")

# Make the RGB values range [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)

# # Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# # Save the image as jpg
# cv2.imwrite("flat_shading_image.jpg", rgb_img)
# print("Saved image in flat_shading_image.jpg")

# # Show the image
cv2.imshow("Image", rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
