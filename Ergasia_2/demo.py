import cv2
import numpy as np
from render_object import render_object
from transform import Transform

# Load the data
data = np.load("hw2.npy", allow_pickle=True).item()

# ===================== STEP 0 ======================#
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
# Make the RGB values range [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)
# Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# Save the image as jpg
cv2.imwrite("step_0.jpg", rgb_img)
# Show the image
cv2.imshow("Image Step 0", rgb_img)
cv2.waitKey(0)

# ===================== STEP 1 ======================#
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
# Make the RGB values range [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)
# Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# Save the image as jpg
cv2.imwrite("step_1.jpg", rgb_img)
# Show the image
cv2.imshow("Image Step 1", rgb_img)
cv2.waitKey(0)


# ===================== STEP 2 ======================#
transform.translate(data["t_0"])
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
# Make the RGB values range [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)
# Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# Save the image as jpg
cv2.imwrite("step_2.jpg", rgb_img)
# Show the image
cv2.imshow("Image Step 2", rgb_img)
cv2.waitKey(0)


# ===================== STEP 3 ======================#
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
# Make the RGB values range [0,255] instead of [0,1]
img *= 255
img = img.astype(np.uint8)
# Change colorspace from RGB to BGR in order to view the image correctly with OpenCV
rgb_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# Save the image as jpg
cv2.imwrite("step_3.jpg", rgb_img)
# Show the image
cv2.imshow("Image Step 3", rgb_img)
cv2.waitKey(0)


cv2.destroyAllWindows()
