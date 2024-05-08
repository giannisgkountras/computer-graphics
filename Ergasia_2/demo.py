import cv2
import numpy as np
from render_object import render_object
from transform import Transform
import time

# Load the data
data = np.load("hw2.npy", allow_pickle=True).item()

# ===================== STEP 0 ======================#
# Use the function to create an image

# Set start time
start = time.time()

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

end = time.time()

print("Step 0 finished in", round(end - start, 2), "seconds.")
# Make the RGB values range [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)
# Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img_step_0 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


# ===================== STEP 1 ======================#

# Set start time
start = time.time()

transform = Transform()
transform.rotate(data["theta_0"], data["rot_axis_0"])
updated_points = transform.transform_pts(data["v_pos"])

# Use the function to create an image
img = render_object(
    updated_points,
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

end = time.time()

print("Step 1 finished in", round(end - start, 2), "seconds.")

# Make the RGB values range [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)
# Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img_step_1 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


# ===================== STEP 2 ======================#
transform.translate(data["t_0"])
updated_points = transform.transform_pts(data["v_pos"])


# Set start time
start = time.time()

# Use the function to create an image
img = render_object(
    updated_points,
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


end = time.time()

print("Step 2 finished in", round(end - start, 2), "seconds.")


# Make the RGB values range [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)
# Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img_step_2 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


# ===================== STEP 3 ======================#

# Set start time
start = time.time()

transform.translate(data["t_1"])
updated_points = transform.transform_pts(data["v_pos"])

# Use the function to create an image
img = render_object(
    updated_points,
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

end = time.time()

print("Step 3 finished in", round(end - start, 2), "seconds.")


# Make the RGB values range [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)
# Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img_step_3 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Save all images
cv2.imwrite("step_0.jpg", rgb_img_step_0)
cv2.imwrite("step_1.jpg", rgb_img_step_1)
cv2.imwrite("step_2.jpg", rgb_img_step_2)
cv2.imwrite("step_3.jpg", rgb_img_step_3)

print()
print("=================")
print("Saved all images!")
print("=================")
print()

# Show all images
cv2.imshow("Image Step 0", rgb_img_step_0)
cv2.waitKey(100)
cv2.imshow("Image Step 1", rgb_img_step_1)
cv2.waitKey(100)
cv2.imshow("Image Step 2", rgb_img_step_2)
cv2.waitKey(100)
cv2.imshow("Image Step 3", rgb_img_step_3)
print("Press any key to close all images!")
cv2.waitKey(0)


cv2.destroyAllWindows()
