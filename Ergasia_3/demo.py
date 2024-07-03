import cv2
import numpy as np
from render_object import render_object
from prepareImgForOpenCV import prepareImgForOpenCV
import time

# Load the data
data = np.load("hw3.npy", allow_pickle=True).item()

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
)

end = time.time()

print(
    "Render with Gouraud Shading and All Lighting Source 3 finished in",
    round(end - start, 2),
    "seconds.",
)

# Make the RGB values range [0,255] instead of [0,1]
img_ambient_gouraud = prepareImgForOpenCV(img_ambient_gouraud)
img_diff_gouraud = prepareImgForOpenCV(img_diff_gouraud)
img_spec_gouraud = prepareImgForOpenCV(img_spec_gouraud)
img_all_gouraud = prepareImgForOpenCV(img_all_gouraud)
img_all_gouraud_source1 = prepareImgForOpenCV(img_all_gouraud_source1)
img_all_gouraud_source2 = prepareImgForOpenCV(img_all_gouraud_source2)
img_all_gouraud_source3 = prepareImgForOpenCV(img_all_gouraud_source3)

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

cv2.imwrite("./Results/Gouraud Ambient.jpg", img_ambient_gouraud)
cv2.imwrite("./Results/Gouraud Diffuse.jpg", img_diff_gouraud)
cv2.imwrite("./Results/Gouraud Specular.jpg", img_spec_gouraud)
cv2.imwrite("./Results/Gouraud All Lighting All Sources.jpg", img_all_gouraud)
cv2.imwrite("./Results/Gouraud All Source 1.jpg", img_all_gouraud_source1)
cv2.imwrite("./Results/Gouraud All Source 2.jpg", img_all_gouraud_source2)
cv2.imwrite("./Results/Gouraud All Source 3.jpg", img_all_gouraud_source3)


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
)
end = time.time()

print(
    "Render with Phong Shading and All Lighting Sources finished in",
    round(end - start, 2),
    "seconds.",
)

img_all_phong = prepareImgForOpenCV(img_all_phong)
cv2.imshow("Phong All Lighting All Sources", img_all_phong)
cv2.imwrite("./Results/Phong All Lighting All Sources.jpg", img_all_phong)

cv2.waitKey(0)


cv2.destroyAllWindows()
