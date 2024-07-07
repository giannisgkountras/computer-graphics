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
start = time.time()
img_ambient_gouraud = render_object(
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
    0,
    0,
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
    "Render with Gouraud Shading and Ambient Lighting finished in",
    round(end - start, 2),
    "seconds.",
)


# Set start time
start = time.time()
img_diff_gouraud = render_object(
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
    0,
    data["kd"],
    0,
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
    "Render with Gouraud Shading and Diffuse Lighting finished in",
    round(end - start, 2),
    "seconds.",
)


# Set start time
start = time.time()
img_spec_gouraud = render_object(
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
    0,
    0,
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
    "Render with Gouraud Shading and Specular Lighting finished in",
    round(end - start, 2),
    "seconds.",
)


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
img_all_gouraud_source1 = render_object(
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
    data["light_positions"][0],
    data["light_intensities"][0],
    data["Ia"],
    data["uvs"],
    data["face_uv_indices"],
    texture_map,
)

end = time.time()

print(
    "Render with Gouraud Shading and All Lighting Source 1 finished in",
    round(end - start, 2),
    "seconds.",
)

# Set start time
start = time.time()
img_all_gouraud_source2 = render_object(
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
    data["light_positions"][1],
    data["light_intensities"][1],
    data["Ia"],
    data["uvs"],
    data["face_uv_indices"],
    texture_map,
)

end = time.time()

print(
    "Render with Gouraud Shading and All Lighting Source 2 finished in",
    round(end - start, 2),
    "seconds.",
)

# Set start time
start = time.time()
img_all_gouraud_source3 = render_object(
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
    data["light_positions"][2],
    data["light_intensities"][2],
    data["Ia"],
    data["uvs"],
    data["face_uv_indices"],
    texture_map,
)

end = time.time()

print(
    "Render with Gouraud Shading and All Lighting Source 3 finished in",
    round(end - start, 2),
    "seconds.",
)


# =======================================================================================================#
# PHONG SHADING
start = time.time()
img_ambient_phong = render_object(
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
    0,
    0,
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
    "Render with Phong Shading and Ambient Lighting finished in",
    round(end - start, 2),
    "seconds.",
)


# Set start time
start = time.time()
img_diff_phong = render_object(
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
    0,
    data["kd"],
    0,
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
    "Render with Phong Shading and Diffuse Lighting finished in",
    round(end - start, 2),
    "seconds.",
)


# Set start time
start = time.time()
img_spec_phong = render_object(
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
    0,
    0,
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
    "Render with Phong Shading and Specular Lighting finished in",
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


# Set start time
start = time.time()
img_all_phong_source1 = render_object(
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
    data["light_positions"][0],
    data["light_intensities"][0],
    data["Ia"],
    data["uvs"],
    data["face_uv_indices"],
    texture_map,
)

end = time.time()

print(
    "Render with Phong Shading and All Lighting Source 1 finished in",
    round(end - start, 2),
    "seconds.",
)

# Set start time
start = time.time()
img_all_phong_source2 = render_object(
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
    data["light_positions"][1],
    data["light_intensities"][1],
    data["Ia"],
    data["uvs"],
    data["face_uv_indices"],
    texture_map,
)

end = time.time()

print(
    "Render with Phong Shading and All Lighting Source 2 finished in",
    round(end - start, 2),
    "seconds.",
)

# Set start time
start = time.time()
img_all_phong_source3 = render_object(
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
    data["light_positions"][2],
    data["light_intensities"][2],
    data["Ia"],
    data["uvs"],
    data["face_uv_indices"],
    texture_map,
)

end = time.time()

print(
    "Render with Phong Shading and All Lighting Source 3 finished in",
    round(end - start, 2),
    "seconds.",
)

# Convert the images to OpenCV format
img_ambient_gouraud = prepareImgForOpenCV(img_ambient_gouraud)
img_diff_gouraud = prepareImgForOpenCV(img_diff_gouraud)
img_spec_gouraud = prepareImgForOpenCV(img_spec_gouraud)
img_all_gouraud = prepareImgForOpenCV(img_all_gouraud)
img_all_gouraud_source1 = prepareImgForOpenCV(img_all_gouraud_source1)
img_all_gouraud_source2 = prepareImgForOpenCV(img_all_gouraud_source2)
img_all_gouraud_source3 = prepareImgForOpenCV(img_all_gouraud_source3)
img_ambient_phong = prepareImgForOpenCV(img_ambient_phong)
img_diff_phong = prepareImgForOpenCV(img_diff_phong)
img_spec_phong = prepareImgForOpenCV(img_spec_phong)
img_all_phong = prepareImgForOpenCV(img_all_phong)
img_all_phong_source1 = prepareImgForOpenCV(img_all_phong_source1)
img_all_phong_source2 = prepareImgForOpenCV(img_all_phong_source2)
img_all_phong_source3 = prepareImgForOpenCV(img_all_phong_source3)

print()
print("Saving images...")
# Save the images
cv2.imwrite("./Results/Gouraud Ambient.jpg", img_ambient_gouraud)
cv2.imwrite("./Results/Gouraud Diffuse.jpg", img_diff_gouraud)
cv2.imwrite("./Results/Gouraud Specular.jpg", img_spec_gouraud)
cv2.imwrite("./Results/Gouraud All Lighting All Sources.jpg", img_all_gouraud)
cv2.imwrite("./Results/Gouraud All Source 1.jpg", img_all_gouraud_source1)
cv2.imwrite("./Results/Gouraud All Source 2.jpg", img_all_gouraud_source2)
cv2.imwrite("./Results/Gouraud All Source 3.jpg", img_all_gouraud_source3)

cv2.imwrite("./Results/Phong Ambient.jpg", img_ambient_phong)
cv2.imwrite("./Results/Phong Diffuse.jpg", img_diff_phong)
cv2.imwrite("./Results/Phong Specular.jpg", img_spec_phong)
cv2.imwrite("./Results/Phong All Lighting All Sources.jpg", img_all_phong)
cv2.imwrite("./Results/Phong All Source 1.jpg", img_all_phong_source1)
cv2.imwrite("./Results/Phong All Source 2.jpg", img_all_phong_source2)
cv2.imwrite("./Results/Phong All Source 3.jpg", img_all_phong_source3)

print()
print("All images saved in the Results folder.")

# Display the images

cv2.imshow("Gouraud Ambient", img_ambient_gouraud)
cv2.waitKey(100)
cv2.imshow("Gouraud Diffuse", img_diff_gouraud)
cv2.waitKey(100)
cv2.imshow("Gouraud Specular", img_spec_gouraud)
cv2.waitKey(100)
cv2.imshow("Gouraud All Lighting All Sources", img_all_gouraud)
cv2.waitKey(100)
cv2.imshow("Gouraud All Source 1", img_all_gouraud_source1)
cv2.waitKey(100)
cv2.imshow("Gouraud All Source 2", img_all_gouraud_source2)
cv2.waitKey(100)
cv2.imshow("Gouraud All Source 3", img_all_gouraud_source3)
cv2.waitKey(100)


cv2.imshow("Phong Ambient", img_ambient_phong)
cv2.waitKey(100)
cv2.imshow("Phong Diffuse", img_diff_phong)
cv2.waitKey(100)
cv2.imshow("Phong Specular", img_spec_phong)
cv2.waitKey(100)
cv2.imshow("Phong All Lighting All Sources", img_all_phong)
cv2.waitKey(100)
cv2.imshow("Phong All Source 1", img_all_phong_source1)
cv2.waitKey(100)
cv2.imshow("Phong All Source 2", img_all_phong_source2)
cv2.waitKey(100)
cv2.imshow("Phong All Source 3", img_all_phong_source3)
cv2.waitKey(100)

print("Press any key to close.")

cv2.waitKey(0)


cv2.destroyAllWindows()
