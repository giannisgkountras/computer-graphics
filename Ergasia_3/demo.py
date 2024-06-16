import cv2
import numpy as np
from render_object import render_object

import time

# Load the data
data = np.load("hw3.npy", allow_pickle=True).item()

# ===================== STEP 0 ======================#
# Use the function to create an image

# Set start time
start = time.time()
# print(data)
img = render_object(
    "gouraud",
    data["focal"],
    data["cam_eye"],
    data["cam_lookat"],
    data["cam_up"],
    data["bg_color"],
    data["M"],
    data["N"],
    data["H"],
    data["W"],
    data["verts"],
    data["vertex_colors"],
    data["face_indices"],
    data["ka"],
    data["kd"],
    data["ks"],
    data["n"],
    data["light_positions"],
    data["light_intensities"],
    data["Ia"],
)

end = time.time()

print("Step 0 finished in", round(end - start, 2), "seconds.")
# Make the RGB values range [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)
# Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img_step_0 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Flip the image vertically to match the original data
img_flipped = cv2.flip(rgb_img_step_0, 0)
cv2.imshow("Image Step 0", img_flipped)
cv2.waitKey(0)


cv2.destroyAllWindows()
