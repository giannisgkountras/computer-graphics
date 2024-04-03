import numpy as np
import cv2
from vector_interp import vector_interp
from f_shading import f_shading
from render_img import render_img
from g_shading import g_shading
from f_shading_2 import f_shading_2

data = np.load("hw1.npy", allow_pickle=True).item()
# print(data)

img_f = np.ones((512, 512, 3), dtype=float)
img_g = np.ones((512, 512, 3), dtype=float)
img = np.ones((512, 512, 3), dtype=float)

img = f_shading_2(
    img,
    [
        [20, 20],
        [250, 80],
        [300, 400],
    ],
    [[1.0, 0.0, 0.0], [0, 1, 1], [1, 1.0, 0]],
)


# img_g = g_shading(
#     img_g,
#     [[20, 20], [50, 20], [500, 400]],
#     [[1.0, 1.0, 0.0], [1.0, 1.0, 1.0], [0.9, 0.9, 0.9]],
# )

# img_g = render_img(data["faces"], data["vertices"], data["vcolors"], data["depth"], "g")
# img_f = render_img(data["faces"], data["vertices"], data["vcolors"], data["depth"], "f")

img_g *= 255
img_f *= 255
img *= 255

img_g = img_g.astype(np.uint8)
img_f = img_f.astype(np.uint8)
img = img.astype(np.uint8)

rgb_img_g = cv2.cvtColor(img_g, cv2.COLOR_BGR2RGB)
rgb_img_f = cv2.cvtColor(img_f, cv2.COLOR_BGR2RGB)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# cv2.imshow("Flat", rgb_img_g)
# cv2.imshow("Gouraud", rgb_img_f)
cv2.imshow("f_shading", rgb_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
