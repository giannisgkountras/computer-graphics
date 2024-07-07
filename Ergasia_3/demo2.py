import cv2
import numpy as np
from render_object import render_object
from prepareImgForOpenCV import prepareImgForOpenCV
import time

# Load the data
data = np.load("hw3.npy", allow_pickle=True).item()
texture_map = cv2.imread("cat_diff.png")
# Convert the BGR texture_map to RGB format
texture_map = cv2.cvtColor(texture_map, cv2.COLOR_BGR2RGB)
texture_map = texture_map.astype(np.float32) / 255.0


# ===================== STEP 0 ======================#
# Use the function to create an image

# Set start time

# Set start time
start = time.time()
img_all_gouraud = render_object(
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
    data["uvs"],
    data["face_uv_indices"],
    texture_map,
)

end = time.time()

print(
    "Render with Gouraud Shading and All Lighting finished in",
    round(end - start, 2),
    "seconds.",
)


# Set start time
start = time.time()
img_all_phong = render_object(
    "phong",
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
    data["uvs"],
    data["face_uv_indices"],
    texture_map,
)

end = time.time()

print(
    "Render with Phong Shading and All Lighting finished in",
    round(end - start, 2),
    "seconds.",
)


# Convert the images to OpenCV format

img_all_gouraud = prepareImgForOpenCV(img_all_gouraud)


img_all_phong = prepareImgForOpenCV(img_all_phong)


print()
print("Saving images...")
# Save the images

cv2.imwrite("./Results/Gouraud All Lighting All Sources.jpg", img_all_gouraud)


cv2.imwrite("./Results/Phong All Lighting All Sources.jpg", img_all_phong)


print()
print("All images saved in the Results folder.")

# Display the images


cv2.imshow("Gouraud All Lighting All Sources", img_all_gouraud)
cv2.waitKey(100)

cv2.imshow("Phong All Lighting All Sources", img_all_phong)
cv2.waitKey(100)

print("Press any key to close.")

cv2.waitKey(0)


cv2.destroyAllWindows()
